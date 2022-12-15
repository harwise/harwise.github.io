---
layout: default
title: Proof
---

{% include katex.html %}

# Proof

* Three types of statesments
    * True statements: Theorems & propositions.
    * Truth unknown: Conjectures.
    * False statements: X.

<br>

* Existence statements. $\exist$
    * Produce an example.
* Universal Statements. $\forall$
    * An expression of form $P(x) \Rightarrow Q(x)$ is understood to be the *statement* $\forall x \isin X, P(x)\Rightarrow Q(X)$.
    * To prove a statement $P$, is the same to prove $true \Rightarrow P$.
* Contropositive.
    * $P(x) \Rightarrow Q(x)$ is logically the same as $\lnot Q(x) \Rightarrow \lnot P(x)$.
* Controdiction.
    * $P$, or $true \Rightarrow P$ is logically the same as $\lnot P \Rightarrow false$.
    * $P \Rightarrow Q$ is logically the same as $\lnot(\forall x, P \Rightarrow Q) \Rightarrow false$, $\lnot(\forall x, \lnot P \lor Q) \Rightarrow false$, i.e. ($\exist x, P \land \lnot Q) \Rightarrow false$.

<br>

* Disprove (prove $\lnot P$)
    * $\lnot(\forall x \isin S, P(x))$ is the same as $\exist x \isin S, \lnot P(x)$. The example x is called a counterexample.
    * $\lnot(P(x) \Rightarrow Q(x))$ is the same as $\exist x \isin S, P(x) \land \lnot Q(x)$. The example x is called a counterexample.
    * $\lnot(\exist x \isin S, P(x))$ is the same as $\forall x \isin S, \lnot P(x)$.
    * Controdiction.
        * $\lnot P$ is the same as $P \Rightarrow false$.
        * $\lnot (\exist x, P)$ is the same as $(\exist x, P) \Rightarrow false$.

<br>

* Mathematical Induction
    * For the statement $S_1, S_2, S_3, S_4,...$ are all true.
    * Induction + contradition.
        * Let k > 1 be the smallest integer for which $S_k$ is false.
        * Prove $S_{k-1} \land \lnot S_k \Rightarrow false$

# Relations

* A relation on a set $A$ is a subset $R \subseteq A \times A $.
    * $(x,y) \isin R$
    * $xRy$
    * $R$ is **reflexive** if $\forall x \isin A, xRx$.
        * In its diagram, there is a loop at each point x.
    * $R$ is **symmetric** if $\forall x \isin A, xRy \Rightarrow yRx$.
        * In its diagram, whenver there is an arrow from x to y, there is one from y back to x.
    * $R$ is **transitive** if $\forall x,y,z \isin A, ((xRy)\land(yRz))\Rightarrow xRz$.
        * In its diagram, whenver there are arrows from x to y and y to x, there is also one from x to z. 

* A relation on a set $A$ is an **equivalence relation** if it is reflexive, symmetric and transitive.
    * Given a set $A$ and an equivalence relation on it $R$, the **equivalence class** containing $a$ is denoted as $[a]=\{x \isin A:xRa\}$.
    * Given a set $A$ and an equivalence relation on it $R$, $[a] = [b]$ if and only if $aRb$.
    * Suppose $R$ is an equivalence relation on a set $A$. Then the set $\{[a]: a \isin A\}$ of equivalence classes of $R$ forms a **partition** of $A$.
    * **Equivalence relations** and **partitions** are really just two different ways of
looking at the same thing.

# Functions

* A function $f$ from $A$ to $B$ ($f:A \to B$) is a relation $f \subseteq A \times B$ from $A$ to $B$, satisfying the property that for each $a \isin A$ the relation contains exactly one ordered pair of $(a, b)$.
    * $f(a) = b$
    * $A$ is called **domain** of $f$.
    * $B$ is called **codomain** of $f$.
        * A function’s codomain is not really an intrinsic feature of
the function, but more a matter of convenience
        * Two functions $f:A \to B$ and $g:A \to D$ are equal if $f=g$(as sets). They can have different codomains.
    * The **range** of $f$ is the set $\{f(a):a \isin A\}$.

* The **composition** of $f$ with $g$, denoted as $g \circ f: A \to C$.
    * $g \circ f (x) = g(f(x))$.
    * Composition of functions is **not commutative**.
    * Composition of functions is **associative**. $(h \circ g) \circ f = h \circ (g \circ f)$.
    * Suppose $f:A \to B$ and $g: B \to C$. If both $f$ and $g$ are **injective**/**surjective**, then $g \circ f$ is **injective**/**surjective**.

* Inverse Functions
    * Given a relation $R$ from $A$ to $B$, the **inverse relation of** $R$ is the relation from $B$ to $A$ defined as $R^{-1} = \{ (y,x):(x,y) \isin R \}$.
    * Let $f: A \to B$ be a function. Then $f$ is bijective if and only if the inverse relation $f^{-1}$ is a function from $B$ to $A$.
        * **Identity function** $i_A:A \to A$ is defined as $i_A(x)=x$.
        * $f^{-1} \circ f = i_A$
        * $f \circ f^{-1} = i_B$

* **Image** and **Preimage**
    * Suppose $f: A \to B$ is a function.
    * If $X \subseteq A$, the **image of** $X$ is the set $f(X) = \{ f(x):x \isin X \} \subseteq B$.
    * If $Y \subseteq B$, the **preimage of** $Y$ is the set $f^{-1}(Y) = \{ x \isin A: f(x) \isin Y\} \subseteq A$.
    * $f(W \cap X) \subseteq f(W) \cap f(X)$
    * $f(W \cup X) = f(W) \cup f(X)$
    * $f^{-1}(Y \cap Z) = f^{-1}(Y) \cap f^{-1}(Z)$
    * $f^{-1}(Y \cup Z) = f^{-1}(Y) \cup f^{-1}(Z)$
    * $X \subseteq f^{-1}(f(X))$
    * $f(f^{-1}(Y)) \subseteq Y$

# Calculus

* **Triangle inequality**. If $x, y, z \isin R$, then $|x-y| \le |x-z| + |z-y|$.
    * $|x+y| \le |x| + |y|$
    * $|x-y| \le |x| + |y|$
    * $|x| - |y| \le |x+y|$
    * $|x| - |y| \le |x-y|$
* **Limit**
    * Suppose $f:X \to R$ is a function, where $X \subseteq R$, and $c \isin R$. Then $\lim_{x \to c}{f(x)}$ means that for any real $\epsilon > 0 $ (no matter how small), there is a real number $\delta > 0$ for which $|f(x)-L|< \epsilon$ provided that $0<|x-c|<\delta$.
        * $\forall \epsilon>0, \exist \delta >0, (0<|x-c|<\delta) \Rightarrow (|f(x)-L|< \epsilon)$
        * $lim_{x \to c}af(x) = a\ lim_{x \to c}f(x)$
        * $lim_{x \to c}(f(x) \pm g(x)) = lim_{x \to c}f(x) \pm lim_{x \to c}g(x)$
        * $lim_{x \to c}f(x)g(x) = (lim_{x \to c}f(x))\cdot(lim_{x \to c}g(x))$
        * $lim_{x \to c}\frac{f(x)}{g(x)} = \frac{lim_{x \to c}f(x)}{lim_{x \to c}g(x)}$
        
* **Continuous**
    * A function $f(x)$ is **continuous** at $x=c$ if $lim_{x \to c}=f(c)$.
        1. $f(c)$ is defined,
        2. $lim_{x \to c}f(x)$ exists,
        3. $lim_{x \to c}f(x)=f(c)$.
    * If $lim_{x \to c}g(x) = L$ and $f$ is **continuous** at $x=L$, then $lim_{x \to c}f(g(x)) = f(lim_{x \to c}g(x))$

* Sequence
    * We denote a sequence with *n*th term $a_n$ as $\{a_n\}$.
    * A sequence $\{a_n\}$ **converges** to a number $L \isin \R$ provided that for any $\epsilon >0$ there is an $N \isin \N$ for which $n > N$ implies $|a_n - L| < \epsilon$.
* Series
    * A **series** is an infinite sum $\Sigma_{k=1}^{\infty}a_k$.
    * A series $\Sigma_{k=1}^{\infty}a_k$ **converges** to a real number $S$ if its sequence of partial sum ${S_n}$ converges to $S$.

# Cardinality of Sets

* $|\N| = |\Z| = |\mathbb{Q}| = \aleph_0$. **Countablely infinite**.
    * If $A$ and $B$ are both countably infinite, then so is $A \times B$.
    * If $A$ and $B$ are both countably infinite, then so is $A \cup B$.
    * An infinite subset of a countably infinite set is countably infinite.
* $|\N| \not= |\R|$
* $|\R|=|(0, +\infty)| = |(0, 1)| = |\wp(\N)|$, where $\wp$ means powerset.
* If $|A| \le |B|$ and $|B| \le |A|$, then $|A| = |B|$. In other words, if there are injections $f: A \to B$ and $g: B \to A$, then there is a bijection $h: A \to B$.

