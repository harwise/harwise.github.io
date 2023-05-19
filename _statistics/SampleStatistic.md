---
layout: default
title: Sample Statistic
---

{% include katex.html %}

# 统计量

统计量不同于统计参数。统计参数通常由于数量过大而不便于统计计算。而统计量仅仅统计抽出来的样本。统计量可以用于对统计参数进行估计。

$\dfrac{\overline{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)$

$\dfrac{\overline{X} - \mu}{S / \sqrt{n}} \sim t(N-1)$

$E(S^2) = D(X)$

$D(\overline{X}) = \dfrac{1}{n}D(X)$

# Distributions

## Chi-squared $\chi^2$

$X_1, X_2,...,X_n \sim N(0,1)$

$\implies X_1^2 + X_1^2 + ... + X_n^2 \sim \chi^2(n)$

## $t$

$X \sim N(0,1); Y \sim \chi^2(n)$

$\implies \dfrac{X}{\sqrt{Y/n}} \sim t(n)$

## $F$

$X \sim \sim \chi^2(n_1); Y \sim \chi^2(n_2)$

$\implies \dfrac{X/n_1}{Y/n_2} \sim F(n_1, n_2)$

# 矩估计

1. 求 $EX$
2. 令 $EX = \overline{X}$，求出未知参数 $\theta$
3. 得到的解就是估计值 $\hat\theta$

# 极大/最大似然估计

1. 写出似然函数 $L(\theta) = \prod \limits_{i=1}^h f(x_i, \theta)$
2. $lnL(\theta)展开$
3. 通过对$\theta$求导，得到极值点处的$\theta$值。
4. 得到的就是估计值 $\hat\theta$

# 置信区间

## $N(\mu, \sigma^2)$

$\mu$ with $\sigma$ known: $(\overline X - \dfrac{\sigma}{\sqrt{n}}u_{\alpha/2}, \space \overline X + \dfrac{\sigma}{\sqrt{n}}u_{\alpha/2})$

$\mu$ with $\sigma$ unknown: $(\overline X - \dfrac{S}{\sqrt{n}}t_{\alpha/2}(n-1), \space \overline X + \dfrac{S}{\sqrt{n}}t_{\alpha/2}(n-1))$

$\sigma^2$: $(\dfrac{(n-1)S^2}{\chi^2_{\alpha/2}(n-1)}, \dfrac{(n-1)S^2}{\chi^2_{1-\alpha/2}(n-1)})$