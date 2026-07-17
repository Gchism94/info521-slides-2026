---
title: "Laplace Approximation & a Taste of Sampling"
module: "Module 5 · Lecture B"
source_script: scripts/m5-approximate-inference/m5b-laplace-sampling.script.md
reading_time_min: 7
---

# Module 5 · Lecture B — Laplace & Sampling

Lecture A left a posterior we can evaluate anywhere but cannot normalize. Two escape routes recover approximate inference: replace it with a Gaussian, or draw from it. The running example is deliberately small — 25 real NHANES adults — because at large $N$ every method agrees and there is nothing to see.

## Laplace: a Gaussian at the peak

Find the peak (the MAP, by Newton), Taylor-expand the log-posterior to second order there, and declare the quadratic exact. A quadratic log-density is a Gaussian, so

$$p(\mathbf{w}\mid\mathcal{D}) \approx \mathcal{N}\bigl(\hat{\mathbf{w}}_{\text{MAP}},\; \mathbf{A}^{-1}\bigr),
\qquad \mathbf{A} = \mathbf{X}^{\top}\mathbf{R}\mathbf{X} + \tfrac{1}{\tau^2}\mathbf{I}.$$

Two computable ingredients — a Newton fit and one matrix inverse — and all Bayesian machinery downstream reuses the Module 4 Gaussian formulas.

**The through-line closes here.** The curvature matrix $\mathbf{X}^{\top}\mathbf{R}\mathbf{X}$ is the observed Fisher information, and $\mathbf{X}^{\top}\mathbf{X}$ has now appeared four times: Module 1 (invertible $\Rightarrow$ unique $\hat{\mathbf{w}}$), Module 3 (the Hessian, and $\mathcal{I}^{-1} = \mathrm{Cov}[\hat{\mathbf{w}}]$), Module 4 (the data's precision in $\mathbf{S}_N^{-1}$), and Module 5 (the Laplace covariance$^{-1}$). One object — *curvature: how sharply the data pin the parameters down* — the whole course through.

Laplace is **local**: it matches the peak and its curvature and nothing else. On 25 patients the exact posterior for the age slope is skewed with a heavy upper tail, and the symmetric Gaussian misprices exactly there. It fails on skew and multimodality, but **sharpens with data** (posteriors Gaussian-ize as $N$ grows) — cheap and excellent at scale, risky at $N=25$.

## Metropolis: draw instead of describe

If we had samples $\mathbf{w}^{(s)} \sim p(\mathbf{w}\mid\mathcal{D})$, every integral would become an average — intervals from sample quantiles, predictions by averaging $\sigma(\mathbf{w}^{(s)\top}\mathbf{x}_*)$, no normalizer ever computed. **Random-walk Metropolis** draws them: propose a nearby move, and accept it with probability equal to the ratio of the (unnormalized) posterior at the two points. Because it is a ratio, the intractable normalizer **cancels**. Uphill moves are always taken, downhill moves sometimes — that "sometimes" is what makes it *explore* rather than *optimize*.

On the 25-patient cohort the trace is a stationary "hairy caterpillar" (good mixing), and the histogram of draws reproduces the exact skewed posterior — including the tail Laplace flattened — for free.

## Choosing

Laplace costs one Newton run and outputs a Gaussian; its error shrinks with **data**, and it fails on skew/multimodality. Metropolis costs thousands of evaluations and outputs draws; its error shrinks with **compute**, and it fails on poor tuning/slow mixing. Practically: **Laplace first**, sample when the answer matters in the tails — the two agreeing is itself evidence. (Three sampling knobs to know: burn-in, step size, and correlation between draws.)

## What to remember

- Laplace = $\mathcal{N}(\hat{\mathbf{w}}_{\text{MAP}}, \mathbf{A}^{-1})$ with $\mathbf{A} = \mathbf{X}^{\top}\mathbf{R}\mathbf{X} + \tau^{-2}\mathbf{I}$.
- It matches the peak but misses skew and multimodality; it improves with more data.
- Metropolis accepts on *ratios*, so the normalizer cancels; draws replace formulas.
- Assumptions (Laplace) vs compute (MCMC) is the trade.

## Through-lines

This closes the inference arc — loss → likelihood → posterior → approximation — around one recurring matrix. Modules 6–7 change the *question* (drop the labels), not the machinery.
