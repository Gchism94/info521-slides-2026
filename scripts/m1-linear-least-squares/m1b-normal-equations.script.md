---
deck: "Linear Models & Least Squares"
subtitle: "INFO 521 · Module 1 · Lecture B — Normal Equations & Geometry"
source_qmd: modules/m1-linear-least-squares/m1b-normal-equations.qmd
dest: scripts/m1-linear-least-squares/m1b-normal-equations.script.md
scenes: 17
est_spoken_words: 1633
est_runtime_min: 12.6   # at ~130 wpm
---

## Title slide — Linear Models & Least Squares

Welcome back to Module 1 — this is Lecture B: normal equations and geometry. In Lecture A we set up the model and the loss and then left one thing unfinished: actually finding the best weights. Today we finish it. We derive the closed-form solution, we see the beautiful geometric picture behind it — least squares as a projection — and we end on the single condition that makes the answer unique, a condition that quietly returns in Module 3. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four outcomes. First, derive the closed form — scalar first, to build the intuition, then the matrix normal equations for w-hat. Second, see least squares as an orthogonal projection onto the column space of X, and meet the hat matrix that does the projecting. Third, extend the whole thing to basis functions — fit curves while staying, technically, a linear model. And fourth, state exactly when the solution is unique. Keep an eye on that last one — it's a thread we deliberately pick back up in Module 3.

## Recap (Lecture A)

One line of recap. From Lecture A we have a model — prediction equals w-transpose x — and a loss, the mean squared error, y minus X-w, squared and averaged. The question we left open is simply: which w makes that loss smallest? And here's the fact that makes it answerable — the loss is a smooth, convex bowl in w. One bottom, no other dips. So the minimum is wherever the ground goes flat: where the gradient is zero. Let's go set it to zero.

## Section — Solve it: set the gradient to zero.

So — let's solve it. Set the gradient to zero.

## The loss surface

> [cue: optional — cut if running long; nothing downstream depends on it]

Before any algebra, here's the thing we're about to solve, drawn as a landscape. Two axes — intercept and slope — and the color is the loss at each combination. It's one smooth basin, a single bowl, with a clear lowest point marked by the X. And that is the whole reason a closed form exists: one basin means one minimum, so we can find it by asking where the surface goes flat, rather than searching for it. File away that this really is the minimum — the fact that the bowl curves upward in every direction is a property we'll give a name to in Module 3, when curvature becomes the whole story.

## Scalar least squares: the closed form

Let's do it in one dimension first, where you can see every step — just an intercept and a slope, and the loss is the average squared residual.

> [cue: first fragment — intercept]

Set the partial derivative with respect to the intercept to zero, and it tells you the line runs through the means: w-nought-hat is y-bar minus the slope times x-bar.

> [cue: second fragment — slope]

Set the partial with respect to the slope to zero, and out drops the slope — the sum of the cross-deviations, over the sum of the squared x-deviations.

> [cue: third fragment — covariance over variance]

And read that last expression: it is just the covariance of x and y, over the variance of x. That's exactly the line you fit back in Lecture A — no matrices required. Now let's scale it up to many features.

## The gradient

Now all D features at once — and the scalar result turns into a single matrix equation. Write the loss in matrix form: y minus X-w, transposed, times itself, over N.

> [cue: first fragment — the quadratic form]

It's quadratic in w, so differentiating is clean.

> [cue: second fragment — the gradient]

The gradient comes out minus two over N, times X-transpose, times the residual y minus X-w. Remember this is a vector — one partial derivative per weight, stacked up. The matrix-calculus identities that get you to this line live in the appendix; for today, just take the result and keep moving.

## The normal equations

Now set that gradient to zero. The minus-two-over-N is just a nonzero scalar out front, so it drops away, and you're left with X-transpose times the residual equals zero — which rearranges to X-transpose-X, w-hat, equals X-transpose y. These are the normal equations: a D-by-D linear system whose solution is the best weights. Worth burning in — reproducing this exact move, gradient to zero to normal equations, is what the Project-1 checkpoint asks of you, closed-book.

## The solution

And solving that system, when X-transpose-X is invertible, gives the headline result — w-hat equals X-transpose-X inverse, times X-transpose y. One matrix expression, and it hands you the globally best weights in a single shot: no iteration, no learning rate, no tuning. One practical aside: on a computer you solve the linear system rather than literally forming that inverse — it's better conditioned and less work. The inverse is the math; solve is the recipe.

> [cue: fragment — scalar is the D = 1 case]

And those scalar formulas from a few slides back? They're just this result with D equal to one. Same object, smaller. The full vector-calculus derivation, every line of it, is in the matrix-calculus appendix if you want it.

## Closed-form fit on NHANES

Let's run it for real — all six features now, not just age. This plots each patient's predicted BP against their actual BP, and the dashed line is perfect prediction: where every point would land if the model were flawless. The cloud does tilt along that line — so the model has real signal — but there's wide scatter around it. And that's the honest verdict on a six-feature linear fit of blood pressure: useful, and clearly not the whole story. Hold that thought — how good is good enough, and how do we keep from fooling ourselves, is Module 2.

## Section — What least squares is doing: geometry.

So that's the algebra. Now the picture sitting underneath it — the geometry of what least squares is really doing.

## Least squares is a projection

Here's the geometry, and it's worth slowing down for. Picture a space with one axis per patient — so N dimensions. Your target y is a single point way out in that space.

> [cue: the schematic builds one stage at a time — plane, then y, then the projection, then the residual]

Every prediction you could possibly make, every X-w, lives inside a flat sheet — the column space of X, the span of your feature columns. And y almost never lies in that sheet. So least squares does the only sensible thing: it drops y straight down onto the sheet, and the shadow it casts — the closest point in the sheet to y — is the prediction, y-hat. What's left over, the residual, is the arrow from the sheet up to y, and it stands perpendicular to the sheet. In matrix terms that projection is the hat matrix — X, times X-transpose-X inverse, times X-transpose — symmetric, and idempotent, which just means project twice and nothing new happens. One naming note: this often gets written H, but we're saving H for the Hessian later in the course, so here we'll call it P.

## Algebra ⇔ geometry

And here's the payoff — the algebra and the geometry are literally the same statement. "The residual is perpendicular to every feature column" means each column of X, dotted with the residual, is zero — and that's exactly X-transpose r equals zero. Substitute the residual back in and it rearranges, right into X-transpose-X, w-hat, equals X-transpose y. The normal equations again. So the calculus you cranked through — set the gradient to zero — and the picture — drop a perpendicular onto the column space — were never two facts. They're one object, seen two ways.

## Beyond straight lines: basis functions

One more move, and it's a big one. Nothing ever forced our features to be the raw inputs. Replace each input with functions of it — say one, then x, then x-squared, and up — and fit weights on those instead. The model is still linear in the weights, so the exact same solution works: just swap X for the new feature matrix, capital Phi, and turn the same crank — w-hat equals Phi-transpose-Phi inverse, times Phi-transpose y. And that's the subtle point people trip on: "linear model" means linear in the weights, not linear in x. We can absolutely fit curves. But there's no free lunch — more flexibility means more room to overfit, and that trade-off is precisely Module 2.

## Polynomial basis: under- vs over-fit

Here's that tension, drawn. Same thirty patients, two fits. The straight degree-one line is too rigid — it misses real structure in the data, underfitting. The wiggly degree-nine curve does the opposite: it bends to chase individual points, threading through the sample almost perfectly. And your gut should distrust it immediately — hand it thirty new patients and it'll flail, because it fit the noise, not the trend. Somewhere between too stiff and too eager is the right amount of flexibility. Finding that spot, honestly and reliably, is the entire job of the next module.

## When is ŵ unique?

Last piece — is the answer even unique? The clean statement: w-hat is unique exactly when X-transpose-X is invertible, which happens exactly when X has full column rank. In plain terms, two conditions. No feature is a copy or a combination of the others — no perfect collinearity. And you have at least as many patients as features. If either fails, infinitely many weight vectors tie for best — the bowl has a flat trough instead of a single low point, a whole valley of equally good answers. Remember this condition. In Module 3 it comes back wearing a different name — a negative-definite Hessian — and uniqueness turns into curvature. Same X-transpose-X, doing the same job, four weeks apart.

## Recap & checkpoint preview

To recap — least squares in closed form, three beats. One: the normal equations, X-transpose-X w-hat equals X-transpose y, straight from setting the gradient to zero. Two: geometrically, y-hat is the orthogonal projection of y onto the column space, and the residual is perpendicular to it. Three: the solution is unique when X has full column rank. And the checkpoint flag — the closed-book Project-1 checkpoint gates on you reproducing that gradient-to-w-hat derivation with no notes, so practice it cold. Next up is Module 2: we just watched flexibility turn into overfitting — now we learn to measure it and control it.
