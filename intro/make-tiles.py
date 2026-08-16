"""Generate the non-photographic tile(s) used by intro/gc-intro.qmd.

Run from the project root:

    python intro/make-tiles.py

The "Data science" stage of the "How I got here" slide has no photograph (the
multi-panel figure from Greg's original personal deck is not present in
GCIntroduction_extended.pptx). This script draws an illustrative tile instead,
in the course's own visual language, so the four stages of that slide all carry
a graphic.

Deliberately illustrative, not a result: it shows a fitted line with an
uncertainty band, which is the idea the whole course is built around. Swap in a
real figure whenever one is available.

Conventions match shared/slide_helpers.py: Okabe-Ito hues, transparent
facecolor so one asset sits on both the dark and light themes, and neutral
#7a7a7a chrome that clears contrast on either background.
"""
from __future__ import annotations

import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, "shared")
import slide_helpers as sh  # noqa: E402

OUT = os.path.join("intro", "img", "data-science.png")


def main() -> None:
    sh.use_slide_style()
    OK = sh.OKABE_ITO
    rng = np.random.default_rng(521)          # fixed seed, reproducible tile

    n = 90
    x = rng.uniform(0, 10, n)
    y = 2.1 + 0.78 * x + rng.normal(0, 1.35, n)

    # Least squares plus a widening prediction band: the course in one picture.
    b1, b0 = np.polyfit(x, y, 1)
    gx = np.linspace(-0.4, 10.4, 200)
    fit = b0 + b1 * gx
    band = 1.5 * np.sqrt(1 + ((gx - x.mean()) / x.std()) ** 2 / n) * 1.25

    # Tile aspect matches the photo tiles it sits beside on the slide.
    fig, ax = plt.subplots(figsize=(6.1, 5.25), dpi=100)
    ax.fill_between(gx, fit - band, fit + band, color=OK["vermillion"],
                    alpha=0.13, linewidth=0)
    ax.plot(gx, fit, color=OK["vermillion"], linestyle="-", linewidth=3.2)
    ax.scatter(x, y, s=38, color=OK["blue"], alpha=0.85, edgecolors="none",
               zorder=3)

    ax.set_xlim(-0.4, 10.4)
    ax.set_ylim(y.min() - 1.6, y.max() + 1.6)
    ax.set_xticks([])
    ax.set_yticks([])
    # No spines or ticks: at tile size (about 176 x 215 px on the slide) axis
    # chrome is unreadable clutter. The mark itself carries the meaning.
    for side in ("top", "right", "bottom", "left"):
        ax.spines[side].set_visible(False)
    ax.grid(False)

    fig.tight_layout(pad=0.35)
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, transparent=True, dpi=100)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
