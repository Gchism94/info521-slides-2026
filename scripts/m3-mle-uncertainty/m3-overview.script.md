---
deck: "Module 3: Maximum Likelihood and Parameter Uncertainty"
subtitle: "INFO 521 · Module 3 · Overview"
source_qmd: modules/m3-mle-uncertainty/m3-overview.qmd
dest: scripts/m3-mle-uncertainty/m3-overview.script.md
generated_from: overviews/module_spec.py + overviews/narration.py
scenes: 6
est_spoken_words: 358
est_runtime_min: 2.8   # at ~130 wpm
---

## Title slide — Module 3: Maximum Likelihood and Parameter Uncertainty

Module 3. This is the hinge of the course. If you only get one module fully solid, make it this one.

## The question

Two questions. Why squared error, which we have been using for two modules without justifying, and how sure are we about the weights we estimated. Both get answered by the same move: assume a model for the noise, write down the probability of the data you actually observed, and maximise it.

## What the lectures do

Lecture A does the derivation. Gaussian noise, the likelihood of the dataset, the log-likelihood, and then maximum likelihood for the weights turning out to be exactly the least-squares solution you already have. The loss was never arbitrary. You also get the noise variance estimated as part of the deal. Lecture B asks what kind of estimator you now hold: whether it is unique, whether it is unbiased, and how much it would move if you collected the data again.

## Where this sits

Before this module you minimise a loss because it seems reasonable. After it you write down a probability model and derive the loss. Everything from here runs on likelihoods, so it is worth doing this derivation until you can do it without notes. It is also the shortest path to understanding why so much of machine learning looks like optimisation. You are usually maximising a likelihood wearing a different hat.

## Week 3 at a glance

Homework Unit 3, checkpoint quiz 1.2 on maximum likelihood, and Milestone 1.1 is due. There is no activity loop this week. The parameter-uncertainty demo is used live in Lecture B rather than as a peer loop, so the discussion carries the week on its own.

## Watch out for

Unbiased does not mean close. It means centred on the truth across repeat experiments you will never run. Your one estimate can still be far off, and the covariance is what tells you how far. Also, the maximum likelihood estimate of the noise variance is biased. It divides by N where the unbiased version divides by N minus the number of parameters. Lecture A shows you the bias rather than hiding it. The same correction turns up any time you estimate a spread from data you also used to estimate a centre.
