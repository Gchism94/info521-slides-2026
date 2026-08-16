#!/usr/bin/env python3
"""Generate the seven module overview decks from `module_spec.py`.

Writes `modules/<dir>/m<N>-overview.qmd`. These files are GENERATED. Edit
`module_spec.py` and re-run this, or your change will be overwritten and, worse,
will desynchronise the recording script built from the same spec.

The decks carry no Python cells and no figures, so they render fast and do not
touch the freeze cache the lecture decks depend on.

    python overviews/build_decks.py

Rendering to HTML and PDF is the repo's normal path: `quarto render` picks them
up through the `modules/**/*.qmd` glob, then `mkpdf.py` prints every deck in
docs/ to PDF.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from module_spec import MODULES

ROOT = Path(__file__).resolve().parent.parent

# A YAML comment, not an HTML one. Content placed between the front matter and
# the first `##` becomes reveal's second slide, and an HTML comment there gives
# you a silent blank slide in the middle of the deck.
GENERATED = (
    "# GENERATED FILE. Source: overviews/module_spec.py.\n"
    "# Run `python overviews/build_decks.py` after editing the spec.\n"
    "# Hand edits here are lost on the next build and will desynchronise the\n"
    "# recording script, which is generated from the same spec.\n"
)


def frontmatter(m):
    sub = f"INFO 521 · Module {m['n']} · Overview"
    if m["n"] == 7:
        sub += " and Course Wrap-Up"
    return (
        "---\n"
        f'title: "Module {m["n"]}: {m["title"]}"\n'
        f'subtitle: "{sub}"\n'
        'author: "Greg Chism"\n'
        'institute: "College of Information Science · University of Arizona"\n'
        "date: last-modified\n"
        'date-format: "MMMM YYYY"\n'
        + GENERATED +
        "---\n"
    )


def slides(m):
    """Return [(slide_id, heading, markdown_body)] in deck order."""
    out = []

    out.append(("question", "The question", (
        f"### {m['question']}\n\n{m['question_gloss']}\n"
    )))

    body = "\n".join(f"**{name}**\n\n: {desc}\n" for name, desc in m["lectures"])
    out.append(("lectures", "What the lectures do", body))

    out.append(("sits", "Where this sits", m["sits"] + "\n"))

    body = "\n".join(f"- {w}" for w in m["work"])
    out.append(("work", f"{m['week']} at a glance", body + "\n"))

    body = "\n".join(f"**{head}** {text}\n" for head, text in m["watch"])
    out.append(("watch", "Watch out for", body))

    if "wrapup" in m:
        w = m["wrapup"]
        rows = "\n".join(f"| {where} | {what} |" for where, what in w["arc"])
        out.append(("arc", "The course, in one arc",
                    "| | |\n|---|---|\n" + rows + f"\n\n{w['arc_close']}\n"))
        outcomes = "\n".join(f"- **{k}.** {v}" for k, v in
                             __import__("module_spec").CLOS)
        out.append(("learned", "What you can do now",
                    w["learned"] + "\n\n::: {.smaller}\n" + outcomes + "\n:::\n"))
        body = "\n".join(f"- {item}" for item in w["left"])
        out.append(("left", "What is left", body + "\n"))
        out.append(("next", "Where next", w["next"] + "\n"))

    return out


# Slides whose body is a list or a table need the smaller type to fit; the
# short prose slides look starved in it.
DENSE = {"lectures", "work", "watch", "arc", "learned", "left"}


def build(m):
    parts = [frontmatter(m)]
    for sid, heading, body in slides(m):
        cls = " {.smaller}" if sid in DENSE else ""
        parts.append(f"\n## {heading}{cls}\n\n{body}")
    dest = ROOT / "modules" / m["dir"] / f"m{m['n']}-overview.qmd"
    dest.write_text("\n".join(parts), encoding="utf-8")
    return dest


def main():
    print("Generating module overview decks:")
    made = []
    for m in MODULES:
        d = build(m)
        n_slides = len(slides(m))
        made.append(d)
        print(f"  {d.relative_to(ROOT)}  ({n_slides} content slides)")

    print("\nChecks:")
    bad = 0
    for m, d in zip(MODULES, made):
        text = d.read_text(encoding="utf-8")
        problems = []
        n = text.count("\n## ")
        expected = len(slides(m))
        if n != expected:
            problems.append(f"{n} slides, expected {expected}")
        if "GENERATED FILE" not in text:
            problems.append("missing generated-file banner")
        if "College of Information Science" not in text:
            problems.append("wrong affiliation")
        for ch in ("—", "–"):
            if ch in text:
                problems.append("dash character in slide text")
                break
        if "{python}" in text:
            problems.append("unexpected code cell")
        # the self-guided capstone was retired as a project scope; the project
        # is one path now, and these overviews must not offer a choice
        for term in ("capstone", "both scopes", "structured scope", "project scope"):
            if term in text.lower():
                problems.append(f"retired scope language {term!r}")
        if problems:
            print(f"  FAIL  {d.name}: {'; '.join(problems)}")
            bad += 1
        else:
            print(f"  clean {d.name}")
    if bad:
        sys.exit(1)
    print(f"\n{len(made)} decks generated. Run `quarto render` then `mkpdf.py`.")


if __name__ == "__main__":
    main()
