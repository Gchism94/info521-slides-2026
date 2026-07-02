# CLAUDE.md — Guidance for Slides Repo

Guidance for Claude Code working in the slides repo.

## Embedding Activities into Slides

Each reveal.js deck can optionally embed its corresponding peer-engagement activity tool from the [`info521-activities-2026`](../info521-activities-2026) repo. The embed is a single reference maintained in `_variables.yml` so it updates across all decks when a term rolls forward.

### Module–Activity Mapping

| Module | Deck | Corresponding Activity |
|--------|------|------------------------|
| M1 | m1-linear-least-squares | week01-least-squares |
| M2 | m2-generalization | week02-bias-variance |
| M3 | m3-mle-uncertainty | week03-bayesian-updating |
| M4 | m4-* (TBD) | week04-logistic-regression |
| M5 | m5-* (TBD) | week05-kmeans |
| M6 | m6-* (TBD) | week06-pca |
| M7 | m7-* (TBD) | — (no activity) |

### Embedding Pattern: Two Options

#### **PRIMARY (Full-Bleed, Interactive)**
Use a reveal.js `background-iframe` slide. The activity tool fills the entire slide and remains interactive (mouse/keyboard).

```markdown
## [Slide Title] {background-iframe="https://gchism94.github.io/info521-activities-2026/week01-least-squares/" background-interactive="true"}
```

**Notes:**
- Paste the **full, literal URL** into the `background-iframe` attribute.
- `_variables.yml` is NOT expanded inside slide attributes, so use the final URL directly.
- Add a blank markdown slide body (Quarto requires a body). The iframe fills the viewport.
- The activity is **fully interactive** — students can use the tool directly during lecture.
- **Locally** (before Pages goes live), the iframe may appear blank; this is expected.

#### **ALTERNATE (Windowed, Shortcode-Expanded)**
Embed an iframe in the slide body. Useful if you want to pair the activity with explanatory text.

```markdown
## Slide Title

Brief explanation or context.

<iframe class="activity-embed" src="{{< var activities_url >}}/week01-least-squares/"></iframe>
```

**Notes:**
- Quarto **will expand** `{{< var activities_url >}}` inside the HTML body.
- Apply the `.activity-embed` class for consistent sizing and styling (see **Styling** below).
- The iframe is smaller; less immersive but pairs well with commentary.

### Styling for Windowed Embeds

Add this CSS to the deck theme or in a separate `<style>` block if you use the alternate pattern:

```css
.reveal .activity-embed {
  width: 100%;
  height: 68vh;
  border: 0;
  border-radius: 8px;
}
```

This sets the iframe to fill the slide width, use 68% viewport height (leaving room for a title + text above), no border, and subtle rounded corners.

### When to Embed

- **Lecture flow**: If the slide naturally leads into hands-on practice, embed the tool so students can try it immediately.
- **Live interaction during class**: The full-bleed `background-iframe` pattern works best for this — no distractions, full tool interactivity.
- **Assignment reference**: If a slide introduces the week's tool but doesn't need live interactivity, use the alternate pattern or no embed.

### Adding an Embed to a Deck

1. Identify the relevant module and its corresponding activity (see **Module–Activity Mapping** above).
2. Choose PRIMARY (full-bleed) or ALTERNATE (windowed) pattern.
3. **PRIMARY example** (add a new slide in the .qmd):
   ```markdown
   ## Try It: Least Squares {background-iframe="https://gchism94.github.io/info521-activities-2026/week01-least-squares/" background-interactive="true"}
   ```
4. **ALTERNATE example** (add a new slide with markdown body):
   ```markdown
   ## Try It: Least Squares

   Adjust the data points and weights below to minimize the loss function.

   <iframe class="activity-embed" src="{{< var activities_url >}}/week01-least-squares/"></iframe>
   ```
5. Render and preview locally to confirm the slide builds cleanly. The iframe URL may not load offline; Pages-live verification is OK.
6. Commit with a message like: `feat(slides): embed week01 least-squares tool in Module 1 deck`.

### Pre-built Embeds

- **M1 (Linear Least Squares)**: Demo embed added near the end of the linear regression content (PRIMARY, full-bleed). See `modules/m1-linear-least-squares/index.qmd` for the example.

---

## Legacy Conventions

- **PML notation**, **Okabe-Ito palette**, **classic scripts**, **dark mode default** — all unchanged from README.md.
- No ES modules (decks must open via `file://` and render to self-contained HTML for D2L).
