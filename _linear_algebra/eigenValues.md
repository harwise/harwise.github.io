---
layout: default
title: Linear Transforms Eigen Values
---

{% include katex.html %}

* Invariant subspace with dimension 1.
* Invariant subspace space U 的意义在于，能够将 T 在 V 上的作用分解为两项：
    * 作用在 $U$ 上.  
        $T|_U \isin L(U)$ restricition operator. $T|U(u) = Tu$
    * 作用在 quotient space $V/U$ 上 ($dimV/U=dimV-dimU$).  
        $T/U \isin L(V/U)$ qutient operator. $(T/U)(v+U) = Tv + U$
---

* $T-\lambda I$ is not injective/surjective/invertible.
* $v \isin null(T-\lambda I)$
* $U = range(T-\lambda I)$ is invariant under $T$.
    * U可能不包含eigenvector v。比如有n个不同的eigen values的T。
    * U也可能包含eigenvector v。E.g. $Tw=v+\lambda w$, then $(T-\lambda I)w=v+\lambda w - \lambda w=v$

---

* The diagonal of an upper-triangular matrix is its engenvalues.

---

* Every operator on a complex vector space has an eigenvaue.
* Because $U$ is invariant and $dimU < dimV$, as well as for a basis $u_1,...,u_m,w_1,...,w_n$ we have $Tw_k=(T-\lambda I)w_k + \lambda w_k$(!!!在V/U上的eigen vector!!!), by induction we can get "Every $T$ on a complex vector space has an upper-triangular  matrix".

---

* Orthonormal basis: $v = \langle v,e_1 \rangle e_1 + \dots + \langle v,e_n \rangle e_n$ and $ \Vert v \Vert^2 = \vert \langle v,e_1 \rangle \vert^2 + \dots +  \vert \langle v,e_n \rangle \vert^2 $
* Every linearly independent list can be turned into an orthonormal list with the same span; every finite-dimensional inner product space has an orthonormal basis.

---

* adjoint (conjugate transpose): $M(T^*,(f_1,\dots,f_m),(e_1,\dots,e_n))$ is the conjugate transpose of $M(T,(e_1,\dots,e_n),(f_1,\dots,f_m))$

---

* self-adjoint $T=T^*$
    * Eigenvalues are real.
    * It is normal (see below).
    * Self-adjoint <=> (Over R, diagonal matrix with respect to some orthogoal basis.)
    * T is called positive if all eigenvalues are nonnegative.
        * Has a unique positive square root. $T = R*R$.

---

* normal: $TT^*=T^*T$
* normal: $\Vert Tv \Vert = \Vert T^*v \Vert$
    * $T$ and $T^*$ have the same eigenvectors and $T^*$ has eigenvalue $\bar{\lambda}$
    * Eigenvectors corresponding to distinct eigenvalues are orthogonal.
    * Normal <=> (Over C, diagonal matrix with respect to some orthogoal basis.)
    * S is called isometry/orthogonal if $\Vert Sv \Vert = \Vert v \Vert$
        * Invertible and $S^{-1}=S^*$

