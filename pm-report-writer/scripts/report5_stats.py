#!/usr/bin/env python3
"""Compute Report 5 statistics from REAL test results (never invents numbers).

Usage:
  python report5_stats.py results.csv                # integration/system/acceptance (Test Report layout)
  python report5_stats.py results.csv --unit         # unit tests (Unit Test layout)
  python report5_stats.py results.csv --csv out.csv  # also write the statistics table as CSV

results.csv columns (header row required, extra columns ignored):
  test report mode : module, id, result            result in Passed | Failed | Pending | N/A
  --unit mode      : function, id, result, type    result in Passed | Failed | Untested ; type in N | A | B
Optional column in both: round (1..3). Without --round-filter all rows are counted.

Formulas (from the Report5 templates):
  Test coverage (%)            = (Passed + Failed) * 100 / (Total - N/A)
  Test successful coverage (%) = Passed * 100 / (Total - N/A)
  Unit mode extra: Normal/Abnormal/Boundary % = count of type / Total
Total = number of rows (test cases). If the CSV is empty the script stops: no results, no statistics.
"""
import argparse, csv, sys
from collections import OrderedDict

def norm(s):
    s = (s or '').strip().lower()
    return {'pass': 'Passed', 'passed': 'Passed', 'p': 'Passed', 'ok': 'Passed',
            'fail': 'Failed', 'failed': 'Failed', 'f': 'Failed', 'ng': 'Failed',
            'pending': 'Pending', 'untested': 'Untested', 'n/a': 'N/A', 'na': 'N/A'}.get(s)

def pct(a, b): return f'{a * 100 / b:.2f}' if b else 'n/a'

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('csv_in'); ap.add_argument('--unit', action='store_true'); ap.add_argument('--csv')
    ap.add_argument('--round-filter', type=int)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.csv_in, encoding='utf-8-sig', newline='')))
    if not rows:
        print('NO RESULTS: the file has no rows. Report "[Cần bổ sung: chưa có kết quả chạy test]"; do not enter numbers.'); sys.exit(2)
    key = 'function' if a.unit else 'module'
    for need in (key, 'id', 'result') + (('type',) if a.unit else ()):
        if need not in rows[0]:
            print(f'ERROR: column "{need}" missing; found {list(rows[0])}'); sys.exit(2)
    stats = OrderedDict(); bad = []
    for n, r in enumerate(rows, 2):
        if a.round_filter and (r.get('round') or '').strip() and int(r['round']) != a.round_filter: continue
        res = norm(r['result'])
        if res is None or (a.unit and res in ('Pending', 'N/A')) or (not a.unit and res == 'Untested'):
            bad.append(f'line {n}: unknown result {r["result"]!r}'); continue
        m = stats.setdefault(r[key].strip(), {'Passed': 0, 'Failed': 0, 'Pending': 0, 'Untested': 0, 'N/A': 0, 'N': 0, 'A': 0, 'B': 0, 'total': 0, 'ids': set()})
        if r['id'].strip() in m['ids']:
            bad.append(f'line {n}: duplicate id {r["id"]!r} in {r[key]!r}'); continue
        m['ids'].add(r['id'].strip()); m['total'] += 1; m[res] += 1
        if a.unit:
            t = (r.get('type') or '').strip().upper()[:1]
            if t not in ('N', 'A', 'B'): bad.append(f'line {n}: type must be N, A or B, got {r.get("type")!r}'); m['total'] -= 1; m[res] -= 1; m['ids'].discard(r['id'].strip()); continue
            m[t] += 1
    if bad:
        print('PROBLEMS (rows skipped):'); [print(' -', b) for b in bad]
    if a.unit:
        head = ['No', 'Function code', 'Passed', 'Failed', 'Untested', 'N', 'A', 'B', 'Total Test Cases']
        cols = ['Passed', 'Failed', 'Untested', 'N', 'A', 'B', 'total']
    else:
        head = ['No', 'Module code', 'Passed', 'Failed', 'Pending', 'N/A', 'Number of test cases']
        cols = ['Passed', 'Failed', 'Pending', 'N/A', 'total']
    table = []
    for i, (name, m) in enumerate(stats.items(), 1):
        chk = (m['Passed'] + m['Failed'] + m['Untested']) if a.unit else (m['Passed'] + m['Failed'] + m['Pending'] + m['N/A'])
        if chk != m['total']: bad.append(f'{name}: result counts do not add up to total')
        if a.unit and m['N'] + m['A'] + m['B'] != m['total']: bad.append(f'{name}: N+A+B != total')
        table.append([i, name] + [m[c] for c in cols])
    sub = ['', 'Sub total'] + [sum(r[2 + k] for r in table) for k in range(len(cols))]
    table.append(sub)
    print('| ' + ' | '.join(head) + ' |'); print('|' + '---|' * len(head))
    for r in table: print('| ' + ' | '.join(str(x) for x in r) + ' |')
    d = dict(zip(cols, sub[2:]))
    na = d.get('N/A', 0)
    denom = d['total'] - na if not a.unit else d['total']
    cov = pct(d['Passed'] + d['Failed'], denom); suc = pct(d['Passed'], denom)
    print(f'\nTest coverage (%): {cov}   [(Passed + Failed) x 100 / ({"Total" if a.unit else "Total - N/A"}) = ({d["Passed"]} + {d["Failed"]}) x 100 / {denom}]')
    print(f'Test successful coverage (%): {suc}   [Passed x 100 / {denom}]')
    if a.unit:
        print('Normal case (%): ' + pct(d['N'], d['total']) + '   Abnormal case (%): ' + pct(d['A'], d['total']) + '   Boundary case (%): ' + pct(d['B'], d['total']))
    if bad: print('\nCHECKS FAILED:'); [print(' -', b) for b in bad if 'line' not in b]
    if a.csv:
        with open(a.csv, 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.writer(f); w.writerow(head); w.writerows(table)
        print(f'wrote {a.csv}')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
