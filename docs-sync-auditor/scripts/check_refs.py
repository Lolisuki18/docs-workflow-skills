#!/usr/bin/env python3
"""Verify relative Markdown links and backticked `path:line` refs inside docs/.

Usage: python scripts/check_refs.py <docs_dir> [repo_root]
Exit code 1 when any broken link or out-of-range file:line reference is found.
"""
import os, re, sys
from pathlib import Path

LINK_RE = re.compile(r'\[[^\]]+\]\((?!https?://|mailto:|#)([^)#\s]+)(?:#[^)]*)?\)')
FILE_LINE_RE = re.compile(r'`([A-Za-z0-9_./\-]+\.[A-Za-z0-9]+):(\d+)(?:-\d+)?`')


def check_docs(docs_dir: Path, repo_root: Path) -> list[str]:
    errors: list[str] = []
    for md in sorted(docs_dir.rglob('*.md')):
        text = md.read_text(encoding='utf-8')
        for m in LINK_RE.finditer(text):
            rel = m.group(1)
            if not (md.parent / rel).exists():
                errors.append(f'{md}: broken link -> {rel}')
        for m in FILE_LINE_RE.finditer(text):
            ref, line_no = m.group(1), int(m.group(2))
            target = (repo_root / ref) if (repo_root / ref).exists() else (md.parent / ref)
            if not target.is_file():
                errors.append(f'{md}: missing file ref -> {ref}:{line_no}')
            else:
                lines = len(target.read_text(encoding='utf-8', errors='replace').splitlines())
                if line_no < 1 or line_no > lines:
                    errors.append(f'{md}: line {line_no} out of range (1..{lines}) in {ref}')
    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__.strip())
        return 2
    docs_dir = Path(sys.argv[1]).resolve()
    repo_root = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else docs_dir.parent
    errs = check_docs(docs_dir, repo_root)
    for e in errs:
        print('FAIL', e)
    print(f'checked {docs_dir}: {len(errs)} error(s).')
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
