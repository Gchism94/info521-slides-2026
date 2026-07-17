---
deck: "Appendix: The Bias–Variance Decomposition"
subtitle: "INFO 521 · Module 2 · Lecture B — supplement"
source_qmd: modules/m2-generalization/appendix-bias-variance.qmd
dest: scripts/m2-generalization/appendix-bias-variance.script.md
scenes: 6
est_spoken_words: 648
est_runtime_min: 5.0   # at ~130 wpm
---

## Title slide — Appendix: The Bias–Variance Decomposition

This is an appendix to Module 2, Lecture B — the full derivation of the bias-variance decomposition. In the lecture I claimed that expected test error splits cleanly into bias squared, variance, and irreducible noise. Here we prove it. The whole thing rests on one algebraic trick and a couple of cross terms conveniently dying. It's optional depth, but the argument is genuinely satisfying. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Where we are

Here's what we're proving: at a fixed input, the expected squared error equals bias squared, plus variance, plus sigma-squared. First, the bookkeeping — four objects, all at that one fixed point. The truth: y is f-of-x plus noise epsilon, where epsilon is mean-zero with variance sigma-squared. The estimate: f-hat, which is random because it depends on whichever training set we happened to draw — that's the repeated-datasets picture from Module 3, now in prediction space. The average fit: f-bar, the expectation of f-hat over all those training sets — the orange curve from the repeated-fits figure. And crucially, the test-time noise epsilon is a fresh draw, independent of the training set.

## The one trick: add and subtract f̄

Here's the one trick the whole proof turns on — add and subtract the average fit, f-bar. Write the miss, y minus f-hat, as three centered pieces: f minus f-bar, the systematic miss; plus f-bar minus f-hat, the dataset luck; plus epsilon, the fresh noise.

> [cue: fragment reveals]

Now square that sum and take the expectation, over both the training set and the noise. Squaring a sum of three gives you three squared terms — which will become bias squared, variance, and sigma-squared — plus three cross terms. And all the real work is showing those cross terms vanish.

## The cross terms die

So let's kill the cross terms, one at a time.

> [cue: first fragment reveals]

The first pairs the systematic miss with the dataset luck. But f minus f-bar is a constant — there's no randomness left in it — so it pulls straight out of the expectation, and what remains is the expected value of f-bar minus f-hat, which is zero by the very definition of f-bar as the average of f-hat. Constant times zero is zero.

> [cue: second fragment reveals]

The other two both involve epsilon. And because the test noise is mean-zero and independent of the training set, each one factors into something times the expectation of epsilon — which is zero. All three cross terms gone. And notice exactly where independence earned its keep: right there. If training data leaked into the test draw, that last factorization would fail. Leakage doesn't just spoil your estimate; it breaks the theorem itself.

## The decomposition, earned

What survives the carnage is exactly the decomposition. Bias squared — how far the average fit sits from the truth, the price of rigidity. Variance — how much a single fit swings around that average, the price of flexibility. And sigma-squared — the noise floor no model, however tuned, can ever beat. In the accent color: complexity moves the first two in opposite directions, their sum is the U-curve from the main lectures, and ridge's lambda is what walks you along it. Point back to the repeated-fits figure and it's the same statement — degree one was the bias term made visible; degree nine was the variance term.

## Fine print

Three things the derivation quietly assumed — worth saying out loud, once. First, this is one input at a time; the decomposition holds pointwise, and real test error averages it over the whole input distribution. Second, it's squared loss only — that clean three-way split is a special property of the square; other losses split differently, or not at all. And third, these are expectations over repeated datasets, not quantities you can read off your one sample. On your single dataset you see one draw — which is exactly why cross-validation estimates bias and variance rather than computing them. That's the loop back to Lecture A, closed.
