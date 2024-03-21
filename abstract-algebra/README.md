# Abstract algebra

notation

1. isomorphic $\cong$
2. homomorphism $\simeq$
3. homotopic $\sim$

层次关系

1. [wiki/list-of-algebra](https://en.wikipedia.org/wiki/List_of_algebras)
2. 线性代数R（或称代数）：定义在数域K上的线性空间，线性空间中元素$\vec{x},\vec{y},\vec{z}$，数域上元素$a$，定义乘法
   * 乘法封闭：$\vec{x}\vec{y} \in R$
   * 乘法分配率：$\vec{x}(\vec{y}+\vec{z})=\vec{x}\vec{y}+\vec{x}\vec{z}$
   * 数乘结合交换率：$a(\vec{x}\vec{y})=(a\vec{x})\vec{y}=\vec{x}(a\vec{y})$
3. 结合代数：在线性代数的基础上定义乘法结合律$(\vec{x}\vec{y})\vec{z}=\vec{x}(\vec{y}\vec{z})$
   * 非结合代数non-associative algebra [wiki](https://en.wikipedia.org/wiki/Non-associative_algebra)：叉乘outer product
4. 半群 semigroup $(G,\cdot)$ 由集合 $G$ 和二元运算 $\cdot$ 构成 [wiki](https://en.wikipedia.org/wiki/Semigroup)
   * 封闭性：$\forall a,b\in G,a\cdot b\in G$
   * 结合律：$\forall a,b,c\in G, (a\cdot b)\cdot c=a\cdot (b\cdot c)$, 可归纳为最多有限次的结合律
5. 幺半群 Monoid $(G,\cdot)$ [wiki](https://en.wikipedia.org/wiki/Monoid)
   * $(G,\cdot)$为半群
   * 单位元：$\exist e\in G, \forall a\in G, e\cdot a=a\cdot e=a$
   * 注：可逆元素组成的集合形成群
6. 群 group $(G,\cdot)$
   * $(G,\cdot)$为幺半群
   * 逆元：$\forall a\in G, \exist b\in G, a\cdot b=b\cdot a=e$
7. 交换群 Abelian group $(G,\cdot)$
   * 群group
   * 交换律：$\forall a,b\in G, a\cdot b=b\cdot a$
8. 循环群 cyclic group

## set theory

举栗子

1. $\mathbb{N}_0=\left\{0,1,2,\cdots\right\}$
2. natural number $\mathbb{N}_1=\left\{1,2,3,\cdots\right\}$
3. integer $\mathbb{Z}=\left\{0,\pm 1, \pm 2,\cdots\right\}$
4. rational number $\mathbb{Q}=\left\{ \frac{m}{n} | m,n\in\mathbb{Z},n\ne 0 \right\}$
5. real number $\mathbb{R}=\left\{ \pm x_1x_2x_3\cdots x_n.y_1y_2y_3\cdots | 0\leq x_i,y_i\leq 9 \right\}$
6. complex number $\mathbb{C}=\left\{ a+i | a,b\in\mathbb{R},i^2=-1 \right\}$
7. $2\mathbb{Z}=\left\{ 2n | n\in\mathbb{Z} \right\}$
8. $\mathbb{R}^+=\left\{ x\in\mathbb{R} | x>0 \right\}$
9. $\mathbb{R}^{\ge}=\left\{ x\in\mathbb{R} | x\ge 0 \right\}$
10. $\mathbb{Z}^{\ge}=\left\{ x\in\mathbb{Z} | x\ge 0 \right\}$
11. $\mathbb{Z}^{*}=\left\{ x\in\mathbb{Z} | x\ne 0 \right\}$
12. $U(n)=(\mathbb{Z}/n\mathbb{Z})^\times=\mathbb{Z}_n^\times=\left\{ k+n\mathbb{Z} : 1\leq k\leq n-1, \mathrm{gcd}(k,n)=1 \right\}$ [wiki](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n)
13. $\emptyset$

concept

1. [youtube-link](https://www.youtube.com/playlist?list=PL22w63XsKjqxPO6pQ8wiZcIrtpTznGSre)
2. operation
   * subset, improper subset (self), proper subset
   * union
   * intersection, disjoint (no intersection)
   * Cartesian product
   * cardinality
3. function example $f:\mathbb{R}\to\mathbb{R}, f(x)=x^2$
   * domain $\mathbb{R}$, range $\mathbb{R}$, image $\mathbb{R}^\ge$
   * domain $\mathbb{R}$, codomain $\mathbb{R}$, range $\mathbb{R}^\ge$
   * domain $\mathbb{R}$, range $\mathbb{R}^\ge$
   * domain $\mathbb{R}$, codomain $\mathbb{R}$, image $\mathbb{R}^\ge$
4. function
   * definition: set of ordered pair
   * injective 单射的 $\forall x_1\ne x_2, f(x_1) \ne f(x_2)$
   * surjective 满射的
   * composition of function $(g\circ f )(x)=g(f(x))$
   * identity function $i(x)$
   * invertible function $f^{-1}$: bijective = injective + surjective, same cardinality
5. partition
   * one cell (class) in the partition
   * the union of all cells is the set $S$
   * any two cells are disjoint
6. relation $\mathfrak{R}$ on a nonempty set $S$ is a subset of $S\times S$
   * $\left\{ (x,y) | y=2x+1 \right\}$ over set $\mathbb{R}$
   * $\left\{(x,y) | x<y\right\}$ over $\mathbb{R}$
7. equivalence relation $\sim$ on a nonempty set $S$ is a relation on set $S$ that
   * (reflexive) $\forall a \in S, a\sim a$
   * (symmetric) $\forall a,b\in S$, if $a\sim b$, then $b\sim a$
   * (transitive) $\forall a,b,c\in S$, if $a\sim b,b\sim c$, then $a\sim c$
   * example: $\left\{ (m,n) | m-n=0 \bmod 3 \right\}$ over $\mathbb{Z}$
8. equivalence class: let $\sim$ be an equivalence relation defined on a nonempty set $S$. if $x\in S$, then the equivalence class of $x$ is denoted by $[x]$ where $[x]=\left\{ y\in S | y\sim x \right\}$ (partition)
9. principal of mathematical induction
   * well-ordering principal: every nonempty set of positive integers has a least element
10. the division algorithm: if $a$ is any integer and $b$ is any positive integer, then there exist unique integers $q$ and $r$ with $0\leq r<b$, such that $a=qb+r$
    * $327=54*6+3$, quotient, remainder
