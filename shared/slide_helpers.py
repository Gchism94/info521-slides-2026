"""INFO 521 slides — shared matplotlib + data helpers for {python} figure cells.

Design goals (the hardened figure pipeline every deck inherits):

* **Okabe-Ito palette, identical hex** to theme/info521-head.html and the
  activities repo, with a **redundant non-color cue** (line style + marker) paired
  to every series so figures read in mono / colorblind.
* **Transparent facecolor** so one static SVG sits on either the dark or the
  light deck theme. Because a pre-rendered SVG can't follow the runtime toggle,
  axis chrome (spines / ticks / labels) uses a single neutral gray chosen to
  clear ~4:1 contrast on BOTH #1a1a1a (dark) and #f5f5f5 (light). Data ink uses
  Okabe-Ito hues, which are legible on both; yellow and black are kept OUT of the
  default cycle (yellow vanishes on light, black on dark).
* **SVG output**, alt text required.
* A thin **NHANES loader shim** over the editable-installed `info521` package —
  no vendoring; the package is the single source of truth.
"""
from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

__all__ = [
    "OKABE_ITO",
    "use_slide_style",
    "series_style",
    "finalize",
    "load_nhanes",
    "primary_predictor",
]

# -----------------------------------------------------------------------------
# Palette. Hex is identical to theme/info521-head.html (--ok-*) and the
# info521-activities-2026 / info521.plotting palettes — the course standard.
# -----------------------------------------------------------------------------
OKABE_ITO = {
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "green": "#009E73",
    "orange": "#E69F00",
    "skyblue": "#56B4E9",
    "yellow": "#F0E442",
    "purple": "#CC79A7",
    "black": "#000000",
}

# Default series order + the redundant non-color cues paired to each. Yellow and
# black are excluded here (poor contrast on one theme) but remain in OKABE_ITO
# for deliberate, contrast-checked use.
_CYCLE_COLORS = ["blue", "vermillion", "green", "orange", "skyblue", "purple"]
_LINESTYLES = ["-", "--", "-.", ":", (0, (3, 1, 1, 1)), (0, (5, 1))]
_MARKERS = ["o", "s", "^", "D", "v", "P"]

# Neutral axis-chrome gray: ~4:1 contrast on both the dark and light deck bg, so
# the same SVG stays readable whichever way the theme toggle is set.
_CHROME = "#7a7a7a"
_GRID = "#7a7a7a"


def use_slide_style() -> None:
    """Apply the INFO 521 slide figure defaults. Call once near the top of a deck.

    Transparent facecolor, Okabe-Ito color + linestyle prop-cycle, neutral chrome,
    projection-friendly sizes, and SVG-friendly text.
    """
    mpl.rcParams.update({
        # Sit on either theme.
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "savefig.facecolor": "none",
        "savefig.transparent": True,

        # Crisp vector text in the embedded SVG (keep text as text, not paths).
        "svg.fonttype": "none",

        # 16:9-friendly, sized for projection.
        "figure.figsize": (8.5, 4.8),
        "figure.dpi": 110,
        "font.size": 15,
        "axes.titlesize": 17,
        "axes.labelsize": 15,
        "legend.fontsize": 13,
        "lines.linewidth": 2.4,
        "lines.markersize": 7,

        # Neutral chrome readable on dark AND light.
        "text.color": _CHROME,
        "axes.labelcolor": _CHROME,
        "axes.edgecolor": _CHROME,
        "axes.titlecolor": _CHROME,
        "xtick.color": _CHROME,
        "ytick.color": _CHROME,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": _GRID,
        "grid.alpha": 0.30,
        "grid.linewidth": 0.8,

        # Color paired with a dash style so series differ without color.
        "axes.prop_cycle": (
            cycler(color=[OKABE_ITO[c] for c in _CYCLE_COLORS])
            + cycler(linestyle=_LINESTYLES)
        ),
    })


def series_style(i: int) -> dict:
    """Return ``{color, linestyle, marker}`` for series ``i`` (wraps at 6).

    Use when you need the marker cue too (e.g. scatters or point-markers on a
    line), so each series is distinguishable by hue, dash, AND shape.

    >>> ax.plot(x, y, **series_style(0))   # blue, solid, circle
    """
    n = len(_CYCLE_COLORS)
    k = i % n
    return {
        "color": OKABE_ITO[_CYCLE_COLORS[k]],
        "linestyle": _LINESTYLES[k],
        "marker": _MARKERS[k],
    }


# Reject obvious non-descriptions so "alt-text-required" means something.
_ALT_PLACEHOLDERS = {"", "todo", "tbd", "figure", "plot", "chart", "image", "x"}


def finalize(fig, *, alt: str):
    """Finalize a figure for a slide. **Alt text is required.**

    Tightens layout and enforces a real alt-text description. Pass the SAME string
    to the cell's ``#| fig-alt:`` option so it reaches the rendered HTML/SVG::

        #| fig-alt: "Scatter of systolic BP vs age with a least-squares fit line."
        fig, ax = plt.subplots()
        ...
        finalize(fig, alt="Scatter of systolic BP vs age with a least-squares fit line.")

    Raises
    ------
    ValueError
        If ``alt`` is missing, too short, or a placeholder — fail loudly rather
        than ship an inaccessible figure.
    """
    if not isinstance(alt, str) or alt.strip().lower() in _ALT_PLACEHOLDERS or len(alt.strip()) < 15:
        raise ValueError(
            "finalize() requires a real alt-text description (>=15 chars, not a "
            "placeholder). Describe what the figure SHOWS, and mirror it in the "
            "cell's `#| fig-alt:` option."
        )
    fig.tight_layout()
    # Belt-and-suspenders: keep transparency even if rcParams were overridden.
    fig.patch.set_alpha(0.0)
    for ax in fig.axes:
        ax.patch.set_alpha(0.0)
    fig.set_label(alt.strip())  # stash for optional retrieval / debugging
    return fig


# -----------------------------------------------------------------------------
# NHANES loader shim. Thin wrapper over the editable-installed `info521`
# package (info521-projects-2026/common/info521). NOT vendored — that package is
# the single source of truth and ships the NHANES extract its loader resolves.
# -----------------------------------------------------------------------------
def load_nhanes(path: str | None = None) -> dict:
    """Load the NHANES clinical dataset via ``info521.data.load_clinical``.

    Returns the loader's dict: ``{X, y, dbp, features, primary, target}``. See
    the package docstring for the column contract (target ``sbp``; ``dbp``
    reserved; primary predictor ``age``).

    Raises
    ------
    ModuleNotFoundError
        If the ``info521`` package is not importable — install it editable into
        the render venv (see requirements.txt / render.sh). Do NOT vendor a copy.
    """
    try:
        from info521.data import load_clinical
    except ModuleNotFoundError as exc:  # pragma: no cover - environment guard
        raise ModuleNotFoundError(
            "The `info521` loader package is not installed in this environment. "
            "Install it editable (single source of truth — do not vendor):\n"
            "    uv pip install -e ../info521-projects-2026\n"
            "or run ./render.sh, which bootstraps the venv from requirements.txt."
        ) from exc
    return load_clinical(path)


def primary_predictor(ds: dict):
    """Return the 1-D primary-predictor column ('age') from a loaded dataset."""
    from info521.data import primary_predictor as _pp
    return _pp(ds)
