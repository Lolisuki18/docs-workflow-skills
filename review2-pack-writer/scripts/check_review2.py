#!/usr/bin/env python3
"""Cross-checks for the Review 2 forms (BM01, BM02, BM04) written as Markdown.

Usage:
  python check_review2.py --bm01 BM01.md [--bm02 BM02.md] [--bm04 BM04.md] [--members N]
  python check_review2.py formula --features F --workflows W --transitions T --nfrs N [--committed C]

The Markdown files must keep the headings of the templates in references/
(e.g. "## 5. Known Gaps", "### 8.1 By workflow"). Exit code 1 if any check FAILS.
Checks implemented: X1, X3, X4(partial), X5, X7, X9, X10(partial), X13 and the BM01 word budget.
Everything else in the cross-check list stays a manual check.
"""
import argparse, math, re, sys

# ---------------------------------------------------------------- parsing
def split_sections(text):
    """Return list of (level, heading, body) for markdown headings."""
    parts, cur = [], None
    for line in text.splitlines():
        m = re.match(r'^(#{1,6})\s+(.*\S)\s*$', line)
        if m:
            if cur: parts.append(cur)
            cur = [len(m.group(1)), m.group(2), []]
        elif cur:
            cur[2].append(line)
    if cur: parts.append(cur)
    return [(l, h, '\n'.join(b)) for l, h, b in parts]

def find_section(sections, pattern):
    for l, h, b in sections:
        if re.search(pattern, h, re.I):
            return b
    return None

def split_row(line):
    """Split a markdown table row on pipes, keeping escaped pipes (\\|), pipes inside
    `code spans` and pipes inside [link](url) text/targets inside their cell."""
    s = line.strip()
    if s.startswith('|'): s = s[1:]
    if s.endswith('|') and not s.endswith('\\|'): s = s[:-1]
    cells, cur, i, tick, brk, par = [], '', 0, False, 0, 0
    while i < len(s):
        ch = s[i]
        if ch == '\\' and i + 1 < len(s) and s[i + 1] == '|':
            cur += '|'; i += 2; continue
        if ch == '`': tick = not tick
        elif not tick:
            if ch == '[': brk += 1
            elif ch == ']' and brk: brk -= 1
            elif ch == '(' and i > 0 and s[i - 1] == ']': par = 1
            elif ch == ')' and par: par = 0
        if ch == '|' and not tick and not brk and not par:
            cells.append(cur.strip()); cur = ''
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells

def tables(body):
    """Parse markdown tables in body -> list of (header, rows)."""
    out, cur = [], []
    for line in body.splitlines() + ['']:
        if line.strip().startswith('|'):
            cur.append(split_row(line))
        else:
            if len(cur) >= 2 and all(re.fullmatch(r':?-{2,}:?', c) or c == '' for c in cur[1]):
                out.append((cur[0], [r for r in cur[2:]]))
            cur = []
    return out

def data_rows(rows):
    """Rows whose first cell is non-empty (ignore blank template rows)."""
    return [r for r in rows if r and r[0].strip()]

def num(s):
    m = re.search(r'-?\d+(?:\.\d+)?', s or '')
    return float(m.group()) if m else None

def pair(s):
    m = re.findall(r'\d+', s or '')
    return tuple(int(x) for x in m[:2]) if len(m) >= 2 else ((int(m[0]), 0) if m else None)

def words(s):
    return len(re.findall(r'\S+', s))

# ---------------------------------------------------------------- reporting
results = []
def rec(code, status, msg):
    results.append((code, status, msg))
    print(f'[{status}] {code}: {msg}')

def min_tests(features, workflows, transitions, nfrs):
    return 3 * features + workflows + transitions + nfrs

# ---------------------------------------------------------------- checks
def check_bm01(path, members):
    text = open(path, encoding='utf-8').read()
    secs = split_sections(text)
    # split main (0-8) and appendix
    main_text = text
    idx = re.search(r'^#{1,2}\s+Appendix A', text, re.I | re.M)
    if idx: main_text = text[:idx.start()]
    wc = words(main_text)
    if wc > 1300: rec('X2', 'FAIL', f'BM01 sections 0-8 have ~{wc} words (> 1300): likely over 4 pages (estimate)')
    elif wc > 1100: rec('X2', 'WARN', f'BM01 sections 0-8 have ~{wc} words (> 1100): close to the 4-page limit (estimate)')
    else: rec('X2', 'PASS', f'BM01 sections 0-8 have ~{wc} words (estimate; render to PDF to confirm)')

    s2 = find_section(secs, r'^2\.\s*System at a Glance')
    if s2 is not None:
        n = words(re.sub(r'<!--.*?-->', '', s2, flags=re.S))
        rec('X3', 'PASS' if n <= 150 else 'FAIL', f'section 2 has {n} words (max 150)')
    for pat, label, exact in [(r'^3\.\s*Key Design Decisions', 'section 3 decisions', 5), (r'^4\.\s*Top Risks', 'section 4 risks', 3)]:
        b = find_section(secs, pat)
        if b is None: rec('X3', 'FAIL', f'{label}: heading not found'); continue
        t = tables(b); rows = data_rows(t[0][1]) if t else []
        rec('X3', 'PASS' if len(rows) == exact else 'FAIL', f'{label}: {len(rows)} rows (exactly {exact})')
        if label.startswith('section 3') and t:
            hdr = [h.lower() for h in t[0][0]]
            oi = next((i for i, h in enumerate(hdr) if h.startswith('owner')), None)
            if oi is not None:
                is_ph = lambda v: not v.strip() or bool(re.search(r'\[(?:Cần bổ sung|Needs input|Inferred from code)\b', v, re.I))
                empty = [r[0] for r in rows if oi >= len(r) or is_ph(r[oi])]
                rec('X3', 'PASS' if not empty else 'FAIL', f'section 3 owners present' if not empty else f'section 3 rows without owner: {empty}')
    b7 = find_section(secs, r'^7\.\s*Non-Functional')
    if b7 is not None:
        t = tables(b7); rows = data_rows(t[0][1]) if t else []
        rec('X3', 'PASS' if len(rows) <= 6 else 'FAIL', f'section 7: {len(rows)} NFR rows (max 6)')
    b8 = find_section(secs, r'^8\.\s*Ownership')
    if b8 is not None:
        t = tables(b8); rows = data_rows(t[0][1]) if t else []
        if members: rec('X4', 'PASS' if len(rows) == members else 'FAIL', f'section 8: {len(rows)} rows for {members} members')
    a1 = find_section(secs, r'A1\.?\s*Main Workflows')
    wf_count = None
    if a1 is not None:
        t = tables(a1); rows = data_rows(t[0][1]) if t else []
        wf_count = len(rows)
        if members: rec('X5', 'PASS' if wf_count >= members else 'FAIL', f'A1: {wf_count} workflows for {members} members (min = members)')
        hdr = [h.lower() for h in t[0][0]] if t else []
        if 'owner' in hdr:
            is_ph = lambda v: not v.strip() or bool(re.search(r'\[(?:Cần bổ sung|Needs input|Inferred from code)\b', v, re.I))
            oi = hdr.index('owner'); owners = [r[oi].strip() for r in rows if oi < len(r)]
            real_owners = [o for o in owners if not is_ph(o)]
            rec('X5', 'PASS' if len(real_owners) == len(rows) and rows else 'FAIL', 'every workflow has one owner' if len(real_owners) == len(rows) and rows else 'workflow without owner')
            if members:
                rec('X5', 'PASS' if len(set(real_owners)) >= members else 'WARN',
                    f'{len(set(real_owners))} distinct owners for {members} members (each member should own >= 1)')
    a3 = find_section(secs, r'A3\.?\s*Functional Test Case')
    if a3 is not None:
        t = tables(a3)
        if t:
            sub = {r[0].lower(): num(r[3]) if len(r) > 3 else None for r in t[0][1] if r}
            cnt = {r[0].lower(): num(r[1]) if len(r) > 1 else None for r in t[0][1] if r}
            def g(prefix, d):
                return next((v for k, v in d.items() if k.startswith(prefix)), None)
            f, w, tr, n = (g('mandatory', cnt), g('main workflows', cnt), g('state', cnt), g('agreed', cnt))
            tot = g('committed total', sub)
            if None not in (f, w, tr, n):
                need = min_tests(int(f), int(w), int(tr), int(n))
                rec('X7', 'PASS' if tot is not None and tot >= need else 'FAIL',
                    f'A3 minimum = 3x{int(f)} + {int(w)} + {int(tr)} + {int(n)} = {need}; committed total {int(tot) if tot is not None else None}')
            else:
                rec('X7', 'WARN', 'A3 counts incomplete; cannot compute the minimum')
    # A2 demo scenarios per workflow
    a2 = find_section(secs, r'A2\.?\s*Demo Scenarios')
    if a2 is not None and wf_count:
        t = tables(a2); rows = data_rows(t[0][1]) if t else []
        hdr = [h.lower() for h in t[0][0]] if t else []
        if 'type' in hdr and 'workflow' in hdr:
            ti, wi = hdr.index('type'), hdr.index('workflow'); by = {}
            for r in rows:
                if wi < len(r) and ti < len(r):
                    by.setdefault(r[wi].strip(), set()).add(r[ti].strip().lower())
            bad = [w for w, ty in by.items() if not ({'main'} <= ty and any(x.startswith('exc') for x in ty))]
            rec('X6', 'PASS' if not bad and len(by) >= wf_count else 'FAIL',
                f'demo scenarios cover {len(by)}/{wf_count} workflows; missing main or exception: {bad or "none"}')
    return secs

def check_bm02(path, bm01_text):
    text = open(path, encoding='utf-8').read(); secs = split_sections(text)
    b3 = find_section(secs, r'^3\.\s*Findings'); b5 = find_section(secs, r'^5\.\s*Summary')
    if b3 is None: rec('X1', 'FAIL', 'BM02 section 3 not found'); return
    t = tables(b3)
    if not t: rec('X1', 'FAIL', 'BM02 section 3 has no table'); return
    hdr = [h.lower() for h in t[0][0]]; rows = data_rows(t[0][1])
    si = hdr.index('severity') if 'severity' in hdr else None
    ri = next((i for i, h in enumerate(hdr) if h.startswith('team response')), None)
    if si is None or ri is None:
        rec('X1', 'FAIL', 'BM02 section 3 table missing Severity or Team response column'); return
    is_ph = lambda v: not v.strip() or bool(re.search(r'\[(?:Cần bổ sung|Needs input|Inferred from code)\b', v, re.I))
    no_resp = [r[0] for r in rows if is_ph(r[ri])]
    rec('X13', 'PASS' if not no_resp else 'FAIL', 'every finding has a Team response' if not no_resp else f'findings without Team response: {no_resp}')
    need = [r[0] for r in rows if r[si].strip().lower() == 'high' and re.match(r'(kept|planned)', r[ri].strip(), re.I)]
    bm01 = split_sections(bm01_text); s5 = find_section(bm01, r'^5\.\s*Known Gaps') or ''
    missing = [i for i in need if i not in s5]
    rec('X1', 'PASS' if not missing else 'FAIL',
        f'High + Kept/Planned findings: {need or "none"}; missing from BM01 section 5: {missing or "none"}')
    if b5:
        st = tables(b5)
        if st:
            for r in st[0][1]:
                if not r or not r[0].strip(): continue
                sev = r[0].strip().lower(); vals = [num(c) for c in r[1:5]] + [None] * 4
                counted = {k: sum(1 for x in rows if x[si].strip().lower() == sev and re.match(k, x[ri].strip(), re.I)) for k in ('fixed', 'kept', 'planned')}
                total = sum(1 for x in rows if x[si].strip().lower() == sev)
                ok = vals[0] is not None and int(vals[0]) == total and [int(v or 0) for v in vals[1:4]] == [counted['fixed'], counted['kept'], counted['planned']]
                rec('X13', 'PASS' if ok else 'FAIL', f'summary {r[0]}: table says {vals[:4]}, rows give total {total}, {counted}')

def check_bm04(path):
    text = open(path, encoding='utf-8').read(); secs = split_sections(text)
    def total_row(rows):
        return next((r for r in rows if r and r[0].strip().lower() == 'total'), None)
    b81 = find_section(secs, r'^8\.1'); b82 = find_section(secs, r'^8\.2'); b83 = find_section(secs, r'^8\.3'); b84 = find_section(secs, r'^8\.4')
    if None in (b81, b82, b83):
        rec('X9', 'FAIL', 'BM04 sections 8.1-8.3 not all found'); return
    ts81, ts82, ts83 = tables(b81), tables(b82), tables(b83)
    if not (ts81 and ts82 and ts83):
        rec('X9', 'FAIL', 'BM04 sections 8.1-8.3 missing tables'); return
    t81, t82, t83 = ts81[0], ts82[0], ts83[0]
    r81, r82 = total_row(t81[1]), total_row(t82[1])
    h81 = [h.lower() for h in t81[0]]; h82 = [h.lower() for h in t82[0]]
    c83 = {r[0].lower(): r[1] for r in t83[1] if len(r) > 1}
    def g(prefix):
        return next((v for k, v in c83.items() if k.startswith(prefix)), '')
    wf, demos, tcs, auto = g('number of main workflows'), g('number of demo'), g('committed functional'), g('of which automated')
    def col(h, r, name):
        i = next((k for k, x in enumerate(h) if x.startswith(name)), None); return r[i] if (i is not None and r and i < len(r)) else ''
    for label, (a, b, c) in {
        'test cases': (col(h81, r81, 'test cases'), col(h82, r82, 'test cases'), tcs),
        'automated': (col(h81, r81, 'automated'), col(h82, r82, 'automated'), auto)}.items():
        va, vb, vc = num(a), num(b), num(c)
        ok = va is not None and va == vb == vc
        rec('X9', 'PASS' if ok else 'FAIL', f'{label}: 8.1 total={a!r}, 8.2 total={b!r}, 8.3={c!r}')
    da, db, dc = pair(col(h81, r81, 'demo')), pair(col(h82, r82, 'demo')), pair(demos)
    sums = [sum(x) if x else None for x in (da, db, dc)]
    ok_pair = da is not None and da == dc
    ok = ok_pair and sums[0] == sums[1] == sums[2]
    rec('X9', 'PASS' if ok else 'FAIL', f'demo scenarios: 8.1 (main, exception)={da}, 8.2 total={sums[1]}, 8.3 (main, exception)={dc}')
    nwf = len(data_rows([r for r in t81[1] if r and r[0].strip().lower() != 'total']))
    rec('X9', 'PASS' if num(wf) == nwf else 'FAIL', f'workflows: 8.1 has {nwf} rows, 8.3 says {wf!r}')
    # X7 / automation share
    tc, au = num(tcs), num(auto)
    if tc is not None and au is not None:
        need = math.ceil(tc * 0.5)
        rec('X7', 'PASS' if au >= need else 'FAIL', f'automated {int(au)} of {int(tc)} (need >= {need}, 50% rounded up)')
    if b84:
        t = tables(b84)
        if t:
            hdr = [h.lower() for h in t[0][0]]; ai = next((i for i, h in enumerate(hdr) if h.startswith('agreed')), None)
            if ai is not None:
                is_ph = lambda v: not v.strip() or bool(re.search(r'\[(?:Cần bổ sung|Needs input|Inferred from code)\b', v, re.I))
                empty = [r[0] for r in t[0][1] if r and ai < len(r) and is_ph(r[ai])]
                rec('X10', 'PASS' if not empty else 'WARN', 'agreed thresholds filled (verify they are not below the minimums)' if not empty else f'agreed threshold empty for: {empty}')

# ---------------------------------------------------------------- main
def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'formula':
        ap = argparse.ArgumentParser(); ap.add_argument('formula')
        for k in ('features', 'workflows', 'transitions', 'nfrs'): ap.add_argument('--' + k, type=int, required=True)
        ap.add_argument('--committed', type=int)
        a = ap.parse_args()
        need = min_tests(a.features, a.workflows, a.transitions, a.nfrs)
        print(f'minimum = 3x{a.features} + {a.workflows} + {a.transitions} + {a.nfrs} = {need}; automated >= {math.ceil(need * 0.5)} at the minimum')
        if a.committed is not None:
            ok = a.committed >= need
            print(f'committed {a.committed} -> {"OK" if ok else "BELOW MINIMUM"}; automated needed >= {math.ceil(a.committed * 0.5)}')
            sys.exit(0 if ok else 1)
        return
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--bm01'); ap.add_argument('--bm02'); ap.add_argument('--bm04'); ap.add_argument('--members', type=int)
    a = ap.parse_args()
    if not (a.bm01 or a.bm02 or a.bm04): ap.error('give at least one of --bm01 --bm02 --bm04')
    if a.bm01: check_bm01(a.bm01, a.members)
    if a.bm02:
        if not a.bm01: rec('X1', 'WARN', 'BM01 not given; cannot check Known Gaps')
        else: check_bm02(a.bm02, open(a.bm01, encoding='utf-8').read())
    if a.bm04: check_bm04(a.bm04)
    fails = sum(1 for _, s, _ in results if s == 'FAIL')
    print(f'\nSummary: {sum(1 for _,s,_ in results if s=="PASS")} pass, {sum(1 for _,s,_ in results if s=="WARN")} warn, {fails} fail')
    sys.exit(1 if fails else 0)

if __name__ == '__main__':
    main()
