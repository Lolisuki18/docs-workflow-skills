#!/usr/bin/env python3
"""Fill a table of a course .docx template from a CSV file, keeping the template's own formatting.

Usage:
  python fill_docx_table.py template.docx out.docx --csv rows.csv [--table N] [--replace-sample | --append]
  python fill_docx_table.py template.docx --list            # show tables with their header rows

The first CSV row must equal the table's header row (compared ignoring case and extra spaces), so
columns can never shift. The template file is never modified: the result goes to out.docx.
Blank template rows are filled first; extra rows are created by copying the last row, so fonts,
borders and widths stay as in the template. Rows that already contain sample text (for example
"Feature 1", "dd/MM/yyyy") are never overwritten silently: choose --replace-sample (remove them)
or --append (keep them and add after). Merged cells are written once. Requires python-docx
(pip install python-docx). Windows without a working `python` alias: use `py`.
Only table cells are touched; paragraphs, headings, images and diagrams stay as they are.
"""
import argparse, copy, csv, re, sys

def norm(s): return re.sub(r'\s+', ' ', s or '').strip().lower()

def unique_cells(row):
    seen, out = set(), []
    for c in row.cells:
        if c._tc in seen: continue
        seen.add(c._tc); out.append(c)
    return out

def set_text(cell, text):
    paras = cell.paragraphs
    lines = text.split('\n')
    p = paras[0]
    for extra in paras[1:]:
        extra._element.getparent().remove(extra._element)
    for r in p.runs[1:]:
        r._element.getparent().remove(r._element)
    if p.runs: p.runs[0].text = lines[0]
    else: p.add_run(lines[0])
    for ln in lines[1:]:
        newp = copy.deepcopy(p._element); p._element.getparent().append(newp)
        from docx.text.paragraph import Paragraph
        np_ = Paragraph(newp, p._parent)
        np_.runs[0].text = ln

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('template'); ap.add_argument('out', nargs='?'); ap.add_argument('--csv'); ap.add_argument('--table', type=int)
    ap.add_argument('--list', action='store_true'); ap.add_argument('--replace-sample', action='store_true'); ap.add_argument('--append', action='store_true')
    a = ap.parse_args()
    try:
        import docx
    except ImportError:
        sys.exit('python-docx is required: pip install python-docx')
    d = docx.Document(a.template)
    if a.list:
        for i, t in enumerate(d.tables):
            print(f'[{i}] {len(t.rows)} rows x {len(t.columns)} cols | header: ' + ' | '.join(c.text.strip().replace("\n", " / ") for c in unique_cells(t.rows[0])))
        return
    if not (a.csv and a.out): ap.error('give out.docx and --csv (or use --list)')
    rows = list(csv.reader(open(a.csv, encoding='utf-8-sig', newline='')))
    if not rows: sys.exit('ERROR: empty CSV')
    header, data = rows[0], [r for r in rows[1:] if any(c.strip() for c in r)]
    cands = [a.table] if a.table is not None else range(len(d.tables))
    target = None
    for i in cands:
        t = d.tables[i]
        if [norm(c.text) for c in unique_cells(t.rows[0])] == [norm(h) for h in header]:
            target = t; break
    if target is None:
        sys.exit('ERROR: no table whose header row equals the CSV header: ' + ' | '.join(header) + '\nUse --list to see the tables.')
    body = target.rows[1:]
    if not body:
        sys.exit('ERROR: the table has no data row to copy formatting from (keep at least one row in the template).')
    template_tr = copy.deepcopy(target.rows[-1]._tr)  # formatting source, taken before any removal
    sample = [r for r in body if any(c.text.strip() for c in unique_cells(r))]
    if sample and not (a.replace_sample or a.append):
        sys.exit(f'ERROR: the table has {len(sample)} row(s) with sample text (first: '
                 f'{[c.text.strip() for c in unique_cells(sample[0])][:3]}). Use --replace-sample to remove them or --append to keep them.')
    if a.replace_sample:
        for r in sample: r._tr.getparent().remove(r._tr)
        body = [r for r in target.rows[1:]]
    free = [r for r in body if not any(c.text.strip() for c in unique_cells(r))]
    written = 0
    for rec in data:
        if free: row = free.pop(0)
        else:
            new_tr = copy.deepcopy(template_tr); target._tbl.append(new_tr)
            row = target.rows[-1]
            for c in unique_cells(row): set_text(c, '')
        cells = unique_cells(row)
        if len(rec) > len(cells): sys.exit(f'ERROR: CSV row has {len(rec)} values but the table has {len(cells)} columns: {rec}')
        for c, v in zip(cells, rec): set_text(c, v)
        written += 1
    d.save(a.out)
    print(f'wrote {a.out}: {written} row(s) filled into the table with header: ' + ' | '.join(header))

if __name__ == '__main__':
    main()
