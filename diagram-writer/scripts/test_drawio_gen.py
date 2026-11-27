#!/usr/bin/env python3
"""Smoke test for drawio_gen.py: edges that skip empty layers (forced layers) must not crash.

Run: python test_drawio_gen.py
"""
import os, sys, xml.dom.minidom as md
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import drawio_gen

def spec(direction):
    return {'title': 'skip empty layers', 'direction': direction,
            'nodes': [{'id': 'a', 'label': 'A', 'layer': 0}, {'id': 'b', 'label': 'B', 'layer': 3}],
            'edges': [{'from': 'a', 'to': 'b', 'label': 'skips layers 1-2'}]}

for d in ('LR', 'TB'):
    xml = drawio_gen.build(spec(d))
    md.parseString(xml)
    assert 'source="a" target="b"' in xml and '<Array as="points">' in xml, d
print('ok: edges across empty layers build in LR and TB')
