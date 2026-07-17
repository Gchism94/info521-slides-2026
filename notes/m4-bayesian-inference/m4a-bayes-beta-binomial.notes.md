---
title: "Priors, Posteriors & the Beta–Binomial"
module: "Module 4 · Lecture A"
source_script: scripts/m4-bayesian-inference/m4a-bayes-beta-binomial.script.md
reading_time_min: 7
---

# Module 4 · Lecture A — Priors, Posteriors & the Beta–Binomial

Module 3 measured uncertainty by imagining repeated datasets, with the parameter a fixed unknown. Bayes flips what is random: keep the one dataset you have, and treat the **parameter itself** as uncertain — a distribution updated by evidence.

## Bayes' rule

$$p(\theta\mid\mathcal{D}) \;\propto\; p(\mathcal{D}\mid\theta)\,p(\theta)
\qquad(\text{posterior} \propto \text{likelihood} \times \text{prior}).$$

The **prior** is belief before the data; the **likelihood** is the same Module 3 object; the **posterior** is belief after. Frequentist and Bayesian differ only in what is random — the estimate versus the belief about the parameter — and share the likelihood. The running question: what fraction $\theta$ of adults are hypertensive? Each screened patient is a Bernoulli draw, so after $N$ patients with $n_1$ positives the likelihood is binomial in shape, $\theta^{n_1}(1-\theta)^{n_0}$. The full-NHANES answer is $\theta \approx 0.388$.

## The Beta prior and conjugacy

A prior for a proportion lives on $[0,1]$; the **Beta** family fits, with parameters $a, b$ read as **pseudo-counts** ("as if I had already seen $a{-}1$ positives and $b{-}1$ negatives"). $\mathrm{Beta}(1,1)$ is flat — total ignorance.

The key mechanism is **conjugacy**: multiplying the Beta prior by the binomial likelihood adds the exponents, so

$$\mathrm{Beta}(a,b) \;\xrightarrow{\;n_1\text{ ones},\ n_0\text{ zeros}\;}\; \mathrm{Beta}(a+n_1,\; b+n_0).$$

The posterior stays in the family, and updating collapses to arithmetic: count successes, add to $a$; count failures, add to $b$. Watching real NHANES draws, the posterior narrows around 0.388 as patients accumulate; and three very different priors converge to nearly the same posterior after 200 patients — priors matter most when data are scarce, but enough evidence washes them out. A bad prior delays convergence, it does not destroy it.

## What the posterior buys

The posterior is a complete answer. A **point estimate** is its mean $\tfrac{a+n_1}{a+b+N}$ (or mode); an **error bar** is a 95% **credible interval** read off the density (there is a 95% probability $\theta$ lies in it — what people wish a confidence interval meant). The mean is a weighted **blend** of prior mean and sample frequency, with the data's weight approaching 1 as $N$ grows. Prediction integrates over parameter uncertainty (the **posterior predictive**) rather than plugging in a point estimate; with a flat prior this is Laplace's rule of succession, $\tfrac{n_1+1}{N+2}$, never exactly 0 or 1.

The Beta–Binomial explorer lets you set the prior $(a,b)$, add "positive" and "negative" patients one at a time, and watch the posterior mean and variance update while the posterior curve shifts.

## What to remember

- Posterior $\propto$ likelihood $\times$ prior; Bayes makes the *parameter* the random object.
- Beta–Binomial conjugacy makes the update pure addition on the pseudo-counts.
- One posterior yields point estimates, credible intervals, and predictions.
- Priors dominate when data are scarce and fade as evidence accumulates.

## Through-lines

Everything here is one-dimensional by design. Lecture B runs the same conjugate trick on the *regression weights* — a Gaussian prior meets a Gaussian likelihood — and that closed form is where Project 1 ends.
