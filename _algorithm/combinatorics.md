---
layout: default
title: Combinatorics
---

{% include katex.html %}

* Fibonacci Numbers
    * F(n) = F(n-1) + F(n-2)
    * ~ (1.618^n)/sqrt(5)
    * Zeckendorf's theorm.
        * Every positive integer can be written in a unique way as a sum of one or more distinct Fibonacci numbers such that the sum does not include any two consecutive Fibonacci numbers.
        * Fibinary number. To make the Fibinary representations unique, larger Fibonacci terms must always be used whenever possible (i.e. disallow 2 adjacent 1’s).

* Binomial Coefficients
    * C(n, k) = C(n-1, k-1) + C(n-1, k)
    * C(n ,2) ~ O(n^2)

* Catalan Numbers
    * Cat(n) = C(2n, n) / (n+1); Cat(0) = 1
    * Cat(n+1) = $\sum{_{i=0}^n C_iC_{n-i}}$
    * Cat(n+1) = Cat(n) * $\frac{(2n+2) * (2n+1)}{(n+2) * (n+1)}$
    * Cat(n) ~ O(4^n)
    * The number of distinct binary search trees

* Burnside's Lemma
    * TODO

* Cayley's Formula
    * TODO

* Derangement
    * TODO

* Stirling Numbers
    * TODO

