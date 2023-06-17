# 群论

*备注*：关于群论，我暂时没有想到该如何代码验证，代码验证依赖于representation theory

参考资料

1. link
   * 李新征-群论讲义 [link](http://faculty.pku.edu.cn/_tsf/00/0F/yEVrEjjaaEza.pdf)
   * 蔻享/李新征-群论 [link](https://www.koushare.com/video/videodetail/7557)
   * [wiki/小群列表](https://zh.wikipedia.org/wiki/%E5%B0%8F%E7%BE%A4%E5%88%97%E8%A1%A8)
   * proofwiki, [website](https://proofwiki.org/wiki/Main_Page)
   * [youtube-link](https://www.youtube.com/playlist?list=PL22w63XsKjqxPO6pQ8wiZcIrtpTznGSre)
   * [maki-math](https://www.maki-math.com/#/courses/21)
   * [Clemson/MATH4120](http://www.math.clemson.edu/~macaule/classes/f22_math4120/)
   * [Sheaves-blog](https://sheaves.github.io/topics/)
   * [groupprops](https://groupprops.subwiki.org/wiki/Main_Page)
   * [youtube/HKUST/MATH5143/Eric](https://youtube.com/watch?v=fdGGPi4xpYc&feature=shares) introduction to lie algebra
   * small finite-group [website](https://people.maths.bris.ac.uk/~matyd/GroupNames/index.html)
2. book
   * 《群论》 韩其智，孙洪洲，北京大学出版社 [link](https://book.douban.com/subject/3584574//)
   * 《群论讲义》 王宏利，未出版
   * 《群论及其在固体物理中的应用》 徐婉棠，喀兴林，高等教育出版社
   * 《Group Theory: Application to the Phsycics of Condensed Matter》 M. S. Dresselhaus, G. Dresselhaus, A. Jorio, Springer [link](https://www.springer.com/gp/book/9783540328971)
   * 《Group Theory for Physicists》 Zhongqi Ma（马中骐）, World Scientific
   * 《Group Theory in a Nutshell for Physicists》 Anthony Zee [link](https://press.princeton.edu/books/hardcover/9780691162690/group-theory-in-a-nutshell-for-physicists)
3. code
   * GTPack: A Mathematica group theory package for application in solid-state physics and photonics, [arxiv](https://arxiv.org/abs/1807.01245), [frontiersin](https://www.frontiersin.org/articles/10.3389/fphy.2018.00086/full), [website](https://gtpack.org/)
   * [github/IBL-AbstractAlgebra](https://github.com/dcernst/IBL-AbstractAlgebra)
   * [githhub/GAP](https://github.com/gap-system): Group Algorithm Programming
   * [github/WignerD](https://github.com/zichunhao/WignerD)
   * [sage/lie](https://doc.sagemath.org/html/en/reference/spkg/lie.html)
   * [github/jaxlie](https://github.com/brentyi/jaxlie)
4. history
   * Emmy Noether (1882-1935, 德国犹太人)：理体系的对称性与守恒量之间得关系
   * Eugene Paul Wigner（1902-1995，匈牙利人，后加入美国籍）
   * Hermann Klaus Hugo Weyl（1885-1955，德国人）
   * Linus Carl Pauling
5. 有限群理论、转动群、双群、李群，群基础理论，群表示理论
6. 规范场理论：连续变换下的对称性与守恒量的关系
7. conception
   * 自同构 Automorphism $Aut(X)$
   * 自同态 Endomorphism $End(X)$
   * group algebra
   * universal enveloping algebra of Lie algebra
   * irreducible and indecomposable

集合论set

1. link [youtube-link](https://www.youtube.com/playlist?list=PL22w63XsKjqxPO6pQ8wiZcIrtpTznGSre)
2. 栗子
   * $\mathbb{N}_0=\left\{0,1,2,\cdots\right\}$
   * natural number $\mathbb{N}_1=\left\{1,2,3,\cdots\right\}$
   * integer $\mathbb{Z}=\left\{0,\pm 1, \pm 2,\cdots\right\}$
   * rational number $\mathbb{Q}=\left\{ \frac{m}{n} | m,n\in\mathbb{Z},n\ne 0 \right\}$
   * real number $\mathbb{R}=\left\{ \pm x_1x_2x_3\cdots x_n.y_1y_2y_3\cdots | 0\leq x_i,y_i\leq 9 \right\}$
   * complex number $\mathbb{C}=\left\{ a+i | a,b\in\mathbb{R},i^2=-1 \right\}$
   * $2\mathbb{Z}=\left\{ 2n | n\in\mathbb{Z} \right\}$
   * $\mathbb{R}^+=\left\{ x\in\mathbb{R} | x>0 \right\}$
   * $\mathbb{R}^{\ge}=\left\{ x\in\mathbb{R} | x\ge 0 \right\}$
   * $\mathbb{Z}^{\ge}=\left\{ x\in\mathbb{Z} | x\ge 0 \right\}$
   * $\mathbb{Z}^{*}=\left\{ x\in\mathbb{Z} | x\ne 0 \right\}$
   * $U(n)=(\mathbb{Z}/n\mathbb{Z})^\times=\mathbb{Z}_n^\times=\left\{ k+n\mathbb{Z} : 1\leq k\leq n-1, \mathrm{gcd}(k,n)=1 \right\}$ [wiki](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n)
   * $\emptyset$
3. operation
   * subset, improper subset (self), proper subset
   * union
   * intersection, disjoint (no intersection)
   * Cartesian product
   * cardinality
4. function example $f:\mathbb{R}\to\mathbb{R}, f(x)=x^2$
   * domain $\mathbb{R}$, range $\mathbb{R}$, image $\mathbb{R}^\ge$
   * domain $\mathbb{R}$, codomain $\mathbb{R}$, range $\mathbb{R}^\ge$
   * domain $\mathbb{R}$, range $\mathbb{R}^\ge$
   * domain $\mathbb{R}$, codomain $\mathbb{R}$, image $\mathbb{R}^\ge$
5. function
   * definition: set of ordered pair
   * injective 单射的 $\forall x_1\ne x_2, f(x_1) \ne f(x_2)$
   * surjective 满射的
   * composition of function $(g\circ f )(x)=g(f(x))$
   * identity function $i(x)$
   * invertible function $f^{-1}$: bijective = injective + surjective, same cardinality
6. partition
   * one cell (class) in the partition
   * the union of all cells is the set $S$
   * any two cells are disjoint
7. relation $\mathfrak{R}$ on a nonempty set $S$ is a subset of $S\times S$
   * $\left\{ (x,y) | y=2x+1 \right\}$ over set $\mathbb{R}$
   * $\left\{(x,y) | x<y\right\}$ over $\mathbb{R}$
8. equivalence relation $\sim$ on a nonempty set $S$ is a relation on set $S$ that
   * (reflexive) $\forall a \in S, a\sim a$
   * (symmetric) $\forall a,b\in S$, if $a\sim b$, then $b\sim a$
   * (transitive) $\forall a,b,c\in S$, if $a\sim b,b\sim c$, then $a\sim c$
   * example: $\left\{ (m,n) | m-n=0 \bmod 3 \right\}$ over $\mathbb{Z}$
9. equivalence class: let $\sim$ be an equivalence relation defined on a nonempty set $S$. if $x\in S$, then the equivalence class of $x$ is denoted by $[x]$ where $[x]=\left\{ y\in S | y\sim x \right\}$ (partition)
10. principal of mathematical induction
    * well-ordering principal: every nonempty set of positive integers has a least element
11. the division algorithm: if $a$ is any integer and $b$ is any positive integer, then there exist unique integers $q$ and $r$ with $0\leq r<b$, such that $a=qb+r$
    * $327=54*6+3$, quotient, remainder

数论基础 `@number_theory`

群论举栗子

1. $(k,+)$ for $k$ being $\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C},n\mathbb{Z},\mathbb{Z}/n\mathbb{Z}$
2. $(\mathbb{N}_1,\cdot)$ 幺半群
3. $(k,\cdot)$ for $k$ being $\mathbb{Q}^\times,\mathbb{Q}^+,\mathbb{R}^\times,\mathbb{R}^+,\mathbb{C}^\times,\mathbb{C}^+$
4. matrix group $(k^{m\times n},+)$ for $k$ being $\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$
5. general linear group $(GL(n,k),+)$ for $k$ being $\mathbb{Q},\mathbb{R},\mathbb{C}$ [wiki](https://en.wikipedia.org/wiki/General_linear_group)
   * $(GL(n,\mathbb{R}),\cdot)\to (\mathbb{R}^\times,\cdot)$ is a group homomorphism
6. special linear group $(SL(n,k),\cdot)$ for $k$ being $\mathbb{Q},\mathbb{R},\mathbb{C}$ [wiki](https://en.wikipedia.org/wiki/Special_linear_group)
7. orthogonal group $O(V)$ preserves a non-generate quadratic form on a vector space $V$ [wiki](https://en.wikipedia.org/wiki/Orthogonal_group)
8. unitary group $U(V)$ [wiki](https://en.wikipedia.org/wiki/Unitary_group)
9. symplectic group $Sp(V)$ [wiki](https://en.wikipedia.org/wiki/Symplectic_group)
10. cyclic group $C_n=\left\{ x^a : a\in \mathbb{Z} \right\}$ [wiki](https://en.wikipedia.org/wiki/Cyclic_group)
    * $C_n\simeq (\mathbb{Z}/n\mathbb{Z},+)$
    * $\mathbb{Z}/n\mathbb{Z}=\langle 1\rangle=\langle n-1\rangle$, e.g. $\mathbb{Z}/6\mathbb{Z}=\langle 1\rangle=\langle 5\rangle$
    * $\mathbb{Z}=\langle -1 \rangle=\langle 1 \rangle$
11. 二面体群 Dihedral group $D_{n}$ [wiki](https://en.wikipedia.org/wiki/Dihedral_group)
    * $|D_n|=2n$
    * $Z(D_4)=\left\{ e, r^2 \right\}$
12. Klein four-group [wiki](https://en.wikipedia.org/wiki/Klein_four-group)
    * $V=\langle a,b | a^2=b^2=(ab)^2=e \rangle$
    * 四元群仅有 $V$ 和 $C_4$
13. symmetric group $S_n$ [wiki](https://en.wikipedia.org/wiki/Symmetric_group)
    * 置换 permutation: for any set $A$, a bijective function $\phi:A\to A$ is called a permutation of $A$
    * 轮换 cycle
    * 对换 transposition
    * operation: composition of functions
    * $|S_n|=n!$
    * $S_3\simeq D_3$
14. multiplicative group of integers modulo $n$, units modulo $U(n)=((\mathbb{Z}/n\mathbb{Z})^\times, \cdot)$ [wiki](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n)
    * $|\mathbb{Z}_n^\times|=|U(n)|=\phi(n)$ Euler's totient function [wiki](https://en.wikipedia.org/wiki/Euler%27s_totient_function)
    * 特别的，若$p$是一个素数，则$|\mathbb{Z}_p^\times|=p-1$
    * $U(10)$ is cyclic and abelian, $U(12)$ is abelian but not cyclic
15. Lorentz group

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

群论基础

1. 概念
   * 群的阶order $|G|$
   * 有限群、无限群
   * 元素的阶 $x^{|x|}=e$
   * abelian group (commutative group), nonabelian group
   * 重排定理：$aG=G$
   * 子群 $H\triangleleft G$: 封闭，可逆
   * 拉格朗日Lagrange定理：有限子群的阶必为群阶的因子
   * 群直积 $G = G_1 \otimes G_2$: $C_6\simeq C_2 \otimes C_3$
   * 生成元 generator
   * 循环子群 cyclic subgroup：有集合生成的子群
   * 正规子群 normal subgroup: $H<G,\forall a\in G, gH=Hg$
2. 陪集 coset, a subgroup $H$ of group $G$, $G/H$
    * def: $a\sim_L b$ iff $a^{-1}b\in H$
    * def: $a\sim_R b$ iff $ab^{-1}\in H$
    * equivalence relation
    * partition $[a]=\left\{ ah | h\in H \right\}$
    * left/right coset
    * left coset of a normal subgroup is right coset
    * coset只是集合，当$H$是正规子群时$G/H$才构成群（称作商群）
3. centeralizer, normalizer [wiki](https://en.wikipedia.org/wiki/Centralizer_and_normalizer) [wiki1](https://en.wikipedia.org/wiki/Center_(group_theory))
    * centeralizer of a subset $S$ of group $G$: $C_G(S)=\left\{ g\in G:\forall s\in S,gsg^{-1}=s\right\}$
    * center of a group $G$: $Z(G)=C_G(G)$
    * normalizer of a subset $S$ of group $G$: $N_G(S)=\left\{ g\in G: gSg^{-1}=S \right\}$
    * $C_G(S)\subset N_G(S)$
    * $C_G(S)\triangleleft G$
    * $N_G(S)\triangleleft G$
    * normal closure of a subset $S$ of a group $G$: $\mathrm{ncl}_G(S)=\cap_{S\subset N \triangleleft G} N$
4. 群同态 group homomorphism
   * 值域domain, 陪域codomain
   * $f: (G,\cdot)\to(G',*)$是一个群同态, 定义$ker(f)=\left\{ x\in G | f(x)=e' \right\}$, $im(f)=\left\{ f(x) : x\in G \right\}$
   * 核是正规子群 $ker(f)\triangleleft G$, 像是子群 $im(f)<G'$
   * 群同态是单同态iff核是平凡的
   * 从群$G$中任取$x$, 则$f:(\mathbb{Z},+)\to (G,\cdot)$定义为$f(n)=x^n$是一个群同态
   * 元素生成的群 $\langle x \rangle=\left\{ x^n, n\in \mathbb{Z} \right\}$
   * 集合生成的群 $\langle S \rangle=\cap \left\{ H\subset G: H\supset S, H<G \right\}$
5. 群同构第一定理
   * 陪集coset $H<G, \left\{ gH : g\in G \right\}$ [wiki](https://en.wikipedia.org/wiki/Coset)
   * 正规子群normal subgroup [wiki](https://en.wikipedia.org/wiki/Normal_subgroup)
   * 正规化子 normalizer $H<G,N(H)=\left\{ g\in G | gHg^{-1}=H \right\}$
6. 群同构第二定理、群同构第三定理

TODO-00

1. let $G$ be a finite group of even order. show that $G$ has an element $a\ne e$ such that $a^2=e$
2. 群作用 $\phi: G\to \mathrm{Perm}(S)$是一个群同态
   * 例子：左乘，共轭作用
   * 左乘作用大部分元素不是群同态
   * 共轭作用每个元素都是同构（自同构）
   * 内自同构，外自同构
   * 轨道 $\mathrm{Orb}(s)=\left\{ s'\in S: \exists x\in G,s'=xs \right\}=\left\{ xs:x\in G \right\}$
   * 稳定化子 $\mathrm{Stab}(s)=\left\{ x\in G : xs=s \right\}$
   * 群作用每个元素对应集合$S$上的一个划分
   * 稳定化子是子群，一般不是正规子群
3. 群作用对于集合而言，类似于modulo对于环，类似于线性空间对于域
4. 拉格朗日定理：每个有限群的子群的阶整除这个群的阶
5. 费马小定理 Fermat's little theorem: 令$p$是一个素数，而$p\nmid a$, 则 $a^{p-1}\equiv 1 \bmod p$，等价的，$a^p\equiv a \bmod p$ [wiki](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
6. 欧拉定理 Euler's theorem: 令 $n\in \mathbb{N}_2$，而$gcd(a,n)=1$，则 $a^{\phi(n)}\equiv 1 \bmod n$ [wiki](https://en.wikipedia.org/wiki/Euler%27s_theorem)
    * 当$n$是素数，则退化为费马小定理
7. 威尔逊定理 Wilson's theorem: 若$p$是一个奇素数（除了2以外的素数），则 $(p-1)!\equiv -1 \bmod p$ [wiki](https://en.wikipedia.org/wiki/Wilson%27s_theorem)

TODO-01

1. 共轭：给定群中的两个元素`f,h`，如果存在元素`g`，使得`gfg^(-1)=h`，则称`f,h`共轭，记作`f~h`
   * 相互性：`f~h`则`h~f`
   * 传递性：`f~h,h~i`则`f~i`
2. 类：群G中所有相互共轭的元素形成的集合
   * 构造方法：给定元素`a`，遍历所有元素`b`，构造集合`{bab^(-1)`
   * 单元元自身构成一类
   * Abel群每个元素构成一类
   * 共轭元素的阶相等
   * 有限群的每个类中元素的个数都是群阶的因子
   * 类**不是**群：这个集合没有单位元
3. 共轭子群：G的两个子群H和K，若存在元素g使得`K=gHg^(-1)`，则称H和K为共轭子群
   * 两个共轭子群里必有同类的元素
   * 传递性
   * 共轭子群类
4. 同构：群G和群F存在一一映射
   * 一一映射/双射：单射且满射
   * 空间反演群和二阶循环群同构，和二阶置换群同构
   * 给定群的两个共轭子群同构
5. 同态：群G到群F存在满射`h`，称作G与F同态，记作$G\sim F$。即任意元素f，存在元素g使得`f=h(g)`
6. 同态核：设G与F同态，那么G中与F的单位元对应的所有元素的集合称作同态核H
   * 同态核定理：同态核H一定是G的不变子群，商群G/H与F同构
   * D3群核二阶循环群同态，同态核是`{e,d,f}`
7. 自同构映射：群G到自身的同构映射v
   * 自同构群：由群G的自同构映射的集合构成的群，记作`A(G)`；不唯一
   * 三阶循环群的自同构群与二阶循环群同构
8. 内自同构映射：选定群G中元素u，定义映射为`f(g)=ugu^(-1)`
   * 内自同构群：由内自同构映射构成的群
   * 内自同构群是自同构群的不变子群
   * Abel群的内自同构群仅包含恒等变换
9. 变换/置换：非空集合X，值域为自身的一一映射f
   * 定义在集合上的“自同构映射”
   * 完全对称群$S_x$：由所有置换组成的群，即n阶置换群$S_n$
   * 对称/变换群：完全对称群的子群
   * 凯莱定义Cayley：群G同构于其完全对称群$S_G$的一个子群
10. 等价性：集合X上的一个对称群G，集合X中元素`x,y`，若存在群G中元素`g`使得`g(x)=y`，则称x与y等价，记作`x~y`
    * 轨道：集合X上的一个对称群G，集合X中元素x的所有等价元素的集合，称为x的G轨道
    * 不变子集：集合X上的一个对称群G，集合X的子集Y，对Y中任意元素y，y的G轨道包含于Y，则称Y为群G在X上的不变子集
    * X中每个G轨道的集合都是不变子集
    * X中的任意子集Y，总能找到G的子群H，使得Y是群H在X上的不变子集，大不了H只包含恒等变换
    * 迷向子群isotropy subgroup：集合X上的一个变换群G，X中元素x，G的子群H保持x不变，则称H是G对x的迷向子群
11. 半直积$G = G_1 \otimes_s G_2$
    * 半直积群
    * `G1`是`G`的不变子群
    * D3群具备以`G1={e,d,f}, G2={e,a}`为因子形成的半直积结构

TODO-02 MATH4120

1. Klein 4-group $V_4$
   * `{e,h,v,r}`
   * generator: `<h,v>`, `<h,r>`
   * abelian
   * $V_4\cong (\mathbb{F}_2^2,+)$
2. symmetry of a triangle `Tri`
   * `{e,r,f,r^2,rf,r^2f}`
   * generator `<r,f | rf=fr^2>`
   * non-abelian
   * self-inverse: `{e,f,rf,r^2f}`
3. Cayley graph structure
   * undirected arrow: self-inverse
   * unlabeled cayley graph
   * label nodes with configuration of an object
   * label nodes with actions
4. Rubik'cube group
   * Theorem(2010): every configgure of the rubik's cube group is at most 20 moves from the solved state. Moreover, there are configuration that are exactly 20 moves away
   * diameter of a graph: the longest shortest path between any two nodes
5. cyclic groups
6. group presentation `G=<generators | relations>`
7. an infinite group $\langle r,f | f^2=1,rfr=f \rangle$
8. the word problem, isomorphism problem, 4-dimensional sphere problem
9. Frieze group: the symmetry group of a frieze
   * minimal translation to the right $t$, horizontal reflation $h$, vertical reflection $v$, glide-reflection $g$
   * $\mathrm{Frz}_1=\langle t,h,v | h^2=v^2=1,hv=vh,tv=vt,tht=h \rangle$
   * $\mathrm{Frz}_2=\langle g,h | h^2=1,ghg=h \rangle$
   * there are 7 different frieze groups, but only 4 up to isomorphism
10. wallpaper group
    * (1877) 17 different wallpaper groups
11. crystal group, crystallographic group, space group, Fedrov group
    * (1877) 230 space group
12. (1978,2002) 4894 four dimensional symmetry group
13. Cayley table (multiplication table)
    * an element cannot appear twice in the same row or column
    * Latin square: a table where every element appears in every row and column
    * F.W. Light's associativity test: there is no shortcut for determining whether the binary operation in a Latin square is associative
14. quaternion group $Q_8$
    * $Q_8=\langle i,j,k | i^2=j^2=k^2=ijk=-1 \rangle=\langle i,j | i^4=j^4=1,iji=j \rangle$
    * a quotient of a group by a subgroup is isomorphic to $V_4$
15. forbidden Cayley graph ???? page45
16. binary operation
    * a set $S$ is closed under a binary operation $*$
    * associative: $a*(b*c)=(a*b)*c$. parentheses are permitted anywhere, but required nowhere
17. group: a set $G$ satisfying
    * an associative binary operation $*$
    * identity element $e$: $e*g=g*e=g$
    * every element has an inverse $g^{-1}$ s.t. $g*g^{-1}=g^{-1}*g=e$
18. group
    * use $+$ for abelian
    * omit the symbol $*$
    * unique inverse (not part of definition)
    * unique identity  (not part of definition)

## 群表示理论

1. 线性空间，向量空间，向量加法，数乘
   * 向量加法，数乘具有封闭性
   * 加法满足交换律，结合律，零元，逆元
   * 数乘满足`1x=x, (ab)x=a(bx), a(x+y)=ax+ay, (a+b)x=ax+bx`
   * 线性相关，线性无关，线性空间的维数dimension，基矢
   * 线性变换
   * 一般线性变换群：所有非奇异线性变换在“矩阵乘法”（线性空间的连续两次线性变换）运算下构成的群
   * 线性变换群：一般线性变换群的子群
   * 非奇异：因为零没有逆元
2. 群表示，忠实表示
   * 抽象群G与矩阵群的同态映射关系
   * 一维恒等表示/显然表示/平凡表示 (trivial representation)
3. 等价表示：相似变换，但表示空间可以不一样
4. 可约表示，不变的真子空间
   * 区别于不变子群；不变子群的元素是群G中元素（矩阵），而不变真子空间是线性空间中元素（矢量）
   * 直和，完全可约
   * 任何群表示最终都可以化为不可约表示的直和，重复度
   * 对于有限群，表示可约则完全可约
5. 酉表示：酉变换群，酉矩阵群
   * 酉表示可约则完全可约
6. 群空间：群G上定义加法和复数域C上的数乘运算
7. 群代数group ring：对群空间的“矢量”定义乘法规则（之前群的定义中只对群元定义了乘法规则，未包含群空间中的矢量）
    * 可以验证满足结合代数
8. 左正则表示regular representation：抽象群G与线性变换群`{L(g_i)}`的同态映射关系（同构）
   * 左正则表示是群表示的忠实表示
   * 右正则表示
9. Schur's Lemma舒尔引理1：群G在有限维向量空间$V_A$和$V_B$有不可约表示$A$和$B$，若对任意G中元素g，存在线性变换M满足$B(g)M=MA(g)$，则当M不为零时，A与B必等价
    * 两个不等价不可约表示，不能通过一个非零线性变换M联系起来$MA(g)=B(g)M$
10. 舒尔引理2：群G在有限维复空间V上的不可约表示A，对于任意G中元素g，若V上线性变换M满足$MA(g)=A(g)M$，则$M=\lambda E$（常数矩阵）
    * 任意复数域上方阵至少有一个特征值 [math-stackoverflow](https://math.stackexchange.com/q/655634)
11. 有限群在内积空间的每一个表示都有等价的酉表示
12. 群函数，群函数空间

pass 正交性与完备性没有理解，暂且先跳过

1. 特征标：群G的表示A，其特征标定义为`{tr(A(g))}`
   * 特征标是群函数，特征标是类函数
   * 等价的两个表示的特征标相同
   * 共轭元素的特征标相同：不共轭元素的特征标可以相同也可以不同
2. 特征标第一正交定理：有限群不可约表示的特征标满足
   * $(\chi^p,\chi^r)=\frac{1}{n}\sum_{i=1}^{n}\chi^{p*}(g_i)\chi^r(g_i)=\delta_{pr}$
   * 不可约表示与自身的特征标内积是1
3. 类函数
   * 类函数空间的维度是群中类的个数
   * 有限群的所有不等价不可约表示的特征标在类函数空间是完备的
   * 群的不等价不可约表示个数是群中类的个数

## 点群与空间群

1. 点群基础，晶体点群，晶体点阵，空间群（旋转轴，滑移面），三维实正交群（母体）
2. 对称操作，对称元素
3. $O_h$群
4. 正交变换，保内积，实正交群，$O(3)$群，$SO(3)$群（不变子群，保手性），空间反演群，
5. 行列式性质：`det(AB)=det(A)det(B)`, `det(A)=det(A^t)`
6. 点群：第一类点群，第二类点群

## MISC

1. 矩阵直积
   * $(A_1\otimes B_1)(A_2\otimes B_2)=(A_1A_2)\otimes (B_1B_2)$
   * 单位/对角/酉矩阵的直积仍是单位/对角/酉矩阵
   * $tr(A\otimes B)=tr(A)tr(B)$

4阶循环群的特征标表如下，其中$A^p(a)=exp(2\pi i(p-1)/4)$

| - | $1\{e\}$ | $1\{a\}$ | $1\{a^2\}$ | $1\{a^3\}$ |
| :-: | :-: | :-: | :-: | :-: |
| $A^1$ | $1$ | $1$ | $1$ | $1$ |
| $A^2$ | $1$ | $i$ | $-1$ | $-i$ |
| $A^3$ | $1$ | $-1$ | $1$ | $-1$ |
| $A^4$ | $1$ | $-i$ | $-1$ | $i$ |

## matrix Lie group and matrix Lie algebra

栗子

1. general linear group $GL(n;k)$ with $k=\mathbb{R},\mathbb{C}$: invertible matrix
   * nonzero real number $\mathbb{R}^*\simeq GL(1;R)$
   * nozero complex number $\mathbb{C}^*\simeq GL(1;C)$
   * unit complex number $S^1\simeq U(1)$
   * $(\mathbb{R},+)\simeq GL(1;\mathbb{R})^+$: positive determinant
2. special linear group $SL(n;k)$ with $k=\mathbb{R},\mathbb{C}$
   * $x\in GL(n,k), det(x)=1$
3. unitary group $U(n)$
   * $xx^\dagger=x^\dagger x=I_n$
   * norm preserving over $\mathbb{C}$
4. special unitary group $SU(n)$
   * $x\in U(n), det(x)=1$
5. orthogonal group $O(n)$
   * $x\in GL(n,\mathbb{R}), xx^T=x^x=I_n$
   * norm preserving over $\mathbb{R}$
6. special orthogonal group $SO(n)$
   * $x\in O(n), det(x)=1$
7. complex orthogonal group $O(n;\mathbb{C})$
   * $x\in GL(n,\mathbb{C}),x^Tx=xx^T=I_n$
   * $det(x)=\pm 1$
8. special complex orthogonal group $SO(n,\mathbb{C})$
   * $x\in O(n,\mathbb{C}),det(x)=1$
9. indifinite orthogonal group $O(p,q)$
   * [wiki](https://en.wikipedia.org/wiki/Indefinite_orthogonal_group)
   * $x\in GL(p+q,\mathbb{R}),g=diag(1,\cdots,1,-1,\cdots,-1), x^Tgx=g$
   * Lorentz group $O(3,1)$
10. indefinite special orthogonal group $SO(p,q)$
    * $x\in O(p,q),det(x)=1$
11. real symplectic group $Sp(n;\mathbb{R})$
    * $\Omega=(i\sigma_y)\otimes I_n, x\in GL(2n,\mathbb{R}),x^T\Omega x=\Omega$
    * $det(x)=1$
    * TODO how to generate
12. complex symplectic group $Sp(n;\mathbb{C})$
    * $\Omega=(i\sigma_y)\otimes I_n, x\in GL(2n,\mathbb{C}),x^T\Omega x=\Omega$
    * $det(x)=1$
    * TODO how to generate
13. compact symplectic group $Sp(n)=Sp(n;\mathbb{C}) \cap U(2n)$
    * conjugate operator: $Pz=\bar{z}$
    * $J=(i\sigma_y\otimes I_n)P$
    * 等价定义 $Sp(n)=\left\{ x: x^\dagger x=xx^\dagger=I_{2n}, xJ=Jx \right\}$
    * unitary group over the quaternions
    * norm preserving over quaternion
    * TODO how to generate
14. Euclidean group $E(n)$
    * $\left\{ (x,R):x\in\mathbb{R}^n,R\in O(n) \right\}$
    * $\left\{ x,R\right\} y=Ry+x$
15. Poincare group, inhomogeneous Lorentz group $P(n;1)$
16. Heisenberg group
    * Heisenberg-Weyl commutation relation
    * Baker-Campbell-Hausdorff ofrmula

concept

1. matrix Lie group: closed subgroup of $GL(n, \mathbb{C})$
   * a non-closed subgroup of $GL(n,\mathbb{C})$: $GL(n,\mathbb{Q})$
   * irrational line in a torus
2. Lie group but not matrix Lie group
   * $G=\mathbb{R}\times\mathbb{R}\times S^1=\left\{(x,y,u):x\in\mathbb{R},y\in\mathbb{R},u\in S^1\subset \mathbb{C}\right\}$
   * $(x_1,y_1,u_1)\cdot (x_2,y_2,u_2)=(x_1+x_2,y_1+y_2,e^{ix_1y_2}u_1u_2)$
3. manifold
4. quaternion algebra $\mathcal{H}$ [wiki](https://en.wikipedia.org/wiki/Quaternion): real linear combination of $I,i\sigma_z,i\sigma_y,i\sigma_x$
5. Jordan-Chevalley decomposition [wiki](https://en.wikipedia.org/wiki/Jordan%E2%80%93Chevalley_decomposition)

TODO

1. package
   * [github/mmgroup](https://github.com/Martin-Seysen/mmgroup) monster groups

## Lie algebra

1. link
   * [github/specialunitary](https://github.com/xalhs/specialunitary)
   * [github/SU-tools](https://github.com/hellpig/SU-tools)
