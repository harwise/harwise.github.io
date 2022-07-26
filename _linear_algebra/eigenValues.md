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
* On a real vector space, all the eigenvalues of $T_c$ are real <=> upper-triangular matrix.

---

* $V = nullT^n \oplus rangeT^n$. 一个维度，经过T变换最多n次，如果没变成0，那它就永远不可能被T变成0. 不变成0，肯定属于range的一部分。
    * E.g. $T=T^2$. 变换一次和变换两次效果相同，说明一次就决定了一个维度是否能变成0，所以$V=nullT \oplus rangeT$.

---

* $V=E(\lambda_1,T) \oplus \dots \oplus E(\lambda_m,T)$ 不一定能成功，取决于它是否有足够的eignevectors.
    * E.g. T(w,z) = (z,0) 只有一个eigenvector.
* $V=G(\lambda_1,T) \oplus \dots \oplus G(\lambda_m,T)$ 只要有eigienvector存在，就能成功。(block diagonal matrix with upper-triangular blocks.)
    * 在 C 上总能成功，因为总有eigenvector.
    * 在 R 上，如果eigenvalues are real，也总能成功。
* $G(\lambda_j,T)$ is invariant under T. （A nilpotent + a scalar multiple of the identity.）
* $(T-\lambda_jI)|_{G(\lambda_j,T)}$ is nilpotent.
* For a nilpotent, there exists a basis: $N^{m_1}v_1,\dots,Nv_1,v_1,\dots,N^{m_n}v_n,\dots,Nv_n,v_n$. 所以有Jordan Form。
    * On C, Jordan Form always exists.
    * On R, Jordan Form exists if the corresponding eigenvalue $\lambda_i$ is real.)

---

* There exists a real invertible matrix P such that $P^{-1}AP = J$ is a real block diagonal matrix.
    * Each block is a real Jordan block.
        * A real Jordan block is either identical to a complex Jordan block (if the corresponding eigenvalue $\lambda_i$ is real).
        * Or is a block matrix itself, consisting of 2×2 blocks (for non-real eigenvalue $\lambda _{i}=a_{i}+ib_{i}$ with given algebraic multiplicity) of the form $C_i=\begin{pmatrix}a_i&-b_i\\ b_i&a_i\end{pmatrix}$ and describe multiplication by $\lambda_i$ in the complex plane. $J_i = \begin{pmatrix}C_i&I&0&0\\0&C_i&I&0\\0&0&C_i&I\\0&0&0&C_i\end{pmatrix}$. Hence in this representation the matrix dimensions are larger than the complex Jordan form.

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
    * Normal <=> (Over R, block diagonal matrix with respect to some orthogoal basis. Each block is 1x1, or 2x2 $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$ with b > 0)
    * S is called isometry/orthogonal if $\Vert Sv \Vert = \Vert v \Vert$
        * Invertible and $S^{-1}=S^*$
        * $\begin{pmatrix}cos{\theta}&-sin{\theta}\\ sin{\theta}&cos{\theta}\end{pmatrix}$ with $\theta \isin (0, \pi)$

---

* Invertible operator T
* T is invertible <=> T is injective/surjective
* T is invertible <=> $(T-\lambda I)$ with $\lambda = 0$ is surjective/injective <=> 0 is not an eigenvalue of T
* T is invertible <=> 0 is not eigenvalue of T <=> $det(T) != 0$
