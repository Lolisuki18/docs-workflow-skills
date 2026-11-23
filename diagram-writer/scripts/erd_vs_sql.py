#!/usr/bin/env python3
"""Compare a Mermaid erDiagram with CREATE TABLE statements in a SQL script, both directions.

Usage: python erd_vs_sql.py schema.sql erd.md [--ignore-case]

Reads: SQL files (CREATE TABLE ... with inline or table-level PRIMARY KEY / FOREIGN KEY / REFERENCES)
and a Markdown/Mermaid file containing an `erDiagram` block with attribute lists
(`entity { type name PK|FK|UK }`, one attribute per line).
Reports: tables only in SQL, tables only in the diagram, columns missing on either side and PK/FK
flag differences. Exit code 1 when any difference is found. It is a syntax-level check: it does not
understand dialect-specific DDL (ALTER TABLE ADD COLUMN, partitions, generated columns); list those
manually. Migrations spread over many files: pass one file at a time or concatenate them first.
"""
import re, sys

def strip_sql_comments(s):
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    return re.sub(r'--[^\n]*', '', s)

def split_top(body):
    parts, depth, cur = [], 0, ''
    for ch in body:
        if ch == '(': depth += 1
        elif ch == ')': depth -= 1
        if ch == ',' and depth == 0: parts.append(cur.strip()); cur = ''
        else: cur += ch
    if cur.strip(): parts.append(cur.strip())
    return parts

def ident(x): return x.strip().strip('`"[]').split('.')[-1].strip('`"[]')

def parse_sql(text):
    text = strip_sql_comments(text); tables = {}
    for m in re.finditer(r'create\s+table\s+(?:if\s+not\s+exists\s+)?([^\s(]+)\s*\(', text, re.I):
        name = ident(m.group(1)); i = m.end(); depth = 1
        while i < len(text) and depth:
            depth += {'(': 1, ')': -1}.get(text[i], 0); i += 1
        cols = {}
        for part in split_top(text[m.end():i - 1]):
            low = part.lower()
            pk = re.match(r'(?:constraint\s+\S+\s+)?primary\s+key\s*\(([^)]*)\)', low)
            fk = re.match(r'(?:constraint\s+\S+\s+)?foreign\s+key\s*\(([^)]*)\)', low)
            if pk:
                for c in pk.group(1).split(','): cols.setdefault(ident(c), {'pk': False, 'fk': False})['pk'] = True
            elif fk:
                for c in fk.group(1).split(','): cols.setdefault(ident(c), {'pk': False, 'fk': False})['fk'] = True
            elif re.match(r'(constraint|unique|key|index|check|fulltext)\b', low):
                continue
            else:
                cname = ident(part.split()[0])
                cols.setdefault(cname, {'pk': False, 'fk': False})
                if 'primary key' in low: cols[cname]['pk'] = True
                if ' references ' in low: cols[cname]['fk'] = True
        tables[name] = cols
    return tables

def parse_mermaid(text):
    mm = re.search(r'erDiagram(.*?)(?:```|\Z)', text, re.S)
    body = mm.group(1) if mm else text
    ents = {}
    for m in re.finditer(r'^\s*([A-Za-z_][\w]*)\s*\{([^}]*)\}', body, re.M | re.S):
        cols = {}
        for line in m.group(2).splitlines():
            toks = line.split()
            if len(toks) < 2: continue
            flags = {t.upper().strip(',') for t in toks[2:]}
            cols[toks[1]] = {'pk': 'PK' in flags, 'fk': 'FK' in flags}
        ents[m.group(1)] = cols
    for m in re.finditer(r'^\s*([A-Za-z_]\w*)\s+[|}o][|o]--[|o][|{o]\s+([A-Za-z_]\w*)', body, re.M):
        ents.setdefault(m.group(1), {}); ents.setdefault(m.group(2), {})
    return ents

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 2:
        print(__doc__); sys.exit(2)
    ic = '--ignore-case' in sys.argv
    sql = parse_sql(open(args[0], encoding='utf-8').read())
    erd = parse_mermaid(open(args[1], encoding='utf-8').read())
    k = (lambda s: s.lower()) if ic else (lambda s: s)
    sq = {k(t): (t, c) for t, c in sql.items()}; er = {k(t): (t, c) for t, c in erd.items()}
    problems = []
    for t in sorted(set(sq) - set(er)): problems.append(f'table in SQL but not in ERD: {sq[t][0]}')
    for t in sorted(set(er) - set(sq)): problems.append(f'entity in ERD but not in SQL: {er[t][0]}')
    for t in sorted(set(sq) & set(er)):
        sc, ec = {k(c): (c, v) for c, v in sq[t][1].items()}, {k(c): (c, v) for c, v in er[t][1].items()}
        if not ec:
            problems.append(f'{sq[t][0]}: ERD lists no attributes (only relationships); columns not compared'); continue
        for c in sorted(set(sc) - set(ec)): problems.append(f'{sq[t][0]}.{sc[c][0]}: column in SQL, missing in ERD')
        for c in sorted(set(ec) - set(sc)): problems.append(f'{sq[t][0]}.{ec[c][0]}: attribute in ERD, missing in SQL')
        for c in sorted(set(sc) & set(ec)):
            for flag in ('pk', 'fk'):
                if sc[c][1][flag] != ec[c][1][flag]:
                    problems.append(f'{sq[t][0]}.{sc[c][0]}: {flag.upper()} differs (SQL={sc[c][1][flag]}, ERD={ec[c][1][flag]})')
    print(f'SQL tables: {len(sql)}; ERD entities: {len(erd)}')
    for p in problems: print(' -', p)
    print('RESULT:', 'MATCH' if not problems else f'{len(problems)} difference(s)')
    sys.exit(0 if not problems else 1)

if __name__ == '__main__':
    main()
