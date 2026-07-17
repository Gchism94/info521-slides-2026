---
deck: "Approximate Inference & Bayesian Classification"
subtitle: "INFO 521 · Module 5 · Lecture A — Breaking Conjugacy: Logistic Regression & Newton's Method"
source_qmd: modules/m5-approximate-inference/m5a-logistic-newton.qmd
dest: scripts/m5-approximate-inference/m5a-logistic-newton.script.md
scenes: 12
est_spoken_words: 1414
est_runtime_min: 10.9   # at ~130 wpm
---

## Title slide — Approximate Inference & Bayesian Classification

Welcome to Module 5 — Approximate Inference and Bayesian Classification, Lecture A: breaking conjugacy, with logistic regression and Newton's method. This is the second act of the course. Module 4 ended on a cliff edge — everything was Gaussian, every formula closed-form, and I promised that would break. Today it breaks. We ask a genuinely clinical question — is this patient hypertensive? — and the moment we binarize that outcome, the beautiful closed-form Bayes of last week is gone. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four outcomes. First, explain why binarizing the outcome breaks conjugacy — and exactly what dies with it. Second, state the logistic regression model and its log-likelihood. Third, show there's no closed form for the fit — and that this is structural, not just harder algebra. And fourth, run Newton–Raphson: gradient, Hessian, update, and read its convergence. This is where Project 2 begins — same patients, same NHANES, but a yes-or-no label.

## Project 2 opens here: binarize the outcome

Module 4 closed with everything Gaussian and every formula closed-form. Now we ask the clinical question instead: is this patient hypertensive? — a zero or a one, by the same rule as last week, systolic at least 130 or diastolic at least 80, measured blood pressure only.

> [cue: first fragment reveals]

The target is now a Bernoulli outcome, not a Gaussian one — each patient is a coin flip whose probability of coming up hypertensive depends on their features.

> [cue: second fragment reveals]

And here, in the accent color, is the whole hinge of the course. A Gaussian prior on the weights now meets a Bernoulli likelihood — and there is no conjugate pair for that combination. The tidy closed-form posterior of Module 4 is gone. This is the conjugacy-break the entire course was built around: same data, same thirty-nine percent prevalence, but the algebra that made Bayes easy is now structurally unavailable.

## The model: squash the line

So how do we model a probability with a linear score? Keep the score — w-transpose x, exactly as always — but squash it through the sigmoid, that S-shaped function that takes any real number and returns something between zero and one. Look at the curve: far left it sits near zero, far right near one, and it crosses one-half right at a score of zero. So the probability a patient is hypertensive is the sigmoid of their linear score. Two things to hold onto. It's still linear in w inside the squash, so all our basis-function machinery from Module 1 still applies. And it's discriminative — we model the probability of the label directly, and never bother modeling the features themselves. The decision boundary, where the score is zero, is still a straight line in feature space. "Linear model" survives binarization.

## The log-likelihood

Now write the likelihood. Independent patients multiply, so take the log and you get the sum over patients of the familiar cross-entropy — y log mu, plus one-minus-y log one-minus-mu, where mu is the sigmoid of the score. To fit, do what we always do: set the gradient to zero. And the gradient is gorgeous — X-transpose times y minus mu, the design matrix times the residual between the labels and the predicted probabilities.

> [cue: fragment reveals]

It looks exactly like the normal equations from Module 1. But look closer — mu hides w inside the sigmoid, that nonlinearity. There is no way to isolate w and solve for it. And this isn't harder algebra, it's the accent-colored punchline: no closed form exists at all. The equation is transcendental. In Module 1 we could solve; here we simply cannot. So we iterate.

## Newton–Raphson: use the curvature

Newton–Raphson is the iteration, and it's smart about it. Instead of stepping uphill blindly, at each point it builds the local quadratic approximation to the log-likelihood and jumps straight to that quadratic's peak. The update uses two things: the gradient, which says which way is up, and the Hessian, the matrix of second derivatives, which says how the slope is curving — one linear solve per step, and no step size to tune. And here's a callback. That Hessian is minus X-transpose-R-X, where R is a diagonal reweighting by each patient's uncertainty, mu times one-minus-mu. It's negative definite, so the log-likelihood is concave — one peak, and Newton finds it. That's m3b's uniqueness argument all over again: X-transpose-X has just become X-transpose-R-X. And notice who gets the most weight in R — the fence-sitters, patients near probability one-half, right at the boundary. They're the ones who actually tell you where the line goes.

## Newton on NHANES: five steps to the answer

Let's run it on all five thousand real patients. Left panel: the log-likelihood climbing as Newton iterates — and look how fast, it's essentially flat by the third step. Right panel: the two weights, intercept and slope, snapping to their final values in about five iterations, to machine precision. The fitted slope is about zero-point-five-two, and here's the clinical read: each standard deviation of age — roughly seventeen years — multiplies a patient's odds of hypertension by e-to-the-point-five-two, about one-point-seven. Age is a real, sizeable risk factor, and now it's quantified.

## The fitted curve on the data

And here's the fitted model against the data. The blue dots are patients, their zero-one labels jittered so you can see the density; the vermillion curve is the fitted sigmoid, rising with age. Now the honest check — those green diamonds are the empirical hypertension rate within each age decile, computed with no model at all, and the sigmoid tracks them closely. That's the curve earning its keep. And the dotted line marks where the predicted probability crosses one-half — around standardized age zero-point-nine-four, which back-transforms to about sixty-six years. A memorable clinical anchor: somewhere past the mid-sixties, the model tips over toward predicting hypertension.

## Live demo: the logistic + Newton explorer

Let's get hands-on. The tool frames this as a different clinical classifier — each point is a tumor, its size across the bottom, colored benign or malignant — but it's the exact same logistic model underneath. Two sliders: the bias, which shifts the S-curve left and right, and the steepness, which sets how sharply it flips from benign to malignant. As you drag them, you're hand-placing the decision boundary, and the readouts respond live — the threshold size where probability crosses one-half, the log loss, and the accuracy. Try to fit it by eye first, and watch the log loss drop as you improve. Then click "Show MLE fit" — that snaps the curve to the maximum-likelihood solution, the very answer Newton computed for us on the blood-pressure data. And "Generative comparison" overlays a different approach — a Gaussian model per class — and shows it landing on essentially the same boundary, a nice reminder that discriminative and generative can meet. "Reset" puts it all back.

> [cue: interact directly on the full-bleed slide — drag Bias and Steepness to fit by eye (log loss drops) → Show MLE fit → Generative comparison → Reset; the Newton-convergence snapshot on the next slide is the PDF fallback if the embed can't load]

## Explorer — static fallback

For print or PDF, or if the embed doesn't load, this snapshot stands in — the Newton log-likelihood convergence on the NHANES hypertension model, climbing to its plateau in a handful of steps. Live in class, we drive the explorer itself on the slide before; there's nothing new to learn here.

> [cue: optional — skip aloud if the live embed worked; this slide exists only for print and PDF]

## What we have — and what we lost

Let's take honest stock — what survived binarizing, and what didn't. On the plus side, the whole frequentist story is intact: we get w-hat by Newton, we know it's unique because the log-likelihood is concave, and we can even get m3b-style uncertainty from the curvature at the peak. But the Bayesian story took the hit. The posterior over the weights is still proportional to the likelihood times the prior — we can evaluate it at any point we like — but we cannot normalize it, because that evidence integral has no closed form. So exact credible intervals and honest predictive probabilities are out of reach. Here's the asymmetry, in the accent color: optimization survived, integration did not. Finding the peak took five Newton steps. Knowing the mass around it — that's the hard part, and it's the whole job of Lecture B.

## Recap & bridge

Quick recap. Binarize the outcome and conjugacy breaks: a Bernoulli likelihood with a Gaussian prior has no closed-form posterior — that's Project 2's opening move. Logistic regression squashes the linear score through a sigmoid, its log-likelihood is concave, and its gradient is X-transpose times the label residual. Newton–Raphson climbs it in about five steps by using the curvature. And here's the bridge, in the accent color: that Hessian Newton computed at the peak is about to become the covariance of a Gaussian approximation to the posterior. Lecture B starts by reusing exactly what we just built — approximating the posterior we can't normalize, first with a Gaussian at the peak, then with samples.
