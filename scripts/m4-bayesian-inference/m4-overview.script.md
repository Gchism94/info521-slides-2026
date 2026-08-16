---
deck: "Module 4: Bayesian Inference"
subtitle: "INFO 521 · Module 4 · Overview"
source_qmd: modules/m4-bayesian-inference/m4-overview.qmd
dest: scripts/m4-bayesian-inference/m4-overview.script.md
generated_from: overviews/module_spec.py + overviews/narration.py
scenes: 6
est_spoken_words: 315
est_runtime_min: 2.4   # at ~130 wpm
---

## Title slide — Module 4: Bayesian Inference

Module 4. We go Bayesian, and for two weeks the algebra is unusually kind to us.

## The question

The question is what you should believe about a parameter before and after seeing data. Module 3 gave you a single best estimate with an error bar. Here the point estimate is replaced by a distribution that you update as evidence arrives.

## What the lectures do

Lecture A works the Beta-Binomial pair on hypertension prevalence. The headline is conjugacy: when the prior and likelihood are matched, updating the posterior is addition. You count successes, you count failures, you add. You also see how fast the prior stops mattering as data accumulates. Lecture B does the same thing for the regression weights, watches the posterior contract, and shows ridge regression reappearing as nothing more than a Gaussian prior.

## Where this sits

That ridge result is worth pausing on. In Module 2 it was a penalty you add because it works. Here it falls out of taking the probability model seriously. That keeps happening once you commit to the model. Module 5 then breaks the conjugacy that makes all of this closed form.

## Week 4 at a glance

Homework Unit 4, checkpoint quiz 1.3 on the conjugate posterior, and Milestone 1.2 is due. The activity loop is the Bayesian-updating explorer, which is the fastest way to build intuition for how the prior loses its grip. Push the sample size up and watch a strong prior and a weak one land on the same answer. That picture is worth more than the algebra for most people.

## Watch out for

The MAP is not the posterior. It is the single highest point of it, and reporting it alone throws away the spread, which was the reason for going Bayesian. And remember that conjugacy is a convenience, not a law. It holds for the pairs in this module and fails the moment the likelihood changes shape, which is exactly what happens next week. Enjoy the arithmetic while it lasts.
