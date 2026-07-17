---
deck: "Appendix: Full Cov[ŵ] derivation"
subtitle: "INFO 521 · Module 3 — supplement"
source_qmd: modules/m3-mle-uncertainty/appendix-covariance.qmd
dest: scripts/m3-mle-uncertainty/appendix-covariance.script.md
scenes: 4
est_spoken_words: 396
est_runtime_min: 3.0   # at ~130 wpm
---

## Title slide — Appendix: Full Cov[ŵ] derivation

This is an appendix to Module 3 — the full derivation of the covariance of w-hat. The main deck stated the result, sigma-squared times X-transpose-X inverse, and promised the derivation here. So here it is, line by line. The whole thing collapses through one identity — X-transpose-X inverse, times X-transpose-X, is the identity — and one very satisfying cancellation. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Where we are

The setup, carried over from the main deck. w-hat is unbiased — its expectation is the true w — and we're after its covariance, which I claimed is sigma-squared times X-transpose-X inverse. Remember what's random here: only y. The design matrix X and the true weights w are fixed. And the model tells us two facts about y: its expectation is X-w, and its covariance is sigma-squared times the identity — meaning independent noise of equal variance on every patient.

## Set up the second moment

Start from the definition of covariance. Because w-hat is unbiased, its covariance is the expected outer product, w-hat w-hat-transpose, minus w w-transpose.

> [cue: first fragment reveals]

Substitute w-hat equals X-transpose-X inverse X-transpose y, and pull all the constant matrices outside the expectation — they're fixed, only y is random. What's left in the middle is the expected outer product of y with itself, sandwiched between those constant factors.

> [cue: second fragment reveals]

And that middle object, the second moment of y, comes from the covariance definition rearranged: it's X w w-transpose X-transpose, from the mean, plus sigma-squared times the identity, from the noise.

## Collect the terms

Now substitute that back in, and use the key identity — X-transpose-X inverse, times X-transpose-X, is just the identity — on each piece. The first piece collapses back to w w-transpose. The second collapses to sigma-squared times X-transpose-X inverse.

> [cue: first fragment reveals]

And here's the satisfying step: that w w-transpose we just recovered cancels exactly against the minus w w-transpose from the covariance definition. The bias-free part drops clean out, and what's left is pure noise scaled by the inverse Gram matrix — the covariance of w-hat is sigma-squared times X-transpose-X inverse.

> [cue: second fragment reveals]

And in the accent color, tie it back to the main deck: that is precisely the inverse Fisher information. The negative second derivative of the log-likelihood was one-over-sigma-squared X-transpose-X, which is the Fisher information — so the covariance of w-hat is its inverse. Curvature and uncertainty, inverses of each other, exactly as the main deck promised.
