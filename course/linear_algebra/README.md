# linear algebra

```text
matrix (svd)
├── diagonalizable 可对角矩阵
│   ├── normal 正规矩阵
│   │   ├── unitary 幺正矩阵
│   │   ├── special unitary
│   │   ├── hermitian 厄米矩阵
│   │   │   ├── orthogonal projection matrix
│   │   │   └── oblique projection matrix
│   │   ├── skew-hermitian 斜厄米矩阵
│   │   ├── circulant 循环矩阵
│   │   └── other
│   └── diagonalizable but unnormal 可对角但非正规矩阵
└── defective matrix
    └──Jordan norm form

matrix (svd)
├── invertible 可逆矩阵 general linear group
└── non-invertible 不可逆矩阵
```

1. link
   * eigendecomposition [wiki](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix)
   * skew-hermitian matrix [wiki](https://en.wikipedia.org/wiki/Skew-Hermitian_matrix)
   * unitary matrix [wiki](https://en.wikipedia.org/wiki/Unitary_matrix)
   * special unitary matrix [wiki](https://en.wikipedia.org/wiki/Special_unitary_group)
   * genral linear group $\mathrm{GL}(n,\mathbb{F})$ [wiki](https://en.wikipedia.org/wiki/General_linear_group)
   * singular value decomposition
   * polar decomposition
   * [mit-mooc-link](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/) Matrix Calculus For Machine Learning And Beyond
2. invertible matrix: $det(A)\ne 0$
   * `min(svd)=0`
3. 可逆矩阵和可对角化没有包含或者被包含关系
   * 可逆但不可对角化：约当矩阵Jordan matrix
   * 可对角化但不可逆：`diag{1,0}`
4. diagonalizable matrix: $A=USU^{-1}$，其中$U$可以是任何可逆矩阵，该分解称作特征值分解eigen decomposition
   * 每个特征向量有一个缩放自由度
   * 当无重根时，且每个特征向量归一化时，特征分解唯一
   * 对于重根的特征子空间内（特征值相同），特征向量可以彼此正交
   * 特征值不同的特征向量，无正交约束
5. normal matrix: $AA^\dagger=A^\dagger A$, 即$[A,A^\dagger]=0$
   * 充要条件：特征值分解$A=USU^{-1}$中的$U$是幺正矩阵，该分解称作谱分解spectral decomposition
   * 正规矩阵近似可以看做厄米矩阵和幺正矩阵的奇奇怪怪组合
   * **强调**正规矩阵对于矩阵加法不封闭
   * **强调**正规矩阵对于矩阵乘积不封闭
   * $A=U^\dag \Lambda U=U^\dag r e^{i\theta} U=U^\dag r V$, $V=e^{i\theta}U$
6. diagonalizable but unnormal matrix
   * 简单谐振子中的产生湮灭算符
   * 特征值分解$A=USU^{-1}$中的$U$不是幺正矩阵，即特征向量不正交
   * （猜想）normal matrix选取部分行部分列可以构成unnormal matrix，即其特征矢量在子空间的投影是不正交的。但并非一定unnormal matrix
   * （猜想）unnormal matrix总是可以拓展高维空间编程normal matrix，pseudo-inverse?
7. hermitian matrix: $A=A^\dagger$
   * 特征值恒实数
8. projection matrix [wiki](https://en.wikipedia.org/wiki/Projection_(linear_algebra)) $PP=P$
   * orthonormal projction matrix $P^\dagger=P$
   * oblique projection matrix $P^\dagger\ne P$
9. skew-hermitian $A^\dagger=-A$
   * 特征值纯虚（包含0）
   * 与hermitian matrix同构`A=iB`
10. unitary matrix: $UU^\dagger=I$
    * 等价定义：列向量正交归一，行向量正交归一
    * 特征值模为1
11. special unitary matrix $det(A)=1$
12. TODO
    * Symplectic matrix [wiki](https://en.wikipedia.org/wiki/Symplectic_matrix)
    * orthogonal complement [wiki](https://en.wikipedia.org/wiki/Orthogonal_complement)

## misc

1. matrix
   * range, image, column space, rank
   * row space
   * support: $supp(A)=\{x|Ax\ne 0\}$

## space

1. topological space
   * [wiki](https://en.wikipedia.org/wiki/Topological_space)
2. metric space
   * [wiki](https://en.wikipedia.org/wiki/Metric_space)
   * identity of indisernibles $d(x,y)=0\leftrightarrow x=y$
   * positivity $x\ne y\rightarrow d(x,y)> 0$
   * symmetry $d(x,y)=d(y,x)$
   * triangle inequality $d(x,z)\leq d(x,y)+d(y,z)$
   * not every metric is induced from a norm [stackexchange](https://math.stackexchange.com/a/166382)
   * complete space
   * compact space
3. normed vector space: must be linear space
   * [wiki](https://en.wikipedia.org/wiki/Normed_vector_space)
   * non-negativity $||x||\geq 0$
   * zero $x=0\leftrightarrow||x||=0$
   * absolute homogeneity $|$tx$|=|t|\; ||x||, t\in \mathbb{R}$
   * triangle inequlity $||x+y||\leq ||x|| + || y||$
4. inner product space
   * [wiki](https://en.wikipedia.org/wiki/Inner_product_space)
   * conjugate symmetry $\langle x,y\rangle=\langle y,x\rangle^*$
   * linearity in the first argument $\langle ax+by,z\rangle=a\langle x,z\rangle+b\langle y,z\rangle$ (different convention in math and physics)
   * positive-definite $x\ne 0\leftrightarrow \langle x,x\rangle >0$
5. linear space (vector space): field $F$, set $V$, addition $+$, scalar multplication
   * [wiki](https://en.wikipedia.org/wiki/Vector_space)
   * 加法结合律 associativity of addition `u+(v+w)=(u+v)+w`
   * 加法交换律 commutativity of addition `u+v=v+u`
   * 加法零元 identity element of addition `v+0=v`
   * 加法逆 inverse elements of addition `v+(-v)=0`
   * 数乘结合律 compatibility of scalar multiplication `a(bu)=(ab)u`
   * 数乘单位元 identity element of scalar multiplication `1*u=u`
   * 数乘矢量分配律 distributivity of scalar multiplication with respect to vector `a(u+v)=au+av`
   * 数乘标量分配律 distributivity of scalar multiplication with respect to scalar `(a+b)u=au+bu`
6. hierarchy: topological space, metric space, normed vector space, inner product space

![hierarchy-space](https://upload.wikimedia.org/wikipedia/commons/7/74/Mathematical_Spaces.png)

example

1. Euclidean space
   * [wiki](https://en.wikipedia.org/wiki/Euclidean_space)
   * Euclidea vector space: a finite-dimensional inner product space over the real numbers
2. Hilbert space
   * [wiki](https://en.wikipedia.org/wiki/Hilbert_space)
   * a Hilbert space $H$ is a real or complex inner produce space that is also a complete metric space with respect to the distance function induced by the inner product
   * pre-Hilbert space：内积空间 + metric space
   * Hilbert space：内积空间 + complete metric space；一个incomplete metric space的栗子见[wiki](https://en.wikipedia.org/wiki/Inner_product_space#Hilbert_space)
   * distance function (norm): symmetric in $x$ and $y$, nonzero, triangle inequality (Cauchy-Schwarz inequality)

norm space

1. matrix norm [wiki/matrix-norm](https://en.wikipedia.org/wiki/Matrix_norm#Schatten_norms)
   * [wiki/Schatten-norm](https://en.wikipedia.org/wiki/Schatten_norm)
   * [wiki/trace-distance](https://en.wikipedia.org/wiki/Trace_distance)
   * nuclear norm
2. dual norm $||x||_*=\sup\{u\cdot x:||x||\leq 1\}$
   * vector space: $\frac{1}{p}+\frac{1}{q}=1$
