#!/usr/bin/env python3
"""Build paste-ready .xlsx workbooks with the template sheet names and column headers from CSV files.

Usage:
  python csv_to_xlsx.py tracking --dir DIR --out Report3_Project_Tracking.xlsx
      DIR holds wbs.csv, issues.csv, defects.csv, qa.csv (any may be missing)
  python csv_to_xlsx.py weekly --dir DIR --group "Group name" --week "dd/mm/yyyy-dd/mm/yyyy" --sheet W3 --out weekly.xlsx
      DIR holds status.csv, issues.csv, next.csv, other.csv

Each CSV must start with the template header row (see references/*-template.md); a different header is an
error, so columns can never silently shift. Rows are copied as given: nothing is invented, and no
placeholder rows are added. Requires openpyxl (pip install openpyxl). The output is a plain workbook that
mirrors the structure; it is not the original course file (copy the rows into that file if required).
"""
import argparse, csv, os, sys

TRACKING = {
    'WBS': ('wbs.csv', 'PROJECT WORK BREAKDOWN STRUCTURE', ['#', 'Function/Screen', 'Feature', 'Level*', 'Function/Screen Details', 'Planned', 'Status']),
    'Issues': ('issues.csv', 'PROJECT ISSUES', ['#', 'Issue', 'Potential Impact', 'Priority', 'Owner', 'Open Date', 'Close Date', 'Status', 'Notes']),
    'Defects': ('defects.csv', 'PROJECT DEFECTS', ['Feature', 'Function/Screen', 'Tester', 'Defect Description', 'Assign To', 'Status', 'Notes']),
    'Q&A': ('qa.csv', 'PROJECT Q&A', ['Date', 'Question', 'By', 'Priority', 'Status', 'Note (answer, other notes)']),
}
WEEKLY = [
    ('I. Status Report', 'status.csv', ['#', 'Project Task', 'In-charge', 'Status', 'Notes (Work Item in Details)']),
    ('II. Project Issues', 'issues.csv', ['#', 'Project Issue', 'Owner', 'Status', 'Notes (Solution, Suggestion, etc.)']),
    ('III. Next Week Plan', 'next.csv', ['#', 'Project Work Item', 'In-charge', 'Deadline', 'Notes (Task Details, etc.)']),
    ('IV. Other Project Masters/Suggestions', 'other.csv', ['#', 'Project Matter/Suggestions', 'Raised By', 'Date', 'Notes']),
]

def read(path, header):
    with open(path, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    if not rows or [c.strip() for c in rows[0]] != header:
        sys.exit(f'ERROR {path}: header must be exactly {header}; found {rows[0] if rows else "empty file"}')
    return [r for r in rows[1:] if any(c.strip() for c in r)]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('kind', choices=['tracking', 'weekly']); ap.add_argument('--dir', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--group', default=''); ap.add_argument('--week', default=''); ap.add_argument('--sheet', default='Wx')
    a = ap.parse_args()
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill, Alignment
    except ImportError:
        sys.exit('openpyxl is required: pip install openpyxl')
    bold = Font(bold=True); fill = PatternFill('solid', fgColor='D9E1F2')
    wb = Workbook(); wb.remove(wb.active)
    def table(ws, r0, header, rows):
        for c, h in enumerate(header, 1):
            cell = ws.cell(r0, c, h); cell.font = bold; cell.fill = fill
        for i, row in enumerate(rows, 1):
            for c, v in enumerate(row[:len(header)], 1):
                ws.cell(r0 + i, c, v).alignment = Alignment(wrap_text=True, vertical='top')
        return r0 + len(rows) + 2
    if a.kind == 'tracking':
        for sheet, (fn, title, header) in TRACKING.items():
            ws = wb.create_sheet(sheet); ws['A1'] = title; ws['A1'].font = Font(bold=True, size=13)
            path = os.path.join(a.dir, fn)
            table(ws, 3, header, read(path, header) if os.path.exists(path) else [])
            for i, h in enumerate(header, 1): ws.column_dimensions[chr(64 + i)].width = max(14, min(50, len(h) + 8))
    else:
        ws = wb.create_sheet(a.sheet[:31]); ws['A1'] = 'PROJECT REPORT'; ws['A1'].font = Font(bold=True, size=13)
        ws['A2'], ws['B2'] = 'Group', a.group; ws['A3'], ws['B3'] = 'Week', a.week
        r = 5
        for title, fn, header in WEEKLY:
            ws.cell(r, 1, title).font = bold
            path = os.path.join(a.dir, fn)
            r = table(ws, r + 1, header, read(path, header) if os.path.exists(path) else []) + 1
        for col, w in zip('ABCDE', (6, 40, 16, 16, 50)): ws.column_dimensions[col].width = w
    wb.save(a.out)
    print(f'wrote {a.out}: sheets {wb.sheetnames}')

if __name__ == '__main__':
    main()
