---
layout: default
title: Distributions
---

{% include katex.html %}

## Useful Math Facts

### The Gamma Function
$\Gamma(\alpha)=\int_0^\infin{y^{\alpha-1}e^{-y}}dy$ for $a\ge0$

if $\alpha > 1$ then $\Gamma(\alpha)=(\alpha-1)\Gamma(\alpha-1)$

if n is a positive integer then $\Gamma(n)=(n-1)!$

$\Gamma(1)=1$

$\Gamma(1/2)=\sqrt\pi$

## Discrete
* Bernoulli(p)
    - flip a coin once;
    * = Binomial(1, p)
    - $p^x(1-p)^{n-x}$
    - $E(X) = p$
    - $V(X) = p(1-p)$
    - MGF = $pe^t+(1-p)$
* Binomial(n, p)
    - flip a coin n times.
    * X1 + X2 ~ Binomial(n1 + n2, p)
    - $\binom{n}{x}p^x(1-p)^{n-x}$
    - $E(X) = np$
    - $V(X) = np(1-p)$
    - MGF = $(pe^t+(1-p))^n$
* Geometric(p)
    - the number of flips needed until the first head when flipping a coin.
    - $p(1-p)^{x-1}I(x\ge 1)$
    - $E(X) = 1/p$
    - $V(X) = (1-p)/p^2$
    - MGF = $pe^t/(1-(1-p)e^t)$ with $t<-log(1-p)$
* Poisson(λ)
    - counts of rare events like radioactive decay and traffic accidents;
    - can be deduced from Binomial.
    * X1 + X2 ~ Poisson(λ1 + λ2)
    - $\lambda^xe^{-\lambda}/x!$
    - $E(X) = \lambda$
    - $V(X) = \lambda$
    - MGF = $e^{\lambda(e^t-1)}$

## Continuous
* Uniform(a, b)
    - $I(a<x<b)/(b-a)$
    - $E(X) = (a+b)/2$
    - $V(X) = (b-a)^2/12$
    - MGF = $(e^{bt}-e^{at})/((b-a)t)$
* Normal, N(μ, σ^2)
    - $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$
    - $E(X) = \mu$
    - $V(X) = \sigma^2$
    - MGF = $exp\{\mu t+\frac{\sigma^2t^2}{2}\}$
* Exp(β)
    - the lifetimes of electronic components and the waiting times between rare events;
    * = Gamma(1, β)
    * X1 + X2 ~ Gamma(2, β)
    - $\frac{e^{-x/\beta}}{\beta}$
    - $E(X) = \beta$
    - $V(X) = \beta^2$
    - MGF = $\frac{1}{1-\beta t}$ with $t<1/\beta$
* Gamma(α, β)
    * X1 + X2 ~ Gamma(α1 + α2, β)
    - $\frac{x^{\alpha-1}e^{-x/\beta}}{\Gamma(\alpha)\beta^\alpha}$
    - $E(X) = \alpha\beta$
    - $V(X) = \alpha\beta^2$
    - MGF = $(\frac{1}{1-\beta t})^\alpha$ with $t<1/\beta$
* Beta(α, β)
* $t_v$
    * $t_\infty$ = Normal
* Cauchy
    * = $t_1$
* $χ^2_p$
    * Z1, ..., Zn ~ IID Normal, then $Z_1^2 + ... + Z_p^2 \sim χ^2_p$
