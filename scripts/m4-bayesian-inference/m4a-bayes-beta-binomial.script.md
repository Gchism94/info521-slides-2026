---
deck: "Bayesian Inference"
subtitle: "INFO 521 · Module 4 · Lecture A — Priors, Posteriors & the Beta-Binomial"
source_qmd: modules/m4-bayesian-inference/m4a-bayes-beta-binomial.qmd
dest: scripts/m4-bayesian-inference/m4a-bayes-beta-binomial.script.md
scenes: 14
est_spoken_words: 1623
est_runtime_min: 12.5   # at ~130 wpm
---

## Title slide — Bayesian Inference

Welcome to Module 4 — Bayesian Inference, Lecture A: priors, posteriors, and the Beta-Binomial. Here's the shift. Module 3 gave us uncertainty by imagining repeated datasets. Today we change what's random: we keep the one dataset we actually have, and treat the parameter itself as uncertain — a distribution over what it might be, updated by evidence. We'll do it on the cleanest possible question, a single proportion, and watch belief converge patient by patient. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four outcomes. First, state Bayes' rule for a parameter and name every term in it. Second, choose and read a Beta prior for a proportion. Third — and this is the mechanical heart of the lecture — perform the conjugate update by hand: a Beta prior plus binomial data gives a Beta posterior. And fourth, say what a posterior buys you that a single point estimate never can. The running question all lecture: what fraction of U.S. adults are hypertensive? Same NHANES data as always, brand-new epistemics.

## From "how uncertain?" to "what do we believe?"

Let's be precise about what's changing. In Module 3 we measured uncertainty by imagining repeated datasets — w-hat scattered into that covariance ellipse, but the true parameter stayed a fixed unknown out there. The randomness lived in the estimate.

> [cue: first fragment reveals]

Bayes flips the object of study. Keep the one dataset you actually collected — you're not imagining others — and instead treat the parameter itself as uncertain: a full probability distribution over what it might be, that you update as evidence comes in.

> [cue: second fragment reveals]

So here's the honest framing — and it's not a holy war. Frequentist: the estimate is the random thing. Bayesian: the belief about the parameter is the distribution. And notice both camps use the exact same likelihood — that Module 3 object, unchanged. In fact, in Lecture B, the Module 3 ellipse comes back to us literally as a Bayesian posterior.

## Bayes' rule, term by term

Bayes' rule, and you should be able to label all four pieces cold. On the left, the posterior — belief about the parameter after seeing the data. It equals, on top, the likelihood times the prior; on the bottom, the evidence. The prior is what you believed before this dataset. The likelihood is that Module 3 object again — how probable the data is at each parameter value. The evidence on the bottom is just a normalizing constant for today; it comes back with a vengeance in Lecture B. And the working form, the one you'll actually use: posterior is proportional to likelihood times prior. The denominator doesn't depend on the parameter, so we ignore it and just normalize at the end.

## The running question: hypertension prevalence

Let's make it concrete. We screen adults one at a time and record whether each is hypertensive, using the clinical rule — systolic at least 130, or diastolic at least 80. And notice that rule uses measured blood pressure only: it's the leakage-safe label Project 2 goes on to predict, the same discipline we set back in Module 1. Each patient is a coin flip — hypertensive is a one, not is a zero — a Bernoulli draw with unknown rate theta. After N patients with n-one positives, the likelihood takes the binomial shape: theta to the number of positives, times one-minus-theta to the number of negatives. The full NHANES answer, across all five thousand adults, is about thirty-nine percent. Today we watch belief climb toward that, one patient at a time.

## The Beta prior

A prior for a proportion has to live between zero and one, and the Beta family is built for exactly that. Two shape parameters, a and b, and the single most useful way to read them is as pseudo-counts. It's as if you'd already seen a-minus-one positives and b-minus-one negatives before the real data arrived. Look at the shapes on screen. Beta-one-one is flat — that's having seen nothing, total ignorance, a uniform prior. Beta-two-two is a gentle hump toward the middle. Beta-two-five leans skeptical, betting theta is low. And Beta-twenty-thirty is sharp and confident, already sure the answer's near zero-point-four. More pseudo-counts means a tighter, more opinionated prior.

## Conjugacy: the update is just addition

And here's the magic that makes this whole module tractable — conjugacy. Multiply the Beta prior by the binomial likelihood, and because both are just theta to some power times one-minus-theta to some power, the exponents simply add. Beta-a-b, updated with n-one ones and n-zero zeros, becomes Beta of a-plus-n-one, b-plus-n-zero. That's the whole update. When a prior family reproduces itself through the likelihood like this — the posterior stays in the same family — we call it conjugate, and updating collapses to exact arithmetic. In the accent color, the entire computation: count your successes, add them to a; count your failures, add them to b. This little addition is the keystone the whole module is built on — and reproducing this derivation is exactly what the checkpoint asks of you.

## Watching belief converge

Let's watch it happen, on real NHANES screening draws — these aren't simulated; the counts in the legend are what actually came up. We start from the flat Beta-one-one prior, knowing nothing. After five patients: a wide, lumpy posterior — we've barely begun. After twenty: noticeably narrower, homing in. After two hundred: a sharp spike, sitting right on the true full-sample prevalence marked by the dashed line. Two things to notice as the patients pile up. The posterior gets narrower — uncertainty genuinely shrinks. And the peak wobbles around early, when data is scarce, then settles down as evidence accumulates. That's Bayesian learning, drawn on real data.

## Does the prior matter?

Reasonable worry: doesn't the answer just depend on which prior I happened to pick? Here's the honest test. On the left, three genuinely different priors — the flat one, a skeptical one betting low, and an over-confident one betting too high. On the right, all three after the same two hundred real patients — and they've basically collapsed onto the same posterior, all sitting on the true prevalence. Two lessons. Priors matter most when data is scarce — early on, they pull real weight. But given enough evidence, the likelihood dominates and washes the prior out. A bad prior delays convergence; it doesn't destroy it. To overrule a prior, you just need evidence in proportion to the pseudo-counts it claimed.

## Live demo: the Bayesian-updating explorer

Let's drive it ourselves. The tool runs this exact Beta-Binomial model — it's framed as coin tosses, so read each "heads" as a hypertensive patient and each "tails" as a normotensive one. Start by setting the prior: the boxes for parameter a and parameter b — leave them both at one for the flat, know-nothing prior. Now feed it patients. Click "Add heads" for a hypertensive screen, "Add tails" for a normal one, and watch three things move together: the observation count ticks up, and the posterior-mean and posterior-variance cards update live. On the main chart you can toggle three curves — the prior, the previous posterior, and the current posterior — so you can literally see each patient nudge the belief along. And keep an eye on the two little tracking plots underneath: posterior mean settling as tosses accumulate, and posterior variance sliding down — uncertainty shrinking in real time. "Reset" clears the patients and snaps you back to the prior. Then retype a and b to start from a confident prior instead, and watch how many patients it takes to move it.

> [cue: interact directly on the full-bleed slide — set a and b → Add heads / Add tails a few times (watch the mean and variance cards) → toggle Prior vs Current posterior → Reset; the sequential-updating snapshot on the next slide is the PDF fallback if the embed can't load]

## Explorer — static fallback

For print or PDF, or if the embed won't load, this snapshot stands in — the same sequential Beta updating, posteriors narrowing toward the full-sample prevalence after zero, five, twenty, and two hundred patients. Live in class, we drive the explorer itself on the slide before; there's nothing new to learn here.

> [cue: optional — skip aloud if the live embed worked; this slide exists only for print and PDF]

## What the posterior buys

So why carry a whole distribution instead of a single number? Because the posterior is a complete answer, and every summary you used to bolt on separately is now just a question you ask it. Want a point estimate? Take the posterior mean — a-plus-n-one, over a-plus-b-plus-N — or the mode. Want an error bar? Read a ninety-five percent credible interval straight off the density: there's a ninety-five percent probability the rate lies in this range, which is exactly what people wish a confidence interval meant. And shrinkage falls out in plain sight — the posterior mean is a weighted blend of the prior mean and the sample frequency, and as N grows the data's weight climbs toward one. That's the sensitivity story from Module 2, now as a single line of algebra.

## Predicting the next patient

One more thing the posterior gives us — an honest prediction for the next patient. Instead of plugging in a single best theta, we average the coin-flip model over the entire posterior. That's the posterior predictive, and because of conjugacy the integral is easy: the probability the next patient is hypertensive is just the posterior mean, a-plus-n-one over a-plus-b-plus-N. The point is that we integrate over our uncertainty in theta rather than pretending we know it exactly. And there's a lovely special case with the flat prior: n-one-plus-one, over N-plus-two — Laplace's rule of succession, which never lets you predict exactly zero or one from finite data. Hold onto this plug-in-versus-integrate distinction; it returns with real force in Lecture B, and it stops being free in Module 5.

## Recap & bridge

Quick recap. Bayes: posterior proportional to likelihood times prior — belief, updated. Beta-Binomial conjugacy: the update is just addition, Beta-a-b to Beta a-plus-n-one, b-plus-n-zero. And the posterior is one object that answers everything — point estimates, intervals, predictions. Everything today was deliberately one-dimensional, a single proportion. In Lecture B we run the very same conjugate trick on the regression weights — a Gaussian prior meets a Gaussian likelihood and gives a Gaussian posterior for w. That closed form is where Project 1 ends.
