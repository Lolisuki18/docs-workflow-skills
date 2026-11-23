#!/usr/bin/env python3
"""Compare a Mermaid erDiagram with the tables defined in a SQL script, both directions.

Usage: python erd_vs_sql.py schema.sql erd.md [--ignore-case]
       (on Windows without a working `python` alias use: py erd_vs_sql.py ...)

Reads SQL: CREATE [TEMP|UNLOGGED] TABLE [IF NOT EXISTS] with schema prefixes (public.users),
quoted names ("users", `users`, [users]), inline or table-level PRIMARY KEY (composite included),
FOREIGN KEY / REFERENCES, types with parentheses or quoted lists (numeric(10,2), ENUM('a','b'),
UUID, arrays), and simple ALTER TABLE statements: ADD [COLUMN], ADD ... PRIMARY KEY,
ADD ... FOREIGN KEY, DROP COLUMN. Migrations spread over several files: concatenate them in order.
Reads the diagram: an `erDiagram` block with `entity { type name PK|FK|UK }` (one attribute per line;
quoted entity names allowed) and relationship lines.
Reports tables only in SQL / only in the diagram, columns missing on either side and PK/FK flag
differences; exit code 1 on any difference.
Not supported (report manually): RENAME, dialect-specific generated columns, partitions, views,
CREATE TYPE (it is not a table), tables created by dynamic SQL or an ORM at runtime.
"""
import re, sys

IDENT = r'(?:"[^"]+"|`[^`]+`|\[[^\]]+\]|[\w$]+)'
QNAME = rf'{IDENT}(?:\s*\.\s*{IDENT})*'

def strip_sql_comments(s):
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    return re.sub(r'--[^\n]*', '', s)

def ident(x):
    x = x.strip()
    parts = re.findall(IDENT, x)
    last = parts[-1] if parts else x
    return last.strip('`"[]')

def split_top(body):
    """Split on commas at depth 0, ignoring commas inside parentheses and quotes."""
    parts, depth, cur, q = [], 0, '', None
    for ch in body:
        if q:
            cur += ch
            if ch == q: q = None
            continue
        if ch in ('"', "'", '`'): q = ch; cur += ch; continue
        if ch == '(': depth += 1
        elif ch == ')': depth -= 1
        if ch == ',' and depth == 0: parts.append(cur.strip()); cur = ''
        else: cur += ch
    if cur.strip(): parts.append(cur.strip())
    return parts

def cols_of(lst):
    return [ident(c) for c in split_top(lst)]

def col(cols, name):
    return cols.setdefault(name, {'pk': False, 'fk': False})

def parse_sql(text):
    text = strip_sql_comments(text); tables = {}
    for m in re.finditer(rf'create\s+(?:(?:global\s+|local\s+)?(?:temporary|temp)\s+|unlogged\s+)?table\s+(?:if\s+not\s+exists\s+)?({QNAME})\s*\(', text, re.I):
        name = ident(m.group(1)); i = m.end(); depth = 1; q = None
        while i < len(text) and depth:
            ch = text[i]
            if q:
                if ch == q: q = None
            elif ch in ('"', "'", '`'): q = ch
            else: depth += {'(': 1, ')': -1}.get(ch, 0)
            i += 1
        cols = tables.setdefault(name, {})
        for part in split_top(text[m.end():i - 1]):
            low = part.lower().strip()
            pk = re.match(r'(?:constraint\s+\S+\s+)?primary\s+key\s*\(([^)]*)\)', low)
            fk = re.match(r'(?:constraint\s+\S+\s+)?foreign\s+key\s*\(([^)]*)\)', low)
            if pk:
                for c in cols_of(re.search(r'\(([^)]*)\)', part).group(1)): col(cols, c)['pk'] = True
            elif fk:
                for c in cols_of(re.search(r'\(([^)]*)\)', part).group(1)): col(cols, c)['fk'] = True
            elif re.match(r'(constraint|unique|key|index|check|fulltext|exclude|like)\b', low):
                continue
            else:
                first = re.match(IDENT, part.strip())
                if not first: continue
                c = col(cols, ident(first.group(0)))
                if 'primary key' in low: c['pk'] = True
                if re.search(r'\breferences\b', low): c['fk'] = True
    # ALTER TABLE support
    for m in re.finditer(rf'alter\s+table\s+(?:only\s+)?(?:if\s+exists\s+)?({QNAME})\s+(.*?);', text, re.I | re.S):
        t = ident(m.group(1)); cols = tables.get(t)
        if cols is None: continue
        for act in split_top(m.group(2)):
            a = act.strip(); low = a.lower()
            add_col = re.match(rf'add\s+(?:column\s+)?(?:if\s+not\s+exists\s+)?({IDENT})\s+\S', a, re.I)
            if re.match(r'add\s+(?:constraint\s+\S+\s+)?primary\s+key', low):
                for c in cols_of(re.search(r'\(([^)]*)\)', a).group(1)): col(cols, c)['pk'] = True
            elif re.match(r'add\s+(?:constraint\s+\S+\s+)?foreign\s+key', low):
                for c in cols_of(re.search(r'\(([^)]*)\)', a).group(1)): col(cols, c)['fk'] = True
            elif re.match(r'add\s+(constraint|unique|index|check|key)\b', low):
                continue
            elif add_col:
                c = col(cols, ident(add_col.group(1)))
                if 'primary key' in low: c['pk'] = True
                if re.search(r'\breferences\b', low): c['fk'] = True
            else:
                d = re.match(rf'drop\s+(?:column\s+)?(?:if\s+exists\s+)?({IDENT})', a, re.I)
                if d and not low.startswith('drop constraint'): cols.pop(ident(d.group(1)), None)
    return tables

def parse_mermaid(text):
    mm = re.search(r'erDiagram(.*?)(?:```|\Z)', text, re.S)
    body = mm.group(1) if mm else text
    ents = {}
    for m in re.finditer(r'^\s*("[^"]+"|[A-Za-z_][\w-]*)\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}', body, re.M | re.S):
        cols = {}
        for line in m.group(2).splitlines():
            line = re.sub(r'"[^"]*"', '', line).strip()
            toks = line.split()
            if len(toks) < 2: continue
            flags = {t.upper().strip(',') for t in toks[2:]}
            cols[toks[1].strip('"')] = {'pk': 'PK' in flags, 'fk': 'FK' in flags}
        ents[m.group(1).strip('"')] = cols
    for m in re.finditer(r'^\s*("[^"]+"|[A-Za-z_][\w-]*)\s+[|}o][|o]\s*[-.]+\s*[|o][|{o]\s+("[^"]+"|[A-Za-z_][\w-]*)', body, re.M):
        ents.setdefault(m.group(1).strip('"'), {}); ents.setdefault(m.group(2).strip('"'), {})
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
