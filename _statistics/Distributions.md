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
        - 假设事件之间的时间不受先前事件之间的时间的影响（即它们是独立的），那么每单位时间的事件数遵循泊松分布.
        - $\lambda$ 是$P(x=k)$分布函数的均值.
    - can be deduced from Binomial.
        - 已知一段时间内的时间一个随机变量的期望。
        - 把此随机变量看作是一个Bernoulli随机变量的叠加。
        - 把此时间段分割成n段，于是整体上可以看作一个Binomial随机变量。让n趋向于无穷。
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
        - 如果每单位时间的事件数服从泊松分布，则事件之间的时间量服从指数分布。
    * = Gamma(1, β)
    * X1 + X2 ~ Gamma(2, β)
    - $\frac{e^{-x/\beta}}{\beta}$
        - 更常见的写法 $Exp(\lambda) = \lambda e^{-\lambda x}$。这时 $\lambda$ 的含义就和泊松分布的 $\lambda$ 的含义相同了，即单位时间内某事件发生的平均次数。
    - $E(X) = \beta$
        - $E(X) = \frac{1}{\lambda}$
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
    - $\frac{\Gamma((v+1)/2)}{\Gamma(v/2)}\frac{1}{(1+x^2/v)^{(v+1)/2}}$
    - $E(X) = 0$ when $v>1$
    - $V(X) = v/(v-2)$ when $v>2$
    - MGF does not exist.
* Cauchy
    * = $t_1$
* $χ^2_p$
    * Z1, ..., Zn ~ IID Normal, then $Z_1^2 + ... + Z_p^2 \sim χ^2_p$
