# ring

参考资料

1. [maki-math](https://www.maki-math.com/#/courses/21)
2. [youtube/abstract-algebra](https://www.youtube.com/playlist?list=PLi01XoE8jYoi3SgnnGorR_XOW3IcK-TP6)

举栗子

1. 多项式环 polynomial ring $k\left[ X_1,\cdots,X_n \right]$ for $k$ being $\mathbb{Z},n\mathbb{Z},\mathbb{R}/n\mathbb{R},\mathbb{Q},\mathbb{R},\mathbb{C},M_n(k)$ [wiki](https://en.wikipedia.org/wiki/Polynomial_ring)
   * indeterminate, monomial, degree
   * non-commutative polynomial rings $k\left\{x,y\right\}$ on basis $1,x,y,x^2,xy,yx,y^2,\cdots$
2. $(n\mathbb{Z},+,\cdot)$
   * no identity $1$
3. $(\mathbb{Z}/n\mathbb{Z},+,\cdot)$
   * $(\mathbb{Z}/n\mathbb{Z},+)$ $n$阶循环群
   * $(\mathbb{Z}/n\mathbb{Z},\cdot)$ 幺半群
   * $(\mathbb{Z}_n^\times,\cdot)$ 构成群
4. $(\mathbb{R}^{n\times n},+,\cdot)$
5. 零环 zero ring $(0,+,\cdot)$
   * 一个环是零环当且仅当加法单位元等于乘法单位元
6. 四元数环 Quaternion $a+bi+cj+dk$ [wiki](https://en.wikipedia.org/wiki/Quaternion)
7. Gaussian integer $\mathbb{Z}[i]=\left\{ a+bi : a,b\in\mathbb{Z} \right\}$ [wiki](https://en.wikipedia.org/wiki/Gaussian_integer)
8. matrix ring $M_n(k)$ for $k$ being $\mathbb{Q}, \mathbb{R}, \mathbb{C}$ [wiki](https://en.wikipedia.org/wiki/Matrix_ring)
9. quadratic integer
10. group rings [wiki](https://en.wikipedia.org/wiki/Group_ring)
11. ring of differeniate operator (non-commutative)
12. lie algebra
13. clifford algebra
14. 零环 zero ring

层次结构

1. 环ring $(R,+,\cdot)$ 由集合 $G$ 和两种二元运算 $+\cdot$ 构成 [wiki](https://en.wikipedia.org/wiki/Ring_(mathematics))
   * $(R,+)$为交换群
   * $(R,\cdot)$为幺半群
   * 分配率 distributive law $a\cdot (b+c)=(a\cdot b)+(a\cdot c)$, $(a+b)\cdot c=(a\cdot c)+(b\cdot c)$
   * 注：通常记 $+$ 单位元为 $0$，通常不显示写出算符 $\cdot$，通常记 $+$ 逆元为 $-a$，通常称 $+$ 为加法，称 $\cdot$ 为乘法
   * 注：$a0=0a=0$, $a^{-1}b=ab^{-1}=(ab)^{-1}$
   * 注：$(R^\times,\cdot)$: 所有乘法可逆元素构成的群
2. 交换环 commutative ring $(R,+,\cdot)$ [wiki](https://en.wikipedia.org/wiki/Commutative_ring)
   * $(R,+,\cdot)$是环
   * $a\cdot b=b\cdot a$
3. 除环 $(R,+,\cdot)$ [wiki](https://en.wikipedia.org/wiki/Division_ring)
   * $(R,+,\cdot)$是环
   * $R\setminus \left\{ 0 \right\}=R^\times$
4. 无零因子环 domain, a nonzero ring with no nontrivial zero divisor
   * 等价定义：$R\setminus\left\{0\right\}$对 $\cdot$ 封闭
   * 等价定义：$R$ 中非零元素的乘积非零
5. 整环 integral domain：无零因子的交换环 [wiki](https://en.wikipedia.org/wiki/Integral_domain)
6. 唯一分解整环unique factorization domain (UFD) [wiki](https://en.wikipedia.org/wiki/Unique_factorization_domain)
7. 主理想环principal ideal ring：每个理想均可由单个元素生成的环 [wiki](https://en.wikipedia.org/wiki/Principal_ideal_ring)
8. 主理想整环 principal ideal domain (PID) [wiki](https://en.wikipedia.org/wiki/Principal_ideal_domain)
9. 单环simple ring
   * 定义：乘法单位元，极大理想是零理想
10. 诺特环Noetherian ring [wiki](https://en.wikipedia.org/wiki/Noetherian_ring)
    * 环$A$的每个理想都是有限生成的

基础知识

1. 子环 $S<R$: $0,1\in S$, $a+b,ab\in S$, $-a\in S$
   * 由集合生成的子环 $\langle A\rangle=\cap \left\{ S\subset R: S\supset A, S<R \right\}$
2. 概念
   * 环直积
3. 理想ideal $I\triangleleft R$ [wiki](https://en.wikipedia.org/wiki/Ideal_(ring_theory))
   * left ideal $(I,+)<(R,+)$, $\forall r\in R, \forall a\in I, ra\in I$
   * right ideal $(I,+)<(R,+)$, $\forall r\in R, \forall a\in I, ar\in I$
   * $n\mathbb{Z}\triangleleft \mathbb{Z}$
   * quotient ring $R/I$
   * $(I,+)$是子群
   * 给定环$(R,+,\cdot)$, 集合$A$生成的理想 $(A)=\cap \left\{ I\subset R : I\supset A, I\triangleleft R\right\}$
   * 给定两个理想$I,J$, 则$I+J=(I\cup J)$
4. 交换环$(R,+,\cdot)$, 理想$I,J,K\triangleleft R$
   * 有限集合生成的理想 $(a_1,\cdots, a_n)=Ra_1+\cdots +Ra_n$
   * $IJ:=(\left\{ ab: a\in I, b\in J \right\})=\left\{a_1b_1+\cdots +a_nb_n:a_1,\cdots,a_n\in I,b_1,\cdots,b_n\in J \right\}$ 元素乘积的有限和构成的集合
   * $IJ\subset I\cap J \subset I+J$, 例如 $I=4\mathbb{Z},J=6\mathbb{Z}$，则$IJ=24\mathbb{Z}$, $I\cap J=12\mathbb{Z}$, $I+J=2\mathbb{Z}$
   * $(I\cap J)(I+J)\subset IJ$: TODO 啥时是真包含？
   * $I\cap (J+K)\supset I\cap J+I\cap K$ 啥时是真包含？
   * 若 $I+J=R$，则称$I,J$互素
5. 环同态 $f: (R,+,\cdot)\to (R',+',*)$
   * $f(1)=1'$, $f(a+b)=f(a)+'f(b)$, $f(ab)=f(a)*f(b)$
   * 核是理想$ker(f)\triangleleft R$
   * 像是子环$im(f)<R'$
   * 环同构第一定理：$R/ker(f)\simeq im(f)$
   * 环同构第二定理: 令$(R,+,\cdot)$是一个环，而$S<R,I\triangleleft R$，则 $S+I<R$, $S\cap I\triangleleft S$, $I\triangleleft S+I$，且$S/(S\cap I)\simeq (S+I)/I$
   * 环同构第三定理: 令$(R,+,\cdot)$是一个环，而$I,J\triangleleft R$，且$I\subset J$，则$J/I\triangleleft R/I$，且$(R/I)/(J/I)\simeq R/J$
6. 零因子zero divisor
   * 左零因子left zero divisor：非零元素$a$是左零因子，iff存在非零元素$b$使得$ab=0$
   * 右零因子right zero divisor：非零元素$a$是右零因子，iff存在非零元素$b$使得$ba=0$
   * left regular (left cancellable), right regular (right cancellable)
   * zero divisor: either left zero divisor or right zero divisor
   * nontrivial (nonzero) zero divisor
   * a nonzero ring with no nontrivial zero divisor is called domain
7. 幂零元 nilpotent：环 $R$ 的一个元素 $x$ 是一个幂零元，则存在一个正整数 $n$, 使得 $x^n$ 等于加法中的零元
8. 理想ideal $I\triangleleft R$ [wiki](https://en.wikipedia.org/wiki/Ideal_(ring_theory))
   * 除环中的（左或右）理想只有平凡（左或右）理想
   * 主理想 primary ideal：能被一个元素生成的理想
   * 素理想 prime ideal
   * 极大理想 maximal ideal
   * 一个理想是子环当且仅当它是整个环
   * 集合生成的理想: $(A)=\cap \left\{ I\subset R: I\supset A, I\triangleleft R \right\}$
   * 令$(R,+,\cdot)$是一个环，而$I,J\triangleleft R$，则 $I+J=\left\{ a+b: a\in \right\}=(I\cup J)\triangleleft R$
9. Bezout's identity 若 $a,b,c\in\mathbb{N}_1$，则$ax+by=c$有整数解$x,y$当且仅当$\mathrm{gcd}(a,b)|c$ [wiki](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity)
10. Bezout's theorem [wiki](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_theorem)

TODO-00

1. do rings have 1: in this course, yes
   * ring $R$ without 1 can be converted into a ring with 1: $Z\oplus R$
   * ring without 1: locally compact space
   * ring with 1: compact space
2. ring homomorphism of rings $R$ and $S$: $f:R\mapsto S$
   * $f(a+b)=f(a)+f(b)$
   * $f(ab)=f(a)f(b)$
   * $f(1)=1$
3. ideal $I$ of ring $R$ is the kernel of a homomorphism from $R$ to some ring $S$
   * $\mathbb{Z}\subset \mathbb{Q}$, $\mathbb{Z}$ is a subring, not an ideal
   * ideal is a ring without 1
4. quotient
   * $\mathbb{Z}/n\mathbb{Z}$
   * $\mathbb{R}[x]/(x^2+1)=\mathbb{C}$ [proofwiki](https://proofwiki.org/wiki/Complex_Numbers_as_Quotient_Ring_of_Real_Polynomial)
   * $k[x,y]/(y^2-x^3+x)$
5. modules $M$ over ring $R$ is like vector space over a field [wiki](https://en.wikipedia.org/wiki/Vector_space) [wiki](https://en.wikipedia.org/wiki/Module_(mathematics))
   * vector field是一个Abelian群加上数乘，module是一个Abelian群再加上环乘
   * $R\times M\mapsto M$, $rm$
   * $(r_1r_2)m=r_1(r_2m)$
   * $(r_1+r_2)m=r_1m+r_2m$
   * $r(m_1+m_2)=rm_1+rm_2$
   * $1m=m$
6. special modules
   * $\mathbb{Z}$-modules: abelian groups (finite abelian groups can be written as a direct product of cyclic groups)
   * $k$-modules for some field $k$: vector space
   * $k[x]$-module for some polynomial ring $k[x]$: linear transformation
   * 环也是一个module (module over self)
   * submodule of $R$: ideal
   * $R/I$: quotient ring (quotient ring $R/I$ is a module over ring $R$)
7. special modules
    * submodules $M\subseteq N$, we can define the quotient $N/M$ which is still a module
    * subideal $I\subseteq J$, we can define the quotient $J/I$ which is not an ideal
8. compare
   * group $G$
     * act on set $S$
     * quotient over normal subgroup $G/N$
   * ring $R$
     * act on module $M$
     * quotient over ideal $R/I$

## 域field

举栗子

1. $(k,+,\cdot)$ for $k$ being $\mathbb{Q},\mathbb{R},\mathbb{C}$

基础知识

1. 域field $(F,+,\cdot)$ [wiki](https://en.wikipedia.org/wiki/Field_(mathematics))
   * $(F,+,\cdot)$为除环
   * $\cdot$ 可交换
2. 有限域finite field, 又称作伽罗瓦域Galois field
3. characteristic
   * zero: the subfield of complex number, p-adic fields
   * prime number $p$: finite field $\mathrm{GF}(p^n)$
