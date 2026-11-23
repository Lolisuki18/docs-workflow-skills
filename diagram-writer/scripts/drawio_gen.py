#!/usr/bin/env python3
"""Generate a clean, editable .drawio (uncompressed mxGraphModel) from a JSON element list.

Usage: python drawio_gen.py spec.json out.drawio

spec.json:
{
  "title": "Architecture - Orders",
  "direction": "LR",                      // LR (layers left->right) or TB (top->bottom)
  "nodes": [
    {"id": "web", "label": "Web Client", "type": "rounded"},
    {"id": "db",  "label": "PostgreSQL", "type": "database"},
    {"id": "users", "label": "users", "type": "table",
     "columns": ["PK id : bigint", "email : varchar"]}
  ],
  "edges": [ {"from": "web", "to": "db", "label": "HTTPS"} ]
}

Node types: rounded (default), rect, ellipse, decision, actor, database, cloud, start, end, table.
Optional node keys: "layer" (force a layer index), "fill" (hex color).
The layout assigns layers by longest path, orders nodes inside a layer to reduce crossings, places
everything on a 10 px grid with the spacing from references/drawio-xml-guide.md and validates the
result (unique ids, edge endpoints exist, no overlapping vertices). Nothing is rendered here:
open the file in the diagrams.net / Draw.io Integration (hediet.vscode-drawio) editor to check it.
"""
import json, sys
from collections import defaultdict
from xml.sax.saxutils import escape

GAP_LAYER, GAP_NODE = 80, 40
STYLES = {
    'rounded':  'rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;',
    'rect':     'rounded=0;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;',
    'ellipse':  'ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;',
    'decision': 'rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;',
    'actor':    'shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;',
    'database': 'shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#d5e8d4;strokeColor=#82b366;',
    'cloud':    'ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;dashed=1;',
    'start':    'ellipse;html=1;fillColor=#000000;strokeColor=#000000;',
    'end':      'shape=doubleEllipse;html=1;fillColor=#ffffff;strokeColor=#000000;',
}
TABLE_STYLE = ('swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;'
               'resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;html=1;'
               'fillColor=#e1d5e7;strokeColor=#9673a6;')
COL_STYLE = ('text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;'
             'spacingRight=4;overflow=hidden;rotatable=0;html=1;')

def snap(v): return int(round(v / 10.0)) * 10

def size(n):
    t = n.get('type', 'rounded'); label = n.get('label', '')
    if t == 'start': return 30, 30
    if t == 'end': return 40, 40
    if t == 'actor': return 30, 60
    if t == 'table':
        longest = max([len(label)] + [len(c) for c in n.get('columns', [])])
        return snap(max(140, longest * 8 + 20)), 26 + 26 * len(n.get('columns', []))
    lines = max(1, -(-len(label) // 18))
    w = snap(max(120, min(len(label), 18) * 8 + 24))
    h = snap(max(60, 20 * lines + 30))
    if t in ('decision', 'ellipse', 'cloud'): w, h = snap(w * 1.2), snap(h * 1.3)
    return w, h

def layers_of(nodes, edges):
    ids = [n['id'] for n in nodes]
    out = defaultdict(list)
    for e in edges: out[e['from']].append(e['to'])
    state, back = {}, set()
    def dfs(u):
        state[u] = 1
        for v in out[u]:
            if state.get(v) == 1: back.add((u, v))
            elif v not in state: dfs(v)
        state[u] = 2
    for i in ids:
        if i not in state: dfs(i)
    layer = {i: 0 for i in ids}
    for _ in range(len(ids)):
        changed = False
        for e in edges:
            u, v = e['from'], e['to']
            if (u, v) in back or u == v: continue
            if layer[v] < layer[u] + 1: layer[v] = layer[u] + 1; changed = True
        if not changed: break
    for n in nodes:
        if 'layer' in n: layer[n['id']] = int(n['layer'])
    return layer

def order_layers(nodes, edges, layer):
    by = defaultdict(list)
    for n in nodes: by[layer[n['id']]].append(n['id'])
    pos = {i: k for L in by.values() for k, i in enumerate(L)}
    neigh = defaultdict(list)
    for e in edges: neigh[e['from']].append(e['to']); neigh[e['to']].append(e['from'])
    for _ in range(4):  # barycenter sweeps
        for L in sorted(by):
            def bary(i):
                ps = [pos[j] for j in neigh[i] if layer[j] != L]
                return sum(ps) / len(ps) if ps else pos[i]
            by[L].sort(key=lambda i: (bary(i), pos[i]))
            for k, i in enumerate(by[L]): pos[i] = k
    return by

def build(spec):
    nodes, edges = spec['nodes'], spec.get('edges', [])
    ids = [n['id'] for n in nodes]
    assert len(ids) == len(set(ids)), 'duplicate node ids'
    for e in edges:
        assert e['from'] in ids and e['to'] in ids, f"edge endpoint missing: {e}"
    horiz = spec.get('direction', 'LR').upper() == 'LR'
    layer = layers_of(nodes, edges)
    by = order_layers(nodes, edges, layer)
    sz = {n['id']: size(n) for n in nodes}
    place, cursor = {}, 40
    for L in sorted(by):
        group = by[L]
        main = max((sz[i][0] if horiz else sz[i][1]) for i in group)
        along = 40
        for i in group:
            w, h = sz[i]
            x, y = (cursor, along) if horiz else (along, cursor)
            place[i] = (snap(x), snap(y), w, h)
            along += (h if horiz else w) + GAP_NODE
        cursor += main + GAP_LAYER
    # centre shorter layers against the tallest one
    extent = {L: sum((sz[i][1] if horiz else sz[i][0]) for i in by[L]) + GAP_NODE * (len(by[L]) - 1) for L in by}
    biggest = max(extent.values())
    for L in by:
        shift = snap((biggest - extent[L]) / 2)
        for i in by[L]:
            x, y, w, h = place[i]
            place[i] = (x, y + shift, w, h) if horiz else (x + shift, y, w, h)
    # overlap validation
    items = list(place.items())
    for a in range(len(items)):
        for b in range(a + 1, len(items)):
            (i, (x1, y1, w1, h1)), (j, (x2, y2, w2, h2)) = items[a], items[b]
            assert x1 + w1 <= x2 or x2 + w2 <= x1 or y1 + h1 <= y2 or y2 + h2 <= y1, f'overlap {i}/{j}'
    maxx = max(x + w for x, y, w, h in place.values()) + 40
    maxy = max(y + h for x, y, w, h in place.values()) + 40
    cells = []
    cid = 2
    for n in nodes:
        i = n['id']; x, y, w, h = place[i]; t = n.get('type', 'rounded')
        label = '' if t in ('start',) else escape(n.get('label', ''), {'"': '&quot;'})
        style = TABLE_STYLE if t == 'table' else STYLES[t]
        if n.get('fill'): style += f"fillColor={n['fill']};"
        if t == 'table': w, h = w, 26
        cells.append(f'<mxCell id="{escape(i)}" value="{label}" style="{style}" vertex="1" parent="1">'
                     f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        if t == 'table':
            for k, col in enumerate(n.get('columns', [])):
                cells.append(f'<mxCell id="{escape(i)}__c{k}" value="{escape(col, {chr(34): "&quot;"})}" style="{COL_STYLE}" vertex="1" parent="{escape(i)}">'
                             f'<mxGeometry y="{26 + 26 * k}" width="{w}" height="26" as="geometry"/></mxCell>')
    for k, e in enumerate(edges):
        lab = escape(e.get('label', ''), {'"': '&quot;'})
        cells.append(f'<mxCell id="e{k + 1}" value="{lab}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;'
                     f'labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{escape(e["from"])}" target="{escape(e["to"])}">'
                     f'<mxGeometry relative="1" as="geometry"/></mxCell>')
    title = escape(spec.get('title', 'Diagram'), {'"': '&quot;'})
    pw, ph = max(1169, snap(maxx)), max(827, snap(maxy))
    return ('<mxfile host="app.diagrams.net">\n'
            f'  <diagram id="d1" name="{title}">\n'
            f'    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
            f'fold="1" page="1" pageScale="1" pageWidth="{pw}" pageHeight="{ph}" math="0" shadow="0">\n'
            '      <root>\n        <mxCell id="0"/>\n        <mxCell id="1" parent="0"/>\n'
            + '\n'.join('        ' + c for c in cells) +
            '\n      </root>\n    </mxGraphModel>\n  </diagram>\n</mxfile>\n')

def main():
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(2)
    spec = json.load(open(sys.argv[1], encoding='utf-8'))
    xml = build(spec)
    import xml.dom.minidom as md
    md.parseString(xml)  # well-formedness check
    open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write(xml)
    print(f'wrote {sys.argv[2]}: {len(spec["nodes"])} nodes, {len(spec.get("edges", []))} edges (validated: unique ids, endpoints, no overlaps).')
    print('Reminder: install Draw.io Integration (hediet.vscode-drawio) to open and edit this file in your IDE.')

if __name__ == '__main__':
    main()
