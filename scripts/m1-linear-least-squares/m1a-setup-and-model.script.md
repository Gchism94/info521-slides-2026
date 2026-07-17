---
deck: "Linear Models & Least Squares"
subtitle: "INFO 521 · Module 1 · Lecture A — Setup, Data, and the Linear Model"
source_qmd: modules/m1-linear-least-squares/m1a-setup-and-model.qmd
dest: scripts/m1-linear-least-squares/m1a-setup-and-model.script.md
scenes: 16
est_spoken_words: 1716
est_runtime_min: 13.2   # at ~130 wpm
---

## Title slide — Linear Models & Least Squares

Welcome to INFO 521 — this is Module 1, Lecture A: setup, data, and the linear model. This is the ground floor of the whole course. Today we frame the regression problem, meet the one dataset we'll live with all term — NHANES blood pressure — and write down the two pieces least squares is built from: a model and a loss. No solving yet; that's Lecture B. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four things to walk out with. First, frame supervised regression in our notation — what the inputs are, what the target is, and what exactly we're learning. Second, load and preprocess the NHANES data, and state the leakage rule for deciding which features are fair game. Third, define the linear model and the mean-squared-error loss — and compute that loss by hand. And fourth, fit a scalar least-squares line and read it back in clinical units. That's the arc for today: model, loss, and data. The closed-form solution and the geometry behind it are Lecture B.

## The course spine

Here's the shape of the whole term, on one slide. We have a single clinical outcome — systolic blood pressure — and we're going to look at it through four different lenses. Least squares first, this module: fit a line by minimizing squared error. Then maximum likelihood in Module 3 — the same fit, but earned from a noise model. Then the Bayesian view — carrying uncertainty instead of just a point estimate. And finally discovery — structure and labels we never handed the model. Same data every time, on purpose. So when something changes across modules, it's the method that changed, not the problem — you're building intuition on one clinical question.

## Supervised regression

Three flavors of machine learning, quickly.

> [cue: first fragment reveals]

Supervised learning: you learn from labeled examples — pairs of an input and a known answer. If the answer is a continuous number, that's regression; if it's a discrete label, that's classification.

> [cue: second fragment reveals]

Unsupervised: no labels at all — you're finding structure, like clustering or PCA. That's the back half of the term.

> [cue: third fragment reveals]

And reinforcement learning — learning from a reward signal. Out of scope for us.

> [cue: fourth fragment reveals]

So here's where we live for all of Module 1: regression is supervised learning with a continuous target. Given patients and their measured blood pressures, learn a function that predicts BP on a patient you haven't seen.

## Notation & data structures

Let's fix notation, because this is the spine for the whole term. One patient is a vector of features. Feed it to the model and you get one prediction — w-transpose x. Now stack the whole dataset: every patient's feature vector becomes a row of a big matrix we call the design matrix, X — N rows for N patients, D columns for D features. And all the targets stack into a single column vector, y. So rows are patients, and the target vector holds their blood pressures. One notation note you'll want early: we write targets as y — if you've seen Bishop's book using t for the target, that t is our y.

## The data — NHANES 2021–2022

Now the data itself. This is NHANES, 2021–22 — about five thousand one hundred U.S. adults, and the target is systolic blood pressure in millimeters of mercury. We're working with six leakage-safe features: age — our primary predictor for Project 1 — body-mass index, waist circumference, total cholesterol, HDL cholesterol, and HbA1c, a measure of blood sugar. Those six names aren't arbitrary; they're the loader's contract, the columns the data actually ships with. And notice one measurement that's deliberately missing from that list — diastolic blood pressure. That omission is the whole next slide.

## The leakage rule

Here's why diastolic isn't in the feature list — the leakage rule. Exclude any predictor that is itself a blood-pressure measurement, or that would trivially hand you the label. Diastolic BP co-measures the very same physiology as systolic — it's basically a peek at the answer — so we reserve it, and it's never a feature. And the key thing: this is a modeling choice we make by design, before we ever fit a line. It is not something the algorithm discovers for us. Flag this one now — it comes back in Project 2's cluster-versus-label reveal, and I want it to feel familiar when it does.

## A first look at the data

Let's actually look. Two panels. On the left is the distribution of the target on its own — systolic BP across all five thousand adults. It piles up around a hundred and twenty, and it's got a right skew: a tail of patients running high. On the right, that same blood pressure plotted against age — standardized here, so zero is the average age. There's a trend, and it slopes upward: older tends to mean higher BP. But look how much scatter sits around it — this is a real relationship, not a tight one. That cloud is exactly what a single line is going to have to summarize.

## The linear model

So here's the model we'll fit. Predict the target as a weighted sum of the features, plus an intercept — w-nought, plus w-one times x-one, on down the features. A little bookkeeping trick: we absorb the intercept by tacking a constant one onto every feature vector, so the whole thing collapses into a clean w-transpose x. Two things to read off the weights. w-nought, the intercept, is the prediction when every feature is zero. And each other weight is a per-unit effect — how much the prediction moves when you turn that one feature up by a unit and hold all the rest fixed.

## The loss: mean squared error

Now, how do we score a fit? With the loss — mean squared error. Take each patient's miss, the residual between the truth and the prediction, square it, and average over everyone. In matrix form that's one over N times the squared length of the residual vector, y minus X-w. Why squared? Two reasons for now. It's smooth — differentiable everywhere — which in Lecture B is exactly what lets us set a gradient to zero and solve in one shot. And it punishes big misses disproportionately, since the penalty grows with the square. One more thing to plant — and I'm flagging it in the accent color on purpose — a squared loss is also precisely what a Gaussian noise model gives you. That's a promise for Module 3, not something we cash today.

## Worked: compute ℒ by hand

Let's compute the loss once, by hand, on toy numbers — so it's concrete before it's abstract. Three points, and a guessed line: y-hat equals a half, plus x.

> [cue: first fragment — predictions]

Plug in the three x's and the predictions come out a half, one and a half, two and a half.

> [cue: second fragment — residuals]

Subtract those from the actual y's and you get the residuals: plus a half, minus a half, plus a half.

> [cue: third fragment — square and average]

Square each one — they're all a quarter — add them up, divide by three, and the loss is a quarter. That's the whole mechanic. Everything Lecture B does is find the w that drives this one number as low as it can go.

## A scalar least-squares fit

Here's the fit on real data — systolic BP against standardized age, with the least-squares line laid through it. Don't worry yet about how we found it; that's Lecture B. Just read what it says. The line slopes gently upward through the cloud — it's the single straight line that makes the squared-error loss as small as possible on this data. And the scatter around it is still enormous, which is honest: age moves blood pressure on average, but it doesn't pin down any one patient. Next slide, let's put actual numbers on that line.

## Interpreting the fit

Now the numbers — and the discipline of reading them in clinical units. The intercept is about a hundred and twenty-one and a half: that's the predicted BP at average age, where standardized age is zero, and it's a clinically sensible middle-of-the-road value. The slope is about six and a half — but six and a half per what? Per one standard deviation of age, which is roughly seventeen years. Convert it and that's about zero-point-four millimeters of mercury per year. Two sanity checks before you trust it: the sign is positive — BP rises with age, good — and the size is modest and plausible. Always translate a weight back into the units a clinician actually thinks in.

## Live demo: the least-squares explorer

Let's make this hands-on — this slide is the live explorer, and it's fully interactive. Each dot is a patient: age across the bottom, resting systolic BP up the side. There's a fit line you can grab by either endpoint and tilt, or nudge with the intercept and slope sliders underneath. As you move it, watch two things respond — the orange residual sticks stretching from each point to your line, and the "your loss" readout, the MSE, ticking up or down. Try to get it as low as you can by eye. Then hit "Show least-squares solution": the green dashed line is the true optimum, and the panel puts its MSE right next to yours, so you can see how close you got. Now the fun one — "Add outlier" drops a young patient with very high blood pressure into the corner, and watch the least-squares line swing toward it. That's squared error punishing one big miss — the outlier sensitivity we'll keep coming back to all term. "Reset" puts everything back.

> [cue: interact directly on the full-bleed slide — drag or slide to fit → Show least-squares solution → Add outlier (watch the line swing) → Reset; the static snapshot on the next slide is the PDF fallback if the embed can't load]

## Explorer — static fallback

If you're reading this in the PDF, or the embed didn't load, this snapshot stands in for it — the same scatter with the least-squares line, frozen in place. Live in class we drive the tool itself on the slide before; there's nothing new to learn here. It's just the print-safe version of the demo.

> [cue: optional — skip aloud if the live embed worked; this slide exists only for print and PDF]

## Recap & bridge

Quick recap. Least squares needs two ingredients, and we now have both: a model — prediction equals w-transpose x — and a loss — mean squared error, the average squared miss. That's it. What we don't have yet is the best w. So the entire job of Lecture B is optimization: set the gradient of that loss to zero, solve it in closed form, and get the famous w-hat equals X-transpose-X inverse, times X-transpose y — and then see the clean geometry hiding underneath it. Same model, same loss; next time, we actually solve.
