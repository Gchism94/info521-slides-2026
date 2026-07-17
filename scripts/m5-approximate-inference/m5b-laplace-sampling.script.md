---
deck: "Approximate Inference & Bayesian Classification"
subtitle: "INFO 521 · Module 5 · Lecture B — Laplace Approximation & a Taste of Sampling"
source_qmd: modules/m5-approximate-inference/m5b-laplace-sampling.qmd
dest: scripts/m5-approximate-inference/m5b-laplace-sampling.script.md
scenes: 13
est_spoken_words: 1490
est_runtime_min: 11.5   # at ~130 wpm
---

## Title slide — Approximate Inference & Bayesian Classification

Welcome back to Module 5 — Lecture B, the Laplace approximation and a taste of sampling. Lecture A left us stuck in a very specific way: we have a posterior we can write down and evaluate anywhere, but we cannot normalize it — and normalizing is exactly what Bayes needs. Today, two escape routes. Replace that posterior with a Gaussian — that's Laplace. Or stop describing it and start drawing from it — that's Metropolis. And along the way, a promise made back in Module 1 finally gets kept. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four outcomes. First, state the Laplace approximation — a Gaussian sitting at the MAP with the inverse Hessian as its covariance — and derive its two ingredients. Second, connect it to the through-line that's been running all term: curvature is Fisher information. Third, explain the Metropolis idea — why ratios of an unnormalized posterior are all you need — and read a trace plot. And fourth, choose between the two: speed versus faithfulness to the true shape.

## The problem, restated

Let's restate the problem cleanly. With a Gaussian prior on the weights, the posterior is the exponentiated log-likelihood times the prior, all over the evidence — and that evidence integral is intractable. We can evaluate the numerator at any w we want; we just can't integrate it. And integrals are precisely what Bayes runs on: normalizing, credible intervals, posterior predictives. In the accent color, today's running example is deliberately small — hypertension versus age on just twenty-five real NHANES adults. Why so few? Because with five thousand patients every method agrees and there's nothing to see. With twenty-five, they visibly disagree — and that's where approximation quality actually matters.

## Idea 1 — Laplace: a Gaussian at the peak

Idea one — Laplace, and it's beautifully pragmatic. Three moves. Find the peak: the MAP estimate, by Newton, exactly as in Lecture A but with one extra term from the prior. Then look at the curvature there — Taylor-expand the log-posterior to second order at the peak, where the linear term conveniently vanishes. And then just declare that quadratic exact. A quadratic log-density is a Gaussian, so the approximation is a Gaussian centered at the MAP, with covariance equal to the inverse of the curvature matrix. That's it — two computable ingredients, a Newton fit and one matrix inverse. And once you have a Gaussian, every Bayesian thing downstream reuses the Module 4 machinery.

## The through-line closes

Now I want to stop and make good on a promise, because this is one of my favorite moments in the course. For our model, that curvature matrix is X-transpose-R-X — the observed Fisher information — plus the prior precision. And look at where X-transpose-X has been. Module 1: X-transpose-X being invertible is what made the least-squares solution unique. Module 3: minus one-over-sigma-squared X-transpose-X was the Hessian, and its inverse was the covariance of w-hat. Module 4: one-over-sigma-squared X-transpose-X was the data's precision inside the posterior. And now, Module 5: X-transpose-R-X plus the prior is the inverse covariance of the Laplace approximation. Four modules, four names — loss curvature, Fisher information, posterior precision, Laplace covariance — and it was one object the whole time. Curvature: how sharply the data pin the parameters down. If you felt X-transpose-X haunting you all term, you were right to.

## Laplace vs. the exact posterior, on real patients

So how good is the Laplace Gaussian? Here's the test, and it's an honest one — because we only have two parameters, we can brute-force the exact posterior on a grid and normalize it for real. Blue is that exact posterior for the age slope; dashed vermillion is the Laplace Gaussian. Near the peak, they match beautifully — same location, same width. But look at the tails. The exact posterior is skewed, with a heavier upper tail, and the symmetric Gaussian can't follow it — it underprices the right tail and overprices the left. That skew is genuine posterior shape from twenty-five real patients, not an artist's flourish. Laplace nailed the center and missed the tails.

## When the peak isn't the story

And that points at exactly when Laplace fails, because Laplace is local — it sees the peak and the curvature there, and nothing else. Skew, like we just saw: the symmetric tails misprice probability right where the risk lives. Multimodality: a second peak somewhere else is completely invisible from the first one. But — and this is the fair scoreboard — Laplace sharpens with data. As N grows, posteriors Gaussian-ize, the same contraction we watched in Module 4, and Laplace converges on the truth: cheap and excellent at scale, risky at twenty-five. So here's what we'd really want, in the accent color: a method whose error shrinks with compute, not with assumptions.

## Idea 2 — don't approximate the shape; draw from it

Idea two, and it's a genuine change of philosophy. Suppose that instead of a formula for the posterior, we simply had samples from it — a big pile of plausible weight vectors, visited in proportion to their posterior probability. Then every integral Bayes needs becomes just an average over those samples. Credible intervals? Read them off as sample quantiles. Predictions? Average the sigmoid over the samples. And you never compute the normalizer at all. This is Monte Carlo — trade algebra for computation. The catch, of course: how do you draw samples from a distribution you can't even normalize?

## The Metropolis trick: ratios cancel the normalizer

Metropolis is the answer, and it turns on one clever trick. One step works like this. From wherever you currently are, propose a random nearby move — a little Gaussian hop. Then accept it with probability equal to the ratio of the posterior at the proposed point over the posterior at the current point, capped at one; otherwise, you stay put. And here's the magic: it's a ratio, so the intractable normalizer — the same value top and bottom — cancels completely. You only ever need the unnormalized posterior, the thing we can actually evaluate. Over many steps, the walk visits each region in proportion to its posterior mass. In the accent color: uphill moves are always taken, downhill moves are sometimes taken — and that "sometimes" is precisely what makes it explore the whole distribution instead of just climbing to the peak like Newton did.

## Metropolis on the real cohort

Here it is on our twenty-five patients. The left panel is the trace — the sampler's value for the slope over time — and what you want is exactly this: a fuzzy, stationary band with no trend and no getting stuck. People call it a hairy caterpillar, and that shape means it's mixing well. The right panel is the payoff: the histogram of all the draws, against the exact posterior in blue and the Laplace Gaussian in dashed vermillion. The draws trace the exact posterior — skew and all. The sampler captured the heavy tail that Laplace flattened, and it did it for free, with no Gaussian assumption. It just visited the distribution as it actually is.

## Practicalities, in one slide

> [cue: optional — cut if running long; nothing downstream depends on it]

If we have a minute, the three practical knobs. Burn-in: the early draws still remember where you started, so you throw them away — we dropped the first two thousand. Step size: too small and you inch along, covering the space slowly; too big and almost every proposal gets rejected; you tune for a moderate acceptance rate, very roughly a fifth to a half. And correlation: consecutive draws aren't independent, so your effective sample size is smaller than your number of draws — the fix is just more steps, which are cheap; pretending independence is the expensive mistake. Beyond this course there are smarter proposals that use gradients, multiple chains, formal diagnostics — but reading a trace and knowing those three knobs is the level we need.

## Choosing your approximation

So which do you reach for? A scoreboard. Laplace costs one Newton run; Metropolis costs thousands of evaluations. Laplace hands you a Gaussian and formulas; Metropolis hands you draws, and you compute averages and quantiles. Laplace's error shrinks with more data; Metropolis's shrinks with more compute. Laplace fails on skew and multimodality; Metropolis fails on bad tuning and slow mixing. The practical rule: reach for Laplace first — it's the fast workhorse — and pull out sampling when the answer matters out in the tails. And when the two agree, that agreement is itself evidence you can trust the result. Project 2 accepts either; what's graded is knowing which regime you're in, and saying why.

## Recap & bridge

To recap. Laplace: a Gaussian at the MAP, with covariance the inverse of X-transpose-R-X plus the prior precision — the Fisher through-line, finally closed. Metropolis: propose and accept on ratios, the normalizer cancels, and draws replace formulas. The trade is assumptions versus compute. And with that, the inference arc of the course is complete — we've gone from loss, to likelihood, to posterior, to approximation. In the accent color, what's next: Module 6 gives us one last supervised idea, the maximum-margin classifier, and then the big turn — unsupervised learning, finding structure with no labels at all. From here on we change the question, not the machinery.
