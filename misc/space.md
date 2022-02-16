# space

1. topological space
   * [wiki](https://en.wikipedia.org/wiki/Topological_space)
2. metric space
   * [wiki](https://en.wikipedia.org/wiki/Metric_space): distance between any two members
   * 未必是线性空间
3. normed vector space
   * [wiki](https://en.wikipedia.org/wiki/Normed_vector_space)
   * 一定是线性空间
4. inner product space
   * [wiki](https://en.wikipedia.org/wiki/Inner_product_space)
5. linear space即vector space
6. 从大到小排序：topological space, metric space, normed vector space, inner product space

misc

1. Euclidean space
   * [wiki](https://en.wikipedia.org/wiki/Euclidean_space)
   * Euclidea vector space: a finite-dimensional inner product space over the real numbers
2. vector space
   * [wiki](https://en.wikipedia.org/wiki/Vector_space)
   * a vector space over a field $F$ is a set $V$ together with two operatos that satisfy the eight axioms
   * operation: addition, scalar multiplication
   * 加法结合律 associativity of addition `u+(v+w)=(u+v)+w`
   * 加法交换律 commutativity of addition `u+v=v+u`
   * 加法零元 identity element of addition `v+0=v`
   * 加法逆 inverse elements of addition `v+(-v)=0`
   * 数乘结合律 compatibility of scalar multiplication `a(bu)=(ab)u`
   * 数乘单位元 identity element of scalar multiplication `1*u=u`
   * 数乘矢量分配律 distributivity of scalar multiplication with respect to vector `a(u+v)=au+av`
   * 数乘标量分配律 distributivity of scalar multiplication with respect to scalar `(a+b)u=au+bu`
3. inner product space
   * [wiki](https://en.wikipedia.org/wiki/Inner_product_space)
   * an inner product space is a vector space $V$ over the field $F$ together with an inner product
   * conjugate symmetry `<x,y>=<y,x>^H`
   * linearity in the first argument `<ax,y>=a<x,y>` `<x+y,z>=<x,z>+<y,z>`
   * positive-definite
4. metric space
   * [wiki](https://en.wikipedia.org/wiki/Metric_space)
   * a metric space is an ordered pair $(M,d)$ where $M$ is a set and $d$ is a metric (distance function)
   * identity of indisernibles `d(x,y)=0 <=> x=y`
   * symmetry `d(x,y)=d(y,x)`
   * subadditivity / triangle inequality `d(x,z) <= d(x,y) + d(y,z)`
   * complete space
   * compact space
5. topological space
   * [wiki](https://en.wikipedia.org/wiki/Topological_space)
6. Hilbert space
   * [wiki](https://en.wikipedia.org/wiki/Hilbert_space)
   * a Hilbert space $H$ is a real or complex inner produce space that is also a complete metric space with respect to the distance function induced by the inner product
   * pre-Hilbert space：内积空间 + metric space
   * Hilbert space：内积空间 + complete metric space；一个incomplete metric space的栗子见[wiki](https://en.wikipedia.org/wiki/Inner_product_space#Hilbert_space)
   * distance function (norm): symmetric in $x$ and $y$, nonzero, triangle inequality (Cauchy-Schwarz inequality)
