---
deck: "Bayesian Inference"
subtitle: "INFO 521 · Module 4 · Lecture B — The Conjugate Gaussian Posterior"
source_qmd: modules/m4-bayesian-inference/m4b-gaussian-posterior.qmd
dest: scripts/m4-bayesian-inference/m4b-gaussian-posterior.script.md
scenes: 12
est_spoken_words: 1518
est_runtime_min: 11.7   # at ~130 wpm
---

## Title slide — Bayesian Inference

Welcome back to Module 4 — Lecture B, the conjugate Gaussian posterior. This is the keystone of the whole course, so I want you fully present for it. In Lecture A we put a distribution on a single proportion and watched it update by simple addition. Today we scale that exact move up to the regression weights of our Module 1 model: a Gaussian prior meets a Gaussian likelihood, and out comes a Gaussian posterior for w, in closed form. This is where the entire Project 1 pipeline comes to rest. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four outcomes. First, place a Gaussian prior on the weights and state the conjugate posterior. Second, read the update formulas — what shrinks, what dominates, and why X-transpose-X shows up yet again. Third, show that ridge regression is just this posterior's peak under a particular prior — cashing in the hook we planted in Module 2. And fourth, form the posterior predictive and separate its two sources of uncertainty. Everything from Lecture A carries up: theta becomes w, Beta becomes Gaussian, counts become matrices — but the closed form survives.

## From θ to w

In Lecture A we put a distribution on a proportion. Now we put one on the regression weights of the model we've had since day one. Two ingredients. The prior: a Gaussian on w, centered at some m-nought — say, blood pressure near 120 with no age effect — with covariance S-nought that says how loosely we hold that belief; a wide one is weakly informative, barely committing. And the likelihood: the Module 3 linear-Gaussian object, the product of per-patient normals centered on the line. One simplification for today — we treat the noise sigma-squared as known, plugging in the estimate from m3a, because that's what keeps the algebra conjugate. Gaussian prior times Gaussian likelihood is the vector version of Beta times binomial: same in-family closure, now carrying matrices.

## The conjugate Gaussian posterior

And here it is — the keystone. Gaussian prior times Gaussian likelihood gives a Gaussian posterior, in closed form, described by two formulas. The posterior covariance S-N is the inverse of S-nought-inverse plus one-over-sigma-squared X-transpose-X. And the posterior mean m-N is S-N times the quantity S-nought-inverse m-nought, plus one-over-sigma-squared X-transpose y. Don't let the symbols wash over you — recognize every ingredient. There's X-transpose-X, from Module 1. There's one-over-sigma-squared, from Module 3. And there's the prior, from Lecture A. Three modules, meeting in two boxed formulas. In the accent color: Project 1 ends exactly here. The whole pipeline — data, model, loss, likelihood, posterior — closes on this pair.

## Reading the formulas

Let's read them, because they're far more intuitive in the right units — precisions, which are just inverse covariances. In precision terms the update is addition all over again: the posterior precision is the prior precision plus the data's precision. Prior information plus data information, added. And look hard at that data term — one-over-sigma-squared X-transpose-X. That is the Fisher information from m3b, the same matrix, making its fourth appearance in this course: the loss bowl in Module 1, the negative Hessian and Fisher information in Module 3, and now the data's contribution to the posterior. The posterior mean is a precision-weighted blend of the prior mean and the data — the vector version of Lecture A's shrinkage. And here's the line I want you to sit with: as N grows, the data drowns the prior, the mean marches to the maximum-likelihood estimate, and the posterior covariance becomes sigma-squared times X-transpose-X inverse — which is exactly the covariance of w-hat from Module 3. Frequentist spread and Bayesian belief, agreeing in the limit.

## Watching the posterior contract

And you can watch that convergence happen. This is the intercept-slope plane, and each ellipse is a two-sigma posterior contour. The wide blue one is the prior — vague, barely committing. Add ten patients and it contracts to the orange one. A hundred, the green. The full five thousand, and it's collapsed to a tiny vermillion dot, sitting right on the least-squares estimate marked by the cross. Now — you have seen this picture before. It's the covariance ellipse from m3b, reborn. But the meaning is flipped. There, the ellipse was the spread of w-hat over imagined repeated datasets. Here, it's our belief about w given the one real dataset we have, tightening as patients arrive. Same math, opposite epistemics — and by the full sample, the two land in the very same place.

## Special case: the ridge prior

Now a special case that pays off an old debt. Take the simplest prior — zero mean, and isotropic: S-nought equals tau-squared times the identity, which just says "I think the weights are small, equally in every direction." Plug it in, and the posterior mean becomes X-transpose-X, plus sigma-squared-over-tau-squared times identity, inverse, times X-transpose y. Look at that. It's ridge regression, exactly — with the penalty lambda equal to sigma-squared over tau-squared. This is the forward hook from Module 2, finally cashed in: the ridge penalty is a Gaussian prior. And now lambda isn't an arbitrary dial — it's a statement about the world. Noisy data, a big sigma-squared, or a tight prior belief, a small tau-squared — both tell you to shrink harder. Regularization is a prior in disguise; here's the disguise coming off.

## MAP vs. the full posterior

Which raises a sharp question — if ridge is Bayesian, what exactly is it computing? The answer is the MAP estimate, maximum a posteriori: the single highest point of the posterior. And for Gaussians the peak equals the mean, so MAP just hands you back m-N. But notice what MAP throws away — it keeps the location and discards the spread, the whole covariance S-N. It's regularized point-fitting wearing Bayesian clothes. The posterior is the real answer; that spread is what predictions actually use, as we'll see on the next slide. Right now, in this cozy Gaussian world, MAP and the full posterior look almost interchangeable — peak equals mean, no harm done. Hold that thought, because Module 5's posteriors won't be Gaussian, and the gap between the peak and the whole distribution becomes the entire story.

## Predicting a new patient

To predict a new patient, we do the Bayesian thing and integrate the model over the whole posterior. The result is beautifully readable: a Gaussian centered on the obvious prediction, m-N-transpose x-star, with a variance made of two distinct pieces added together. The first piece is sigma-squared — patient-level scatter, the irreducible noise, Module 2's floor; no amount of data removes it. The second piece is x-star-transpose S-N x-star — and that's our ignorance about w. It shrinks as data accumulates, and it grows as you predict further from the center of your data. Two kinds of uncertainty, two different remedies. Plug-in prediction uses only the first term and is quietly over-confident — most dangerously out at the extreme ages, which is exactly where clinical decisions get risky.

## The predictive band on NHANES

Here's that made visible, fit on just a hundred and twenty patients so the effect is easy to see. The vermillion line is the predictive mean, and the shaded band is the full predictive uncertainty — both terms together. The green dashed lines are the noise-only band, the first term alone. Through the middle, where we have plenty of data, the two agree — parameter uncertainty is negligible there. But watch the edges: out at the youngest and oldest ages, the shaded band peels away from the dashed one and flares wider. That flare is precisely the x-star-transpose S-N x-star term — our growing ignorance about the line where we've simply seen fewer patients. Fit on all five thousand, it would nearly vanish. Scarcity is what Bayes prices, honestly — and it prices it most where you have the least data.

## The evidence, briefly

> [cue: optional — cut if running long; nothing downstream depends on it]

One quick idea, if we have time. Remember the denominator we waved away in Lecture A — p-of-D, the evidence, or marginal likelihood? It's the likelihood averaged over the prior. And it's quietly powerful: it scores a whole model, prior included, not a single parameter value. Compare the evidence of two models and you can rank them without a test set at all — and it comes with a built-in Occam's razor, because an over-flexible model spreads its prior thin and scores lower. For today's conjugate model, it too is closed form. Beyond the Gaussian world, it's the first thing to break — which is a nice segue to where we're headed next. Cross-validation, by the way, is its frequentist cousin.

## Recap & bridge

To recap the keystone. The conjugate Gaussian posterior: precision adds, prior plus data — S-N-inverse equals S-nought-inverse plus one-over-sigma-squared X-transpose-X, and the mean is the precision-weighted blend. That's Project 1's endpoint. Ridge is its MAP under a zero-mean Gaussian prior, with lambda equal to sigma-squared over tau-squared. And the predictive variance splits cleanly into noise plus our ignorance about w. Now the cliff edge, in the accent color. Every single formula today existed because everything in sight was Gaussian. In Module 5 we binarize the outcome — hypertensive or not — the Gaussian likelihood is gone, conjugacy breaks, no closed form survives, and approximation becomes the craft. That's the second act of the course.
