#!/usr/bin/env python3
"""Render the student notes (notes/**/*.notes.md) to UA-styled PDFs for D2L.

Each note file carries its own YAML (title, module, reading_time_min). That
front matter is replaced at build time with the course Typst format, and the
module line becomes the subtitle, so the PDFs match the rest of the course
documents (US Letter, Arial, navy headings).

Output: out/notes-<stem>.pdf, where <stem> matches the deck and d2l page name
(m1a-setup-and-model, ...), so slides, notes, and lecture pages sort together.

    python build-notes-pdfs.py    # from the repo root

Requires: quarto (bundles Typst), pdftotext (Poppler).
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "notes"
OUT = ROOT / "d2l" / "pdf"


def frontmatter(title, subtitle):
    return f"""---
title: "{title}"
subtitle: "{subtitle}"
format:
  typst:
    papersize: us-letter
    margin:
      x: 1.1in
      y: 1in
    fontsize: 10.5pt
    section-numbering: ""
    mainfont: Arial
    include-in-header:
      - text: |
          #show heading.where(level: 1): set text(fill: rgb("#1B4F72"))
          #show heading.where(level: 2): set text(fill: rgb("#1B4F72"))
          #show heading.where(level: 3): set text(fill: rgb("#205a80"))
          #show link: set text(fill: rgb("#AB0520"))
---
"""


def parse(md):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", md, re.S)
    meta = dict(re.findall(r'^(\w+):\s*"?([^"\n]*)"?\s*$', m.group(1), re.M))
    return meta, m.group(2)


def main():
    OUT.mkdir(exist_ok=True)
    files = sorted(SRC.rglob("*.notes.md"))
    if not files:
        sys.exit("no notes found")
    print(f"Building {len(files)} note PDFs:")
    built = []
    for f in files:
        meta, body = parse(f.read_text(encoding="utf-8"))
        stem = f.name.replace(".notes.md", "")
        sub = (f"INFO 521 · student notes · {meta.get('module', '')}"
               + (f" · ~{meta['reading_time_min']} min read" if meta.get("reading_time_min") else ""))
        # the body repeats the H1 title; the Typst title block already carries it
        body = re.sub(r"^# .*\n", "", body.lstrip(), count=1)
        qmd = ROOT / f"_{stem}.qmd"
        qmd.write_text(frontmatter(meta.get("title", stem), sub) + "\n" + body,
                       encoding="utf-8")
        r = subprocess.run(["quarto", "render", str(qmd), "--to", "typst"],
                           capture_output=True, text=True, cwd=ROOT)
        produced = ROOT / f"_{stem}.pdf"
        qmd.unlink(missing_ok=True)
        if r.returncode != 0 or not produced.exists():
            print(f"  FAIL {stem}\n{r.stdout[-800:]}{r.stderr[-800:]}")
            continue
        dest = OUT / f"notes-{stem}.pdf"
        shutil.move(str(produced), str(dest))
        built.append(dest)
        print(f"  {dest.name}")

    if len(built) != len(files):
        sys.exit(1)

    print("\nChecks:")
    bad = 0
    for p in built:
        txt = subprocess.run(["pdftotext", str(p), "-"],
                             capture_output=True, text=True).stdout
        problems = []
        if "student notes" not in txt:
            problems.append("no subtitle band")
        for term in ("closed-book", "unaided", "P1-M1", "GitHub Classroom"):
            if term in txt:
                problems.append(f"stale {term!r}")
        if len(txt.split()) < 200:
            problems.append("suspiciously short")
        if problems:
            print(f"  FAIL  {p.name}: {'; '.join(problems)}")
            bad += 1
        else:
            print(f"  clean {p.name}")
    if bad:
        sys.exit(1)
    print(f"\nAll {len(built)} note PDFs built and checked.")


if __name__ == "__main__":
    main()
