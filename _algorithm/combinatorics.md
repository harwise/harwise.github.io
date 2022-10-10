---
layout: default
title: Combinatorics
---

{% include katex.html %}

* Fibonacci Numbers
    * F(n) = F(n-1) + F(n-2)
    * ~ $(1.618^n)/\sqrt{5}$
    * Zeckendorf's theorm.
        * Every positive integer can be written in a unique way as a sum of one or more distinct Fibonacci numbers such that the sum does not include any two consecutive Fibonacci numbers.
        * Fibinary number. To make the Fibinary representations unique, larger Fibonacci terms must always be used whenever possible (i.e. disallow 2 adjacent 1’s).

* Binomial Coefficients
    * C(n, k) = C(n-1, k-1) + C(n-1, k)
    * C(n ,2) ~ $O(n^2)$

* Catalan Numbers
    * The number of distinct binary search trees
    * Cat(n) = C(2n, n) / (n+1); Cat(0) = 1
    * Cat(n+1) = $\sum{_{i=0}^n C_iC_{n-i}}$
    * Cat(n+1) = Cat(n) * $\frac{(2n+2) * (2n+1)}{(n+2) * (n+1)}$
    * Cat(n) ~ $O(4^n)$

* Cayley's Formula
    * Cayley(n) = $n^{n-2}$
    * Proof: Prüfer code (Trees.cpp)
    * The number of spanning trees in a complete graph.
    * Is there a nice formula for counting the number T(n) of unlabeled trees on n vertices? Starting from n = 2 we have T(n) : T(2) = 1, T(3) = 1, T(4) = 2, T(5) = 3.
    * T(n) > Cayley(n) / n!
    * It is an open problem to find a closed form formula for T(n).

* Derangement
    * Der(n) = (n-1) * (Der(n-1) + Der(n-2)), Der(0) = 1, Der(1) = 0
    * Proof: Each person may receive any of the n − 1 hats that is not their own. Call the hat which the person P1 receives hi and consider hi’s owner: Pi receives either P1's hat, h1, or some other. Accordingly, the problem splits into two possible cases:
        1. Pi receives a hat other than h1. This case is equivalent to solving the problem with n − 1 people and n − 1 hats because for each of the n − 1 people besides P1 there is exactly one hat from among the remaining n − 1 hats that they may not receive (for any Pj besides Pi, the unreceivable hat is hj, while for Pi it is h1). Another way to see this is to rename h1 to hi, where the derangement is more explicit: for any j from 2 to n, Pj cannot receive hj.
        2. Pi receives h1. In this case the problem reduces to n − 2 people and n − 2 hats, because P1 received hi's hat and Pi received h1's hat, effectively putting both out of further consideration.
    * ${\displaystyle !n=n!\sum _{i=0}^{n}{\frac {(-1)^{i}}{i!}}} \space for \space {\displaystyle n\geq 0}$
    * ${\displaystyle \lim _{n\to \infty }{!n \over n!}=\lim _{n\to \infty }\sum _{i=0}^{n}{\frac {(-1)^{i}}{i!}}=e^{-1}\approx 0.367879\ldots .}$
    * A permutation of the elements of a set such that none of the elements appera in their original position.

* Stirling Numbers
    * ${\displaystyle n!\sim {\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}}$
    * Proof:
        1. ${\displaystyle \ln(n!)=\ln 1+\ln 2+\cdots +\ln n.}$
        2. ${\displaystyle \ln(n!)-{\tfrac {1}{2}}\ln n\approx \int _{1}^{n}\ln x\,{\rm {d}}x=n\ln n-n+1}$

* Erdős–Gallai theorem
    * A sequence of non-negative integers ${d_{1}\geq \cdots \geq d_{n}}$ can be represented as the degree sequence of a finite simple graph on n vertices if and only if
        * $d_{1}+\cdots +d_{n}$ is even and
        * ${\displaystyle \sum _{i=1}^{k}d_{i}\leq k(k-1)+\sum _{i=k+1}^{n}\min(d_{i},k)}$ holds for every k in ${\displaystyle 1\leq k\leq n}$.
    * See Havel Hakimi algorithm.

* Euler's Formula for Planer Graph
    * V - E + F = 2

* Moser's Circle
    * Dividing a circle into areas by means of an inscribed polygon with n sides in such a way as to maximise the number of areas.
    * $f(n)=f(n-1)+\sum^{n-1}_{i=1}\left(1+\left(n-i-1\right)\left(i-1\right)\right)$
        * Proof: the number of lines that each new line intersects can be determined by considering the number of points on the "left" of the line and the number of points on the "right" of the line.
    *  $r_G={n \choose 4}+{n \choose 2}+1$

* Pick's Theorem
    * Suppose that a polygon has integer coordinates for all of its vertices. Let i be the number of integer points that are interior to the polygon, and let b be the number of integer points on its boundary (including vertices as well as points along the sides of the polygon). Then the area A of this polygon is:
    * ${\displaystyle A=i+{\frac {b}{2}}-1.}$

* The number of spanning tree of a complete bipartite graph is:
    * $m^{n-1} \times n^{m-1}$
    * Proof: To prove there are $m^{n−1}n^{m−1}$ spanning trees, we will use a slight modification of Prüfer's original algorithm to get a bijection between trees and integers sequences of length m+n−2. Recall that to get a Prufer code, you repeatedly delete the smallest leaf, and record the label of its neighbor. In our case, we will do almost the same; however, instead of always pruning the smallest leaf, we will prune the smallest leaf in a specific part of the bipartite graph. \
    Specifically, suppose m≤n. We will prune leaves from the parts according to the following pattern: \
    N, N, ..., N, N, M, N, M, N, M \
    So the first string of leaves will come from the larger part, until the parts are equalized, and we alternate thereafter.



* Burnside's Lemma
    * A result in group theory which is often useful in taking account of symmetry when counting mathematical objects.
    * $|X/G|={\frac  {1}{|G|}}\sum _{{g\in G}}|X^{g}|$
        * G is a finite group that acts on a set X.
        * $Xg = \{ x ∈ X : g.x = x \}$
        * $|X/G|$ is the number of orbits.
    * The number of orbits is equal to the average number of points fixed by an element of G.
    * Example: The number of rotationally distinct colourings of the faces of a cube using three colours.
        * Let X be the set of $3^6$ possible face colour combinations that can be applied to a cube in one particular orientation.
        * Let the rotation group G of the cube act on X in the natural manner.
            * one identity element which leaves all $3^6$ elements of X unchanged;
            * six 90-degree face rotations, each of which leaves $3^3$ of the elements of X unchanged;
            * three 180-degree face rotations, each of which leaves $3^4$ of the elements of X unchanged;
            * eight 120-degree vertex rotations, each of which leaves $3^2$ of the elements of X unchanged;
            * six 180-degree edge rotations, each of which leaves $3^3$ of the elements of X unchanged
        * Then two elements of X belong to the same orbit precisely when one is simply a rotation of the other.
        * ${\frac  {1}{24}}\left(3^{6}+6\cdot 3^{3}+3\cdot 3^{4}+8\cdot 3^{2}+6\cdot 3^{3}\right)=57.$
