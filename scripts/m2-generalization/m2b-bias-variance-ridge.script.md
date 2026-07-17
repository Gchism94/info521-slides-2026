---
deck: "Generalization"
subtitle: "INFO 521 · Module 2 · Lecture B — Bias-Variance & Regularization"
source_qmd: modules/m2-generalization/m2b-bias-variance-ridge.qmd
dest: scripts/m2-generalization/m2b-bias-variance-ridge.script.md
scenes: 17
est_spoken_words: 1663
est_runtime_min: 12.8   # at ~130 wpm
---

## Title slide — Generalization

Welcome back to Module 2 — Lecture B, bias-variance and regularization. In Lecture A we found the U-shaped test-error curve and used cross-validation to find its bottom. Today we answer the two questions that leaves open: why is there a U at all — that's the bias-variance decomposition — and how do we deliberately move along it, which is regularization, and specifically ridge regression. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four outcomes. First, explain the bias-variance decomposition of expected test error. Second, state the tradeoff and connect it back to that U-curve. Third, derive and apply ridge regression, and tune its penalty by cross-validation. And fourth — the one I most want to stick — connect ridge straight back to the uniqueness condition from Module 1. Lecture A found the U by experiment; today we explain it, and get a knob to control it.

## Recap: the U, and why

One line back to Lecture A. Test error is U-shaped in complexity — underfit on the left, overfit on the right — and cross-validation told us where the bottom sits. But it never told us why the U is there in the first place. Why should making a model more flexible ever make it worse? Answering that is the whole first half of today. The U isn't an accident; it's the sum of two competing quantities, and we're about to name them.

## Bias and variance, intuitively

Here's the intuition, and it rests on a thought experiment we'll reuse later in the term. Imagine refitting your model on many different datasets, all drawn the same way. Two things can go wrong. Bias is the systematic miss: if the model's too simple, then even averaged over all those datasets it can't reach the truth — it's wrong in the same direction every time. Variance is the sensitivity: if the model's too flexible, it swings wildly from one dataset to the next, chasing whatever noise each one happened to contain. Hold onto that repeated-datasets picture — in Module 3 we draw the exact same story in parameter space, as a cloud of weight estimates. Here it's the spread of the fitted curve; there it's the spread of w-hat.

## Bias and variance on the data

And here it is, drawn. Two panels, each showing the true curve dashed, twenty fits from twenty resampled datasets as thin lines, and their average as the bold line. On the left, degree one: the twenty fits huddle tightly together — low variance — but their average clearly misses the curve. That gap is bias. On the right, degree nine: now the average tracks the truth beautifully — low bias — but the individual fits fan out all over the place. That spread is variance. Too simple is biased but stable; too flexible is accurate on average but wildly unstable. Neither one is what you actually want.

## The decomposition

We can make that exact. For a fixed patient, the expected test error — averaged over all those training sets — splits cleanly into three pieces. Bias squared, the systematic part. Variance, the sensitivity part. And a third term, sigma-squared: the irreducible noise, the scatter baked into the data itself that no model, however clever, can ever beat. The full derivation is in the bias-variance appendix if you want every line. The headline is that these three add up — and the first two trade off against each other, while the third just sits underneath as a floor.

## The tradeoff

So watch what happens as you turn complexity up. Bias-squared falls — a more flexible model can represent more of the truth. But variance rises — that same flexibility starts chasing the sample. Their sum is exactly the U from Lecture A, resting on the irreducible sigma-squared floor. Underfitting is the bias-dominated left wall; overfitting is the variance-dominated right wall. And here's the moral, in the accent color: the best model is not the most flexible one. It's the one that balances those two competing errors against each other.

## Section — Controlling the tradeoff: regularization.

So how do we deliberately move along that U, rather than just finding where we happen to sit on it? Regularization.

## Ridge regression

The idea is simple, and a little sneaky. Take the ordinary squared-error loss and add a penalty on the size of the weights — the squared length of w, scaled by a knob, lambda. Now the fit has to care about two things at once: matching the data, and keeping its weights small. Why would small weights help? Because those wild, wiggly overfit curves are precisely the ones with huge coefficients yanking them up and down. Penalize weight size and you discourage the wiggle. With lambda at zero you're back to ordinary least squares; turn lambda up and you shrink the weights toward zero, trading a little bias for a lot less variance. Lambda is the knob that walks you along the U — and you tune it, of course, by cross-validation.

## Ridge: the closed form

And here's the lovely part — ridge has a closed form, almost the same as before. The penalty just drops a lambda-times-identity inside the normal equations: w-hat-ridge is X-transpose-X, plus lambda-I, all inverse, times X-transpose y. One added term.

> [cue: fragment reveals the accent callback]

Now look at what that one term does, because it's a genuine callback. Back in Module 1, the solution was unique only when X-transpose-X was invertible — full column rank. Add lambda-times-identity, with lambda positive, and you lift every eigenvalue of that matrix up by lambda. It becomes positive definite — which means always invertible, even when you have more features than patients, even when two columns are collinear. So ridge doesn't just reduce variance; it hands you, for free, the unique solution that Module 1 had to assume it had. Same X-transpose-X, back again, now bulletproofed.

## The coefficient path

Here's ridge doing its thing, coefficient by coefficient. The horizontal axis is lambda, on a log scale, and each line is one weight. On the left, small lambda, the weights sit at their unregularized values — a spread of nonzero numbers. Slide right, and every one of them is drawn smoothly toward zero. No weight escapes the pull. That's shrinkage made literal. Crank lambda high enough and the whole model flattens out toward a constant. The art, as always, is stopping somewhere in the middle.

## The two limits

Two limits pin down the whole range. Send lambda to zero and the penalty vanishes — ridge is just ordinary least squares again, the Module 1 fit: maximum variance, minimum bias, the overfit right end of the U. Send lambda to infinity and the penalty swamps everything — the weights are crushed toward zero and the model predicts a flat constant: maximum bias, minimum variance, the underfit left end. Both extremes are degenerate. The lambda you actually want lives in between, and cross-validation is what finds it.

## Choosing λ by cross-validation

So we do exactly what Lecture A taught — but with lambda as the knob instead of degree. Here's five-fold cross-validation error against lambda, again on a log axis, for a deliberately over-flexible degree-fourteen model. Same U shape: elevated on the left where lambda's too small and the model overfits, lowest at some moderate lambda, climbing steeply on the right where lambda's so big the model underfits. The marked minimum is the lambda we pick. A wildly over-flexible model, tamed down to just-right by a single well-chosen penalty.

## Live demo: bias-variance / ridge explorer

Let's drive all of this live. This tool reframes it as a dose–response problem — each point is a patient's response at some treatment dose, and the true curve, the dashed one, is an inverted-U peaking at a moderate dose. Start at degree one: a straight line, badly underfitting that hump — and watch the train and test MSE readouts, both sitting high. Now push the degree up, step by step. Train MSE keeps dropping, but keep your eye on test MSE — it bottoms out and then starts climbing again. That's the U happening live, in the numbers. Now the money button: "Show twenty fits." It refits on twenty different noisy samples and overlays them all. At low degree they sit right on top of each other; crank the degree up and watch them fan out into a wild spray — and that spray is variance, made visible. Here's the fix: slide the ridge penalty lambda up. Watch the fan pull back in and stiffen, the fits calming down as variance drops and a little bias creeps in. "New sample" redraws the data, "Show test points" adds the held-out orange diamonds, and "Reset" puts it all back to degree one with no penalty.

> [cue: interact directly on the full-bleed slide — raise the degree (test MSE turns up) → Show 20 fits (fan widens) → slide λ up (fan tightens) → Reset; the CV-error snapshot on the next slide is the PDF fallback if the embed can't load]

## Explorer — static fallback

For print or PDF, or if the embed doesn't load, this snapshot stands in — the cross-validation-error-versus-lambda curve with the chosen lambda marked, the same balance the live tool lets you feel by hand. Live in class, we drive the explorer itself on the slide before; there's nothing new to learn here.

> [cue: optional — skip aloud if the live embed worked; this slide exists only for print and PDF]

## Forward hook

One forward hook before we recap, and it's a big one — flagged in the accent color. That ridge penalty, lambda times the squared length of w, is secretly a Gaussian prior on the weights. Fitting ridge is doing MAP estimation — maximum a posteriori — under a prior belief that the weights are small. Put plainly: "shrink the weights toward zero" and "believe, before seeing any data, that the weights are probably small" are the very same statement. We derive that equivalence properly in Module 4, where a Gaussian prior meets a Gaussian likelihood. One more object doing double duty across the term.

## Recap

To recap Module 2. Bias-variance: test error is bias squared, plus variance, plus the irreducible sigma-squared — and the U is their sum. Ridge: add lambda-times-the-squared-weights to the loss, and get the closed form X-transpose-X plus lambda-I, inverse, X-transpose y — always invertible, so uniqueness comes for free. And tune lambda by cross-validation, the knob that balances the whole tradeoff. There's no standalone checkpoint for this module; the discipline gets assessed through your modeling choices in Project 1. Carry one thing forward: ridge is a prior in disguise, and Module 4 makes that exact.
