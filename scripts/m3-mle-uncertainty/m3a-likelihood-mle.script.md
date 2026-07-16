---
deck: "Likelihood & Maximum Likelihood"
subtitle: "INFO 521 · Module 3 · Lecture A — From Loss to Likelihood"
source_qmd: modules/m3-mle-uncertainty/m3a-likelihood-mle.qmd
scenes: 15
est_spoken_words: 1741
est_runtime_min: 13.4   # at ~130 wpm
---

## Title slide — Likelihood & Maximum Likelihood

Welcome to Module 3 of INFO 521 — this is Lecture A, Likelihood and Maximum Likelihood. Here's where we're headed: in Module 1 we picked squared error because it felt reasonable. Today we earn it — we build a probability model for the data, and the same fit falls right back out, now with a real foundation underneath it. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four things by the end of this lecture. First, state the linear-Gaussian noise model — and learn to read it generatively, as a recipe that produces data. Second, write down the likelihood and its logarithm, the log-likelihood. Third, derive the maximum-likelihood estimate for the weights — and show it's exactly the least-squares fit from Module 1. And fourth, estimate the noise itself, sigma-squared, and see why that estimate comes out biased. The through-line for the whole lecture: same fit as before, but a new foundation — and that foundation pays us back twice, with a noise estimate today and uncertainty in Lecture B.

## Why squared error? (the debt from Module 1)

Back in Module 1 we chose the mean-squared-error loss — one over N, times the squared length of the residual vector, y minus X-w. And we justified it with a bit of a shrug: it's smooth, it punishes big misses. Reasonable, sure. But it was a choice, and you took it on faith. Today we pay that debt back. Squared error isn't a preference we're stuck defending — it's what a Gaussian noise model implies, forced on us the moment we say the noise is bell-shaped. Remember that accent-colored hint on the loss slide back in m1a? This lecture is what it was pointing at.

## The noise model

Here's the model. Each patient's systolic blood pressure is the linear signal, w-transpose x-n, plus a noise term epsilon-n — and each noise term is drawn independently from a normal distribution with mean zero and variance sigma-squared. You can read that one equation two ways. Reading one: signal plus noise. Reading two, which is algebraically identical: each observation y-n is itself a draw from a Gaussian centered on the line, with spread sigma. That second reading is a generative story — fix the weights and sigma-squared, and the model can actually produce datasets. Hold onto that, because it's the picture the repeated-datasets schematic in Lecture B draws, and it quietly powers everything in this module.

## The Gaussian, in one slide

Quick refresher — most of probability review is async, but the Gaussian earns one slide here. The formula looks busy, but only two things in it matter today. The mean, mu, sets where the bell sits — it centers the curve. The standard deviation, sigma, sets how wide it spreads. And on the plot you can see the rule you already know: about sixty-eight percent of the probability falls within one sigma of the center, and about ninety-five percent within two sigma. Center and spread — that's the whole story, and it's all we'll need going forward.

## The likelihood

The patients are independent, so the probability of the whole dataset is just the product of the per-patient Gaussians — that big product from n equals one up to N. Now watch the shift in viewpoint.

> [cue: first fragment reveals]

The data, X and y, are fixed — they already happened, we're not touching them. The parameters — the weights and sigma-squared — are free; those are the knobs we turn. Read this way, that product becomes a function of the knobs. It scores them: parameters that make the data we actually observed more probable score higher.

> [cue: second fragment reveals]

So maximum likelihood is simple to say — turn the knobs until the data you actually saw is as probable as the model can make it. And one thing to burn in early: a likelihood is not a distribution over the parameters. That's Bayes, and it's Module 4. This is a score.

## The log-likelihood

Products of exponentials are miserable to work with, so we take a logarithm and get the log-likelihood — we'll write it script-l of w, keeping the fancy L reserved for losses only. The log does two nice things: it turns the product into a sum, and the exponential into the quadratic you already know. Written out, there are three terms — but only the last one depends on w.

> [cue: fragment reveals]

And look at that term. It's minus one over two sigma-squared, times the sum of squared errors. It is negative-sum-of-squared-errors, scaled. So maximizing the log-likelihood over w is exactly minimizing squared error — the argmax of script-l equals the argmin of the loss. You can see the equivalence before doing a single derivative; just point at that third term.

## The likelihood surface over NHANES

Let's actually look at it. This is the log-likelihood as we slide the slope parameter, w-1, holding the intercept fixed at its estimate. One smooth, concave arch — a single hump with one clear top. It's the mirror image of the convex loss bowl from m1b, flipped upside down: where the loss had its minimum, the likelihood has its peak. And that peak sits at a slope of about six and a half millimeters of mercury per standard deviation of age, marked by the vertical line. That number — six point five — is exactly the least-squares slope from m1a. Same spot. The two methods land on the identical answer, and now we know why.

## MLE for w: an old friend

Now let's make it exact. Take the gradient of the log-likelihood with respect to w and set it to zero. Because only that squared-error term carries any w, the gradient is one over sigma-squared, times X-transpose-y minus X-transpose-X-w. Set that to zero — and sigma-squared cancels completely; it's a nonzero factor out front, so it just drops away. What's left is X-transpose-X times w equals X-transpose-y — the normal equations. Solve them, and w-hat MLE equals X-transpose-X inverse, times X-transpose y. That is the Module 1 answer, letter for letter. Nothing new to memorize — the derivation is m1b's, wearing likelihood clothes. What's new is the interpretation: least squares is maximum likelihood under Gaussian noise. Same fit, better story — it comes from a model now, not a preference.

## Dividend 1: the noise gets estimated too

Here's the first payoff. The loss treated the scatter around the line as a nuisance — something to shrink and then ignore. The likelihood promotes it to a parameter we get to estimate. Set the derivative of the log-likelihood with respect to sigma to zero, and out drops sigma-squared-hat: the average squared residual at the fitted line — take each patient's residual, square it, average over everyone. For blood pressure on standardized age, sigma-hat comes out around sixteen millimeters of mercury. That's the model's honest give-or-take for a single patient. And clinically, that's the real punchline: age explains the trend across the population, but any individual patient still scatters plus or minus sixteen around the line. Age explains the trend — not the person.

## Model check: are the residuals Gaussian-ish?

We assumed Gaussian noise — so let's actually check that assumption. This is a histogram of the NHANES residuals, with the fitted Gaussian, mean zero and sigma about sixteen, laid over the top as the dashed curve. Through the bulk it's a decent match — roughly bell-shaped, centered where it should be. But look hard at the right tail: it's heavier than the Gaussian predicts. Those are the hypertensive spikes — patients running far above the line. So the assumption is useful, not true — and that phrase is going to follow us all term. Models are assumptions; you check them. And that heavy right tail? Binarizing it — normal versus high — is exactly what Project 2 and Module 5 go and do.

## Dividend 2 — with a catch: σ̂² is biased

Second payoff — but this one comes with a catch. If you average sigma-squared-hat over many datasets from the same generating process, you don't get the true sigma-squared back. You get N-minus-D over N, times sigma-squared — a little less than the truth. It under-estimates. Why? The fit chases the sample. w-hat is tuned to these exact patients, so the residuals measured around it come out systematically smaller than the true errors would. Each fitted parameter eats one degree of freedom — that's the D in N-minus-D. The classic repair divides by N-minus-D instead of N. With five thousand patients and two parameters, that correction is invisible; at N equals ten, it absolutely is not. And notice the contrast waiting in Lecture B, where w-hat turns out unbiased. Maximum likelihood doesn't hand you unbiasedness for free — you check it, estimator by estimator.

## Seeing the bias

And you can watch it happen — this is real NHANES data, no simulation. We draw small subsamples, refit, and record sigma-squared-hat, averaging over two thousand draws at each subsample size, from four patients up to sixty. The blue curve is that average. At the small sizes it sits well below the full-sample reference line — the estimate is genuinely too small. As the subsample grows, it climbs back up toward the truth. And it doesn't just climb vaguely — it rides the green theoretical curve, N-minus-two over N times sigma-squared, almost exactly. That's the bias formula from the previous slide, playing out in front of you on live data.

> [cue: gesture from the low left of the curve up toward the reference line]

## What maximum likelihood buys

Let's step back — one framework, three purchases. One: a principled loss. Squared error stopped being a matter of taste and became a consequence of Gaussian noise; change the noise model, and you change the loss. Two: noise as a first-class estimate. Sigma-squared-hat quantifies patient-level scatter — something the loss view had nowhere to put. Three: a road to uncertainty. The curvature of the log-likelihood at its peak — how sharp that arch is — tells us how tightly the data pin down w-hat, and that is the whole of Lecture B. Plus one honest caution: MLE estimators aren't automatically unbiased — sigma-squared-hat wasn't. Properties get checked, not assumed.

## Recap & bridge

To recap. We wrote a noise model — signal plus zero-mean Gaussian noise. We built its likelihood, and maximizing it turned out to be minimizing the Module 1 loss: least squares, re-earned from a model instead of a preference. And sigma-squared-hat came along for free — the average squared residual, biased by that N-minus-D over N factor. Next, in Lecture B: how uncertain is w-hat? The answer is the curvature of the log-likelihood — the Hessian — and it's going to be X-transpose-X yet again, this time wearing the name Fisher information. Keep your eye on that one matrix: it's the loss bowl in Module 1, the likelihood peak here, the Fisher information next, and the Laplace posterior in Module 5. Same object, the whole course through.
