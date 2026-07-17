---
deck: "Appendix: Matrix Calculus for the Normal Equations"
subtitle: "INFO 521 · Module 1 · Lecture B — supplement"
source_qmd: modules/m1-linear-least-squares/appendix-matrix-calculus.qmd
dest: scripts/m1-linear-least-squares/appendix-matrix-calculus.script.md
scenes: 5
est_spoken_words: 464
est_runtime_min: 3.6   # at ~130 wpm
---

## Title slide — Appendix: Matrix Calculus for the Normal Equations

This is an appendix to Module 1, Lecture B — the matrix calculus behind the normal equations. In the lecture I stated the gradient of the least-squares loss and asked you to take it on faith; here we earn it. Two vector-calculus identities, one expansion, one differentiation, and out falls w-hat. It's optional depth — but if you ever want to see exactly where that gradient comes from, this is it. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Where we are

Quick reminder of the target. In Lecture B I wrote the gradient of the loss directly — minus two over N, times X-transpose, times the residual y minus X-w — and used it without proof. This appendix fills in the two identities behind that expression, and then turns the crank all the way to w-hat equals X-transpose-X inverse, X-transpose y. Nothing here is deep; it's just the derivative mechanics, laid out honestly.

## Two identities

Two facts about differentiating with respect to a vector, and everything else follows. Take a constant vector a and a constant matrix A.

> [cue: first fragment reveals]

First, the derivative of a linear form — a-transpose w, with respect to w — is just the coefficient vector a itself. The linear term differentiates to its own coefficients.

> [cue: second fragment reveals]

Second, the derivative of a quadratic form — w-transpose A w — is A-plus-A-transpose, times w. And when A is symmetric, that collapses to a clean two-A-w. Keep that symmetric case in your pocket, because X-transpose-X is symmetric — which is exactly why our answer is going to come out so tidy.

## Expand the loss

Now write the loss as a quadratic in w — one over N, times the residual transposed, times itself.

> [cue: fragment reveals]

Multiply it out and you get three pieces: a constant, y-transpose y; a linear term, minus two w-transpose X-transpose y — the two cross terms folded into one, because they're equal scalars; and a quadratic term, w-transpose X-transpose-X w. A constant, a linear term, and a quadratic term — which is precisely the two shapes our identities know how to handle.

## Differentiate & solve

So apply them term by term. The constant dies. The linear term, with a equal to X-transpose y, differentiates to minus two X-transpose y. And the quadratic term, with A equal to the symmetric X-transpose-X, differentiates to two X-transpose-X w.

> [cue: first fragment reveals]

Collect those and factor, and you get exactly the gradient the lecture used — minus two over N, times X-transpose, times the residual y minus X-w. Earned now, not asserted.

> [cue: second fragment reveals]

Set it to zero, the minus-two-over-N drops out as a nonzero scalar, and you're left with the normal equations — X-transpose-X w-hat equals X-transpose y — and solving gives w-hat equals X-transpose-X inverse, X-transpose y. That gradient-to-normal-equations step is the one the Project-1 checkpoint asks you to reproduce cold.
