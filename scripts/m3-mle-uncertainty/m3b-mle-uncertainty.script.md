---
deck: "Properties of MLE: Uncertainty in Parameters"
subtitle: "INFO 521 · Module 3 · Lecture B — Properties of the MLE"
source_qmd: modules/m3-mle-uncertainty/m3b-mle-uncertainty.qmd
dest: scripts/m3-mle-uncertainty/m3b-mle-uncertainty.script.md
scenes: 15
est_spoken_words: 1548
est_runtime_min: 11.9   # at ~130 wpm
---

## Title slide — Properties of MLE: Uncertainty in Parameters

Welcome back to Module 3 — this is Lecture B, Properties of the MLE. In Lecture A we derived the maximum-likelihood estimate and found it was just least squares, re-earned from a model. Today we put that estimate on trial and ask three hard questions about it: is it unique, is it unbiased, and how uncertain is it? Three questions, three properties. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Three things by the end of this lecture, one per property. First, show the MLE is unique — that the log-likelihood has a single maximum, which comes down to its Hessian being negative definite everywhere. Second, state precisely what unbiasedness of w-hat does and doesn't mean — there are a few tempting claims it is not. And third, quantify the uncertainty in w-hat, using its covariance and the Fisher information. One heads-up worth flagging now: the closed-book checkpoint gates on reproducing the first two of these — uniqueness and unbiasedness — from scratch. So those two arguments are the ones to really own.

## Recap: likelihood and the MLE

Quick recap from Lecture A. We wrote the linear-Gaussian likelihood — the product over all N patients of a normal density, each one centered on the line w-transpose x-n with variance sigma-squared. Maximizing it handed us two estimates: w-hat equals X-transpose-X inverse, times X-transpose y — the normal equations — and sigma-squared-hat, the average squared residual at the fitted line. So we have the estimator in hand. Today is the honest follow-up: how good is it? Is w-hat unique, is it unbiased, and how much would it wobble if we'd happened to collect a different sample of patients?

## Section — Unique, unbiased, and how uncertain.

So — unique, unbiased, and how uncertain. Let's take those one at a time.

## Property 1 · Uniqueness

First, uniqueness: is there one best w-hat, or could there be a whole ridge of equally good answers? Start from the log-likelihood, script-l of w — again keeping the fancy L reserved for losses only.

> [cue: first fragment reveals]

Take its gradient with respect to w. It's one over sigma-squared, times X-transpose-y minus X-transpose-X-w — and that vanishes exactly at the normal equations. So the peak sits right where we said it did.

> [cue: second fragment reveals]

Now the second derivative — the Hessian. It comes out constant: minus one over sigma-squared, times X-transpose-X. And it's negative definite — sandwich it between any nonzero vector v and you get something strictly negative. A negative-definite Hessian everywhere means the surface is strictly concave: one hump, no ridges, no second peak. So the maximum is single, and it's global.

> [cue: third fragment reveals]

And notice what's carrying the whole argument — the same X-transpose-X, full column rank, that guaranteed a unique solution back in Module 1. It's back, this time wearing the name "negative-definite Hessian." Same condition, same matrix, new costume.

## The generative picture

Before we ask whether w-hat is unbiased, we need the right mental picture — and it's a generative one. Here's the process. On the left, the true weights and the true sigma-squared are fixed, but unknown to us; they generate data — y-n equals w-transpose x-n plus Gaussian noise.

> [cue: fragments reveal stage by stage]

Run that process once and you get one dataset, D — N draws — and fitting it gives one estimate, w-hat. Now run it again, and again: repeated datasets, D-one, D-two, and so on, each producing its own w-hat. Those estimates don't all land in the same spot — they scatter into a cloud. And the spread of that cloud is exactly the covariance of w-hat. Hold that image, because it's the whole game: uncertainty in w-hat is the spread of estimates you'd get across the datasets you didn't collect. Everything on the next few slides is about pinning that spread down with a formula instead of a picture.

## Expectation — a reminder

> [cue: optional — cut if running long; nothing downstream depends on it]

One-slide reminder before we start taking expectations. For a random vector x with density p, the expectation of a function f is just its probability-weighted average — the integral of f times p. The mean is the expectation of x itself; the covariance is the expected outer product of the centered vector — x minus mu, times its own transpose. That's all we need — linearity of expectation and that covariance definition — to get through the next two slides.

## Property 2 · Unbiasedness

Second property — unbiasedness. Take the expectation of w-hat across datasets from the generating process. The key move: only y is random here. The design matrix X is fixed — it's the same patients' ages every single time.

> [cue: first fragment reveals]

So pull that constant matrix straight out front — the expectation of w-hat is X-transpose-X inverse, X-transpose, times the expectation of y.

> [cue: second fragment reveals]

But the model tells us the expected value of y is X-w — the line is the mean. Substitute that in, and you get X-transpose-X inverse, times X-transpose-X, times w.

> [cue: third fragment reveals]

That inverse cancels its own matrix, and you're left with just w. So on average, across all those datasets, w-hat lands right on the true w. It's unbiased.

## What "unbiased" means — and doesn't

Now be careful — this is the slide students misremember. Unbiased means one specific thing: across many size-N samples from the process, the collection of w-hats is centered on the true w. That's it — a statement about the average. It is not the same as three things it's tempting to confuse it with. It's not the claim that more data gives better estimates — true here, but that's a separate sample-size effect, not what unbiasedness asserts. It's not the stronger UMVU property — minimum variance among unbiased estimators — because being centered doesn't mean being tightest. And it's not a promise that w-hat is best for your one dataset; in fact, a biased estimator can land closer to the truth from less data. Unbiasedness is about the center of the cloud, not any single point in it.

## Property 3 · Covariance

Third property — and here's where we finally put a number on the wobble. The punchline first, in the box: the covariance of w-hat equals sigma-squared, times X-transpose-X inverse. Read it for intuition. Small sigma-squared — low noise — gives tight estimates. A large, well-conditioned X-transpose-X — more data, spread more widely — also gives tight estimates. So less noise and more, better-spread data both sharpen w-hat, exactly the way your gut says they should. The full derivation is worked line by line in the covariance appendix if you want to see every step.

## Fisher information

And there's a deeper name for this quantity. The Fisher information is the expected curvature of the log-likelihood — the expected value of the negative second derivative. Work it out and it's one over sigma-squared, times X-transpose-X — which means the covariance of w-hat is simply the inverse of the Fisher information. Curvature and uncertainty are inverses of each other: a sharply curved peak pins the parameters down tightly; a flat one leaves them loose. Read the matrix entry by entry — the diagonal tells you how much information you have about each parameter on its own, and the off-diagonal tells you how much a pair of parameters share, how much their estimates trade off against each other. More information, smaller inverse, tighter covariance.

## Parameter uncertainty on NHANES

Let's see it on real data. Two panels. On the left, the familiar picture — systolic blood pressure against standardized age, with the least-squares line running through it. On the right is the parameter plane itself: intercept w-zero on one axis, slope w-one on the other, with the covariance drawn as an ellipse. And there are two ellipses. The wide, dashed orange one comes from a small sample — just forty patients. The tight, solid green one comes from the full sample of thousands. Same formula both times, sigma-squared-hat times X-transpose-X inverse — the only thing that changed is N. And you can watch the payoff of data directly: the ellipse collapses. Forty patients leaves you a big, fuzzy region of plausible slopes and intercepts; the full sample squeezes it down to a small, confident blob.

## Live demo: the parameter-uncertainty explorer

Let's make that happen live, together. The tool on this slide is the generative picture from earlier, turned into something we can drive — data space on the left, parameter space on the right. I'll hit "Draw one dataset": one sample of patients appears on the left with its fitted line, and on the right, a single orange dot lands in the parameter plane — that's one w-hat. Now the fast way to build the cloud — "Draw one hundred." Watch the right panel flood with orange dots, and look at where they land: right inside the green dashed ellipse, the two-sigma theoretical covariance we just derived, all of them clustered around the purple diamond — the true w. That clustering on the diamond is unbiasedness, made visible. And keep an eye on the readout underneath: the empirical standard deviation of w-hat-one is closing in on the theory value, sigma over root-S-z-z — the formula and the simulation agreeing in real time. Now let me push the noise slider up. Notice the cloud clears and the ellipse redraws larger; draw another hundred and the estimates scatter wider — more noise, more uncertainty, bigger ellipse. Slide the sample size up instead and the whole thing snaps tight. The ellipse isn't a formula on a slide anymore — it's the shape your estimates actually make.

> [cue: interact directly on the full-bleed slide — Draw one → Draw 100 → nudge the σ or N slider and Draw 100 again; the covariance-ellipse figure on the previous slide is the PDF fallback if the embed can't load]

## Through-line

Step back and watch one object do three jobs, three modules apart. In this lecture, the negative-definite Hessian gave us uniqueness. That same curvature, in expectation, is the Fisher information — one over sigma-squared, X-transpose-X. And in Module 5, when a closed form is no longer available to us, the Laplace approximation's posterior covariance will turn out to be exactly this inverse Fisher information — H-inverse. Same X-transpose-X, same inverse, doing uniqueness here and uncertainty two modules from now. When that callback lands in a few weeks, I want you to feel it click.

## Recap + checkpoint preview

To recap — three properties of the linear-Gaussian MLE. It's unique, because the Hessian, minus one over sigma-squared times X-transpose-X, is negative definite. It's unbiased — the expectation of w-hat is the true w. And it's uncertain, but quantifiably so — the covariance of w-hat is sigma-squared times X-transpose-X inverse, which is the inverse Fisher information. And one last thing, because it matters: the closed-book checkpoint for this part of the course gates on the first two. You should be able to reproduce the Hessian-sign argument for uniqueness, and the three-line unbiasedness derivation, completely unaided. Drill those two until they're automatic.
