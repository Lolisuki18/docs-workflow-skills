# draw.io (`.drawio`) XML Guide

Build `.drawio` files that open cleanly in diagrams.net / the VS Code extension and can be edited by drag and drop. The code diagram (Mermaid/PlantUML) stays canonical; the `.drawio` is a visual export built from the same element list.

## 1. File skeleton (uncompressed XML only)

```xml
<mxfile host="app.diagrams.net">
  <diagram id="erd-orders" name="ERD - Orders">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1"
                  connect="1" arrows="1" fold="1" page="1" pageScale="1"
                  pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- cells here, all with parent="1" (or a container id) -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Rules:
- Do **not** compress (`<diagram>` must contain plain `<mxGraphModel>`, not base64/deflate).
- Cells `id="0"` and `id="1"` are mandatory; every other cell has a unique id and a valid `parent`.
- One `<diagram>` page per diagram; name pages after the diagram. Multiple pages allowed in one file.
- Escape XML: `&amp; &lt; &gt; &quot;` in `value`. Line breaks in labels: `&lt;br&gt;` with `html=1` in style.
- Ids: stable, readable (`t_users`, `e_users_orders`) - not random, so regenerations diff cleanly.

## 2. Vertex and edge cells

Vertex:
```xml
<mxCell id="n1" value="Place order" style="rounded=1;whiteSpace=wrap;html=1;"
        vertex="1" parent="1">
  <mxGeometry x="200" y="120" width="140" height="60" as="geometry"/>
</mxCell>
```
Edge (always attach to source/target ids, never float):
```xml
<mxCell id="e1" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;"
        edge="1" parent="1" source="n1" target="n2">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## 3. Layout rules (no overlapping text or arrows)

- Grid: all x, y, width, height multiples of 10.
- Spacing (what `scripts/drawio_gen.py` emits): 60 px between sibling nodes, 160 px between layers (more when edge labels are long). Hand-made files: >= 60 px between nodes, >= 80 px between layers/lanes.
- Lay out in layers: flow left->right (architecture, sequence-like) or top->bottom (activity). Do not place a node on an edge's path.
- Edges: `edgeStyle=orthogonalEdgeStyle` with `endArrow`; add `<Array as="points">` waypoints only to avoid crossing. Minimise crossings by ordering nodes by connectivity. Label edges with `value`, `labelBackgroundColor=#ffffff` so text stays readable.
- Node size: width >= 120 for labels up to ~18 chars; use `whiteSpace=wrap` and enough height (20 px per text line + padding). Never let text overflow the shape.
- Groups/containers: use a parent container cell (`container=1`) for swimlanes/boundaries and set children `parent` to the container id with coordinates relative to it.
- Page: keep within one page (1169x827) when possible; otherwise widen `pageWidth/pageHeight`.
- Colors: light fills, dark text, 2-3 colors max, consistent meaning (e.g. blue = internal service, grey = external). Do not rely on color alone.

## 4. Per-type styles

| Type | Shapes / styles |
|---|---|
| Use Case | actor: `shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;` ; use case: `ellipse;whiteSpace=wrap;html=1;` ; system boundary: `rounded=0;whiteSpace=wrap;html=1;fillColor=none;container=1;` ; association: plain line; include/extend: `dashed=1;endArrow=open;` + label `<<include>>` |
| ERD | table as swimlane: `swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=28;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;` (header 28 px, `collapsible=0` so tables do not fold; the generator uses this) with one child text cell per column (`text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;rotatable=0;connectable=0;html=1;` , height 26, first at y=28, value `PK id : bigint`). Relationships: `edgeStyle=entityRelationEdgeStyle;endArrow=ERmany;startArrow=ERone;endFill=0;startFill=0;` (use `ERzeroToMany`, `ERmandOne`, `ERoneToMany` as needed) |
| Sequence | lifeline: `shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=0;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={"curved":0,"rounded":0};` height >= 300; messages: horizontal edges, sync `endArrow=block`, return `dashed=1;endArrow=open`. Keep message order top->bottom with 40 px steps |
| Activity | start `ellipse;fillColor=#000000;` (30x30), end `shape=doubleEllipse;` , action `rounded=1;`, decision `rhombus;`, swimlane per actor: `swimlane;horizontal=0;` or `shape=table` lanes. Label every decision exit |
| State Machine | state `rounded=1;arcSize=30;whiteSpace=wrap;html=1;`, initial black circle, final `shape=doubleEllipse;`, transitions with `trigger [guard] / action` labels |
| Architecture | components `rounded=1;`, database `shape=cylinder3;`, external service `shape=cloud;` or dashed border, boundaries as containers; label edges with protocol |

## 5. Generation procedure

1. Start from the verified element list (same one used for the Mermaid/PlantUML version).
2. Assign layers/positions on the 10-px grid; compute coordinates in a script or by hand - do not eyeball.
3. Emit XML: containers first, then vertices, then edges. Keep ids stable.
4. Self-check (below). Open-in-editor check is the user's step; state it was not rendered unless a tool did so.

## 6. Checklist before handover

- [ ] XML well-formed; single `<mxfile>`, uncompressed `<mxGraphModel>`.
- [ ] Cells `0` and `1` present; every `parent`, `source`, `target` resolves to an existing id; ids unique.
- [ ] Every edge has source and target (no dangling arrows).
- [ ] Every element corresponds to the verified evidence list; names verbatim.
- [ ] No two vertices overlap; no label overflows its shape; no edge passes through an unrelated vertex.
- [ ] Coordinates on the 10-px grid; consistent spacing.
- [ ] Page names match diagram titles.
- [ ] Mermaid/PlantUML canonical version exists and matches this file's content.
- [ ] Extension reminder given: install **Draw.io Integration (`hediet.vscode-drawio`)**; offer to add it to `.vscode/extensions.json` (`"recommendations": ["hediet.vscode-drawio"]`), edit only after the user agrees and keep other entries.

## 7. Exporting images for Word/PDF

Tell the user: open the `.drawio`, use *File -> Export as -> PNG/SVG* (PNG at 200-300 % scale, transparent background off, border width 10, "include a copy of my diagram" on for round-trip editing). The skill does not generate binary images itself.
