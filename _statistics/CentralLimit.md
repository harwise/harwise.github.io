---
layout: default
title: Central Limit Theorem
---

{% include katex.html %}

# chebyshev's theorem

切比雪夫不等式给出了在随机变量的分布未知，而只需要知道E(X)和D(X)的情况下估计概率的界限。

$P\{[X-\mu] \ge \epsilon \} \le \frac{\sigma^2}{\epsilon^2}$

$P\{[X-\mu] \lt \epsilon \} \ge 1 - \frac{\sigma^2}{\epsilon^2}$

切比雪夫不等式可以对随机变量偏离期望值的概率做出估计，这是大数定律的推理基础。

# 林德贝格-勒维Lindeberg-Levy中心极限定理，又称独立同分布中心极限定理。

如果$\{X_n\}$独立同分布，$E(X)=\mu$, $D(X)=\sigma^2$，则n足够大时$\overline{X_n}$ 近似服从正态分布$N(\mu, \frac{\sigma^2}{n})$

# 棣莫弗-拉普拉斯De Moivre-Laplace中心极限定理

是独立同分布中心极限定理的特殊情况，它是最先被发现的中心极限定理。

当试验次数n足够大时，二项分布近似于正态分布。


# 林德伯格中心极限定理

实际上，一系列独立不同分布的随机变量也可能满足中心极限定理，只是这些不同分布的随机变量要有所限制。

林德伯格中心极限定理对$\{X_n\}$的约束基本上是最弱的，也就是最强的中心极限定理。然而该定理的条件较难运用与验证.

# 李雅普诺夫Lyapunov中心极限定理

是林德伯格中心极限定理的特例。
李雅普诺夫中心极限定理的条件在很多情况下是满足的，因此适用性也很广。