---
layout: default
title: Linear Algebra Transforms
---

{% include katex.html %}

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;url&quot;:&quot;https://raw.githubusercontent.com/harwise/diagrams/main/linear_transforms.drawio&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/embed2.js?&fetch=https%3A%2F%2Fraw.githubusercontent.com%2Fharwise%2Fdiagrams%2Fmain%2Flinear_transforms.drawio"></script>

|linear map|
|:--------:|
|$T(u+v) = Tu + Tv$ <br> $T(\lambda v) = \lambda T(v)$|
|(Fundermental Theorem) <br> Given $u_1,\dots,u_m, v_1,\dots v_n$, <br> and $u$ is a basis of null $T$, <br> then $Tv_1,\dots,Tv_n$ is a basis of range $T$.|

<br><br>

|upper-triangular matrix|
|:---------------------:|
|$T$ with respect to $v_1,\dots,v_n$ is upper triangular.|
|$Tv_j\in span(v_1,\dots v_j)$ for each $j=1,\dots,n$.|
|$span(v1,\dots,v_j)$ is invariant under $T$ for each $j=1,\dots,n$.|

<br><br>

|diagonalizable|
|:------------:|
|$V$ has a basis consisting of eigenvectors of $T$.|
|There exists 1-dimensional subspaces $U_1,\dots,U_n$ of $V$, each invariant under $T$, such that $V=U_1\oplus\dots\oplus U_n$.|
|$V=E(\lambda_1,T)\oplus\dots\oplus E(\lambda_n,T)$.|
|$dimV$ = $dimE(\lambda_1,T)+\dots + dimE(\lambda_m,T)$|

<br><br>

|normal operator|
|:-------------:|
|$TT^\ast= T^\ast T$|
|$\lVert Tv \rVert = \lVert T^*v \rVert$|
|(property) $Tv=\lambda v \iff T^*v=\overline{\lambda}v$|
|(property) Eigenvectors corresponding to distinct enginvalues are orthogonal.|
|Over $C$, normal = diagonalizable with respect to an orthogonal basis.|
|Over $R$, normal = block diagonal matrix such that each block is a 1-by-1 matrix or a 2-by-2 matrix of the form $$\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$$ with b > 0.|

非Normal的矩阵，二维空间下，对于一个eigenvalue，也许只有一个eigenvector，剩下的一个维度没法弄。比如 $$\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$$ 也就是Jordan Form里面的那个I（on R）或者1（on C）的由来。

而Normal的矩阵，每个维度都能分解出来且正交。（不考虑旋转 on R）。

<br><br>

|self-adjoint operator|
|:-------------------:|
|$T = T^*$|
|$\langle Tv,w\rangle=\langle v,Tw\rangle$|
|$M(T)=M(T^*)$ with respect to orthonormal bases.|
|Over $C$, $\langle Tv,v\rangle\in R$|
|(property) Every eigenvalue is real.|
|(property) Eigenvectors corresponding to distinct enginvalues are orthogonal.|
|(property) $\langle Tv,v\rangle=0 \rightarrow T=0$ (This is interesting only over $R$, because over $C$, it is always true, not just for self-adjoint oprators.)|
|Over $R$, self-adjoint $\iff$ diagonalizable with respect to an orthogonal basis|

把 旋转 on R 也排除掉了。

<br><br>

|positive operator|
|:---------------:|
|self-adjoint<br>$\langle Tv,v \rangle\ge0$ for all $v\in V$|
|self-adjoint<br>all the eigenvalues of $T$ are nonnegative.|
|$T$ has a positive square root. (and it's unique)|
|$T$ has a self-adjoint square root.|
|there exists an operator $R\in L(V)$ such that $T=R*R$.|

<br><br>

|isometry|
|:------:|
|perserves norms: $\lVert Sv \rVert = \lVert v \rVert$ for all $v\in V$|
|$\langle Su,Sv \rangle = \langle u,v \rangle$ for all $u,v \in V$|
|$Se_1,\dots,Se_n$ is orthonormal for every orthonormal list $e_1,\dots,e_n$ in $V$.|
|there exists an orthonormal basis $e_1,\dots,e_n$ of $V$ such that $Se_1,\dots,Se_n$ is orthonormal.|
|$S^*S=I$|
|$SS^*=I$|
|$S^*$ is isometry.|
|$S$ is invertible and $S^{-1}=S^*$|
|Over C, diagonalizable with respect to an orthogonal basis (eigenvectors), and eigenvalues have absolute value 1.|
|Over $R$, isometry = block diagonal matrix such that each block is a 1-by-1 matrix or a 2-by-2 matrix of the form $$ \begin{pmatrix} cos{\theta} & -sin{\theta} \\ sin{\theta} & cos{\theta} \end{pmatrix} $$ with $\theta \isin (0, \pi) $.|

<br><br>

## 矩阵的行向量和列向量

矩阵的列向量表示：旧的坐标轴在新的坐标系下的位置；也就是原来的坐标轴向量被变换到了哪里。

矩阵的行向量表示：在旧坐标系下，被变换向量和哪些向量作为内积。注意到这不一定表示旧坐标系下，新坐标轴的位置。只有当新坐标系是**正交且无缩放**矩阵(isometry?)，才可以这么理解。（正交是必须；如果不同的基缩放值不同，会导致虽然列向量正交，但行向量并不正交。）

注意到这两者是相等的：坐标轴向量和行向量做内积 = 坐标轴向量被变换到新坐标系（以列向量为基）下的坐标值。


## 一个特征值也没有

On C: 不可能没有特征值。因为多项式等式总能在C上求得解。

On R: 比如二维旋转矩阵。
$$
\begin{pmatrix}
0.866 & -0.5 \\
0.5 & 0.866
\end{pmatrix}
$$

### **SVD**

$$
\begin{pmatrix}
0.866 & -0.5 \\
0.5 & 0.866
\end{pmatrix} =

\begin{pmatrix}
-1 & 0 \\
0 & 1
\end{pmatrix}

\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}

\begin{pmatrix}
-0.866 & 0.5 \\
0.5 & 0.866
\end{pmatrix}
$$

## 有重复特征值，但对应特征向量只有一个

比如
$$
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}
$$

### **Jordan Dcomposition**

$$
\begin{pmatrix}
0.866 & -0.5 \\
0.5 & 0.866
\end{pmatrix} =

\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}

\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}

\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

前后是正交矩阵且互逆，但中间不是对角阵

### **SVD**

$$
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix} =

\begin{pmatrix}
0.851 & -0.526 \\
0.526 & 0.851
\end{pmatrix}

\begin{pmatrix}
1.618 & 0 \\
0 & 0.618
\end{pmatrix}

\begin{pmatrix}
0.526 & 0.851 \\
-0.851 & 0.526
\end{pmatrix}
$$

SVD 的前后两个正交基并不互逆。

## 不同特征值，不同特征向量，但是特征向量不正交

比如
$$
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}
$$

### **Jordan Dcomposition**

$$
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix} =

\begin{pmatrix}
1 & 0 \\
0 & 1/2
\end{pmatrix}

\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix}

\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}
$$

前后是正交矩阵且互逆，但中间不是对角阵

### **能够使用非正交矩阵和对角阵来分解吗？**

$$
\begin{pmatrix}
2 & 0 \\
1 & 1
\end{pmatrix}
\\
\lambda_1 = 1, v_1 = (0, 1)^T
\\
\lambda_1 = 2, v_1 = (1, 1)^T
$$

虽然可以得到如下结果

$$
\begin{pmatrix}
2 & 0 \\
1 & 1
\end{pmatrix} =

\begin{pmatrix}
-2 & 1 \\
0 & 1/2
\end{pmatrix}

\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}

\begin{pmatrix}
0 & 1 \\
1 & 1
\end{pmatrix}
$$

其中最右边矩阵是来自于两个非正交基，中间矩阵来自于特征值。但是左边矩阵并不是右边矩阵的逆 （实际上我不知道如何用直观的方法求得它）。- 这种分解可能没有实际用处，它说明了正交矩阵的重要性。

### **SVD**

$$
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix} =

\begin{pmatrix}
0.924 & -0.383 \\
0.383 & 0.924
\end{pmatrix}

\begin{pmatrix}
2.414 & 0 \\
0 & 0.414
\end{pmatrix}

\begin{pmatrix}
0.383 & 0.924 \\
-0.924 & 0.383
\end{pmatrix}
$$

SVD 的前后两个正交基并不互逆。

## 特征向量正交

On C, normal operator

on R, self-adjoint operator

比如
$$
\begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix}
$$

### **Jordan Dcomposition** (此时能够对角化)

$$
\begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix} =

\begin{pmatrix}
-1 & 1 \\
1 & 1
\end{pmatrix}

\begin{pmatrix}
-1 & 0 \\
0 & 3
\end{pmatrix}

\begin{pmatrix}
-1/2 & 1/2 \\
1/2 & 1/2
\end{pmatrix}
$$

前后是正交矩阵且互逆，而且中间是对角阵

### **SVD**

$$
\begin{pmatrix}
1 & 2 \\
1 & 1
\end{pmatrix} =

\begin{pmatrix}
0.707 & 0.707 \\
0.707 & -0.707
\end{pmatrix}

\begin{pmatrix}
3 & 0 \\
0 & 1
\end{pmatrix}

\begin{pmatrix}
0.707 & 0.707 \\
-0.707 & 0.707
\end{pmatrix}
$$

SVD 的前后两个正交基并不互逆。