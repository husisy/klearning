# space

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
