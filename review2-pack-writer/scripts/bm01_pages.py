#!/usr/bin/env python3
"""Measure how many A4 pages BM01 sections 0-8 occupy (Appendix A excluded).

Usage: python bm01_pages.py BM01.pdf
       python bm01_pages.py BM01.docx     (needs LibreOffice 'soffice' on PATH to convert)

Needs the 'pypdf' package for PDFs. If a tool is missing the script says so and exits 2;
it never guesses a page count.
Rule being checked: sections 0-8 <= 4 pages (font 11, margins 2 cm).
"""
import os, re, shutil, subprocess, sys, tempfile

def to_pdf(path):
    if path.lower().endswith('.pdf'):
        return path
    soffice = shutil.which('soffice') or shutil.which('libreoffice')
    if not soffice:
        print('CANNOT MEASURE: LibreOffice (soffice) not found; export the .docx to PDF and pass the PDF.')
        sys.exit(2)
    out = tempfile.mkdtemp()
    subprocess.run([soffice, '--headless', '--convert-to', 'pdf', '--outdir', out, path], check=True, capture_output=True)
    return os.path.join(out, os.path.splitext(os.path.basename(path))[0] + '.pdf')

def main():
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    try:
        from pypdf import PdfReader
    except ImportError:
        print('CANNOT MEASURE: install pypdf (pip install pypdf).'); sys.exit(2)
    pdf = to_pdf(sys.argv[1])
    r = PdfReader(pdf); total = len(r.pages)
    start = None; before = 0
    for i, p in enumerate(r.pages):
        txt = p.extract_text() or ''
        m = re.search(r'Appendix\s+A\s*[-–—]?\s*Defense', txt, re.I) or re.search(r'Appendix\s+A\b', txt, re.I)
        if m:
            start, before = i + 1, len(txt[:m.start()].strip()); break
    if start is None:
        main_pages = total
        print(f'Appendix A heading not found; counting all {total} pages as sections 0-8.')
    else:
        main_pages = (start - 1) + (1 if before > 80 else 0)
        print(f'Appendix A starts on page {start} ({before} characters of earlier content on that page).')
    ok = main_pages <= 4
    print(f'Sections 0-8 occupy {main_pages} page(s): {"PASS" if ok else "FAIL"} (limit 4 A4 pages).')
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
