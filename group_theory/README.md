# group theory

1. link
   * [koushare-link](https://www.koushare.com/video/videodetail/7557) [lecture-pdf-link](http://faculty.pku.edu.cn/_tsf/00/0F/yEVrEjjaaEza.pdf) 蔻享/李新征-群论
   * [wiki-link](https://en.wikipedia.org/wiki/List_of_small_groups) [groupnames.org](https://people.maths.bris.ac.uk/~matyd/GroupNames/index.html) list of small groups
   * [maki-math](https://www.maki-math.com/#/courses/21)
   * [Clemson/MATH4120-course-page](http://www.math.clemson.edu/~macaule/classes/f22_math4120/) [homepage](https://www.math.clemson.edu/~macaule/) Matthew Macauley,
   * [youtube-link](https://youtube.com/playlist?list=PLwV-9DG53NDxU337smpTwm6sef4x-SCLv&si=P4FQDjwrwcRQjBBW) visual group theory
   * [groupprops](https://groupprops.subwiki.org/wiki/Main_Page)
   * [youtube/HKUST/MATH5143/Eric](https://youtube.com/watch?v=fdGGPi4xpYc&feature=shares) introduction to lie algebra
   * [github-link](https://github.com/nathancarter/group-explorer) group explorer
   * [Sheaves-blog](https://sheaves.github.io/topics/)
2. book
   * 群论, 韩其智，孙洪洲，北京大学出版社 [link](https://book.douban.com/subject/3584574//)
   * 群论讲义, 王宏利，未出版
   * 群论及其在固体物理中的应用, 徐婉棠，喀兴林，高等教育出版社
   * Group Theory: Application to the Phsycics of Condensed Matter, M. S. Dresselhaus, G. Dresselhaus, A. Jorio, Springer [link](https://www.springer.com/gp/book/9783540328971)
   * Group Theory for Physicists, Zhongqi Ma（马中骐）, World Scientific
   * Group Theory in a Nutshell for Physicists, Anthony Zee [link](https://press.princeton.edu/books/hardcover/9780691162690/group-theory-in-a-nutshell-for-physicists)
3. code
   * GTPack: A Mathematica group theory package for application in solid-state physics and photonics, [arxiv](https://arxiv.org/abs/1807.01245), [frontiersin](https://www.frontiersin.org/articles/10.3389/fphy.2018.00086/full), [website](https://gtpack.org/)
   * [github/IBL-AbstractAlgebra](https://github.com/dcernst/IBL-AbstractAlgebra)
   * [githhub/GAP](https://github.com/gap-system): Group Algorithm Programming
   * [github/WignerD](https://github.com/zichunhao/WignerD)
   * [sage/lie](https://doc.sagemath.org/html/en/reference/spkg/lie.html)
   * [github/jaxlie](https://github.com/brentyi/jaxlie)
   * [github/mmgroup](https://github.com/Martin-Seysen/mmgroup) monster groups
4. history
   * Emmy Noether (1882-1935, 德国犹太人)：理体系的对称性与守恒量之间得关系
   * Eugene Paul Wigner（1902-1995，匈牙利人，后加入美国籍）
   * Hermann Klaus Hugo Weyl（1885-1955，德国人）
   * Linus Carl Pauling
   * [wiki-link](https://en.wikipedia.org/wiki/Platonic_solid) Platonic solid
5. concept
   * 自同构 Automorphism $Aut(X)$
   * 自同态 Endomorphism $End(X)$
   * group algebra
   * universal enveloping algebra of Lie algebra
   * irreducible and indecomposable
6. extension
   * 有限群理论
   * 转动群
   * 双群
   * 李群
   * 群基础理论
   * 群表示理论

举栗子

1. $(k,+)$ for $k$ being $\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C},n\mathbb{Z},\mathbb{Z}/n\mathbb{Z}$ or finite field $\mathbb{F}_q$
2. $(\mathbb{N}_1,\cdot)$ 幺半群
3. $(k,\cdot)$ for $k$ being $\mathbb{Q}^\times,\mathbb{Q}^+,\mathbb{R}^\times,\mathbb{R}^+,\mathbb{C}^\times,\mathbb{C}^+$
4. matrix group $(k^{m\times n},+)$ for $k$ being $\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$
5. Lie group
   * general linear group $(GL(n,k),+)$ for $k$ being $\mathbb{Q},\mathbb{R},\mathbb{C}$ [wiki](https://en.wikipedia.org/wiki/General_linear_group)
   * special linear group $(SL(n,k),\cdot)$ for $k$ being $\mathbb{Q},\mathbb{R},\mathbb{C}$ [wiki](https://en.wikipedia.org/wiki/Special_linear_group)
   * orthogonal group [wiki](https://en.wikipedia.org/wiki/Orthogonal_group)
   * unitary group [wiki](https://en.wikipedia.org/wiki/Unitary_group)
   * symplectic group $Sp(V)$ [wiki](https://en.wikipedia.org/wiki/Symplectic_group)
6. [wiki-link](https://en.wikipedia.org/wiki/Cyclic_group) cyclic group $C_n=\left\{ r^a : a=0,1,\cdots,n-1 \right\}=\langle r|r^n=e \rangle$
   * $C_n\cong (\mathbb{Z}/n\mathbb{Z},+)$
   * $\mathbb{Z}/n\mathbb{Z}=\langle 1\rangle=\langle n-1\rangle$
   * $\mathbb{Z}=\langle -1 \rangle=\langle 1 \rangle$
7. [wiki-link](https://en.wikipedia.org/wiki/Dihedral_group) Dihedral group $D_n$
   * $D_n=\langle r,f| r^n=f^2=rfrf=e \rangle$
   * $D_n=\langle s,t| (st)^n=t^2=s^2=e \rangle$
   * $D_\infty=\langle r,f | f^2=rfrf=e \rangle$
   * $|D_n|=2n$
   * quotient group $D_n/C_n\cong C_2$
   * $Z(D_4)=\left\{ e, r^2 \right\}$
8. [wiki](https://en.wikipedia.org/wiki/Klein_four-group) Klein four-group, Kleinsche Vierergruppe
   * $V=\langle a,b : a^2=b^2=(ab)^2=e \rangle\cong C_2\times C_2$
9. [wiki-link](https://en.wikipedia.org/wiki/Symmetric_group) symmetric group $S_n$
   * $S_n=\langle (1\; 2),(2\; 3),\cdots,(n-1\; n) \rangle$ (not group presentation)
   * $|S_n|=n!$
   * $S_3\cong D_3$
   * [wiki-link](https://en.wikipedia.org/wiki/Permutation_group) permutation group: subgroup of $S_n$
10. [wiki-link](https://en.wikipedia.org/wiki/Alternating_group) alternating group $A_n$
    * $A_n=\left\{ \sigma\in S_n : \mathrm{sgn}(\sigma)=1 \right\}$
    * $A_4/V_4\cong C_3$
11. [wiki-link](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n) multiplicative group of integers modulo $n$, units modulo $U(n)=((\mathbb{Z}/n\mathbb{Z})^\times, \cdot)$
    * [wiki-link](https://en.wikipedia.org/wiki/Euler%27s_totient_function) $|U(n)|=\phi(n)$ Euler's totient function
    * $U(10)\cong C_4$, $U(12)\cong C_2\times C_2$
12. Lorentz group
13. extra special group [wiki-link](https://en.wikipedia.org/wiki/Extra_special_group)
    * Pauli group is an extra special group of $p=2$
14. Heisenberg group [wiki-link](https://en.wikipedia.org/wiki/Heisenberg_group)
    * Pauli group is isomorphic to the Heisenberg group over a finite field [stackexchange-link](https://quantumcomputing.stackexchange.com/q/26351)
15. [wiki-link](https://en.wikipedia.org/wiki/Frieze_group) Frieze group: 7 different frieze groups
    * minimal translation to the right $t$, horizontal reflation $h$, vertical reflection $v$, glide-reflection $g$
    * $\mathrm{Frz}_1=\langle t,h,v | h^2=v^2=1,hv=vh,tv=vt,tht=h \rangle$
    * $\mathrm{Frz}_2=\langle g,h | h^2=1,ghg=h \rangle$
    * there are 7 different frieze groups, but only 4 up to isomorphism
16. [wiki-link](https://en.wikipedia.org/wiki/Wallpaper_group) wallpaper group
    * (1877) 17 different wallpaper groups
17. [wiki-link](https://en.wikipedia.org/wiki/Space_group) space group
    * alias: crystal group, crystallographic group, space group, Fedrov group
    * (1891) 230 space group
    * (1978,2002) 4894 four dimensional point group
18. [wiki-link](https://en.wikipedia.org/wiki/Braid_group) braid group
19. [wiki-link](https://en.wikipedia.org/wiki/Rubik%27s_Cube_group) Rubik's Cube group
    * 1974 Rubik's Cube, Erno Rubik
    * Theorem(2010): every configgure of the rubik's cube group is at most 20 moves from the solved state. Moreover, there are configuration that are exactly 20 moves away
    * diameter of a graph: the longest shortest path between any two nodes
20. [wiki-link](https://en.wikipedia.org/wiki/Quaternion_group) quaternion group $Q_8$
    * $Q_8=\langle i,j,k | i^2=j^2=k^2=ijk=-1 \rangle=\langle i,j | i^4=j^4=1,iji=j \rangle$
    * a quotient of a group by a subgroup is isomorphic to $V_4$
    * $Q_8/C_2\cong V_4$, $Q_8/V_4\cong C_2$, but $Q_8\ne C_2\times V_4$

notation

1. isomorphic $\cong$: bijection
2. homomorphism $\simeq$
3. homotopic $\sim$
4. order
   * group order $|G|$
   * element order $|x|$: the smallest positive integer s.t. $x^{|x|}=e$
5. [wiki-link/subgroup](https://en.wikipedia.org/wiki/Subgroup) [wiki-link/coset](https://en.wikipedia.org/wiki/Coset) subgroup $H<G$
   * left coset $gH$, equivalence relation $a\sim_L b$ iff $a^{-1}b\in H$
   * right coset $Hg$, equivalence relation $a\sim_R b$ iff $ab^{-1}\in H$
   * index $[G:H]=\frac{|G|}{|H|}$
6. [wiki](https://en.wikipedia.org/wiki/Normal_subgroup) normal subgroup $H\triangleleft G$
   * def: $\forall g\in G, gH=Hg$
   * quotient group $G/H$
7. generator group $\langle x \rangle$
   * one element $\langle x \rangle=\left\{ x^n, n\in \mathbb{Z} \right\}$
   * subset $\langle S \rangle=\cap \left\{ H< G: S\subseteq H \right\}$
8. [wiki-link](https://en.wikipedia.org/wiki/Centralizer_and_normalizer) centeralizer, normalizer, center
   * centralizer of a subset $S$ of group $G$: $C_G(S)=\left\{ g\in G:\forall s\in S,gsg^{-1}=s\right\}$
   * normalizer of a subset $S$ of group $G$: $N_G(S)=\left\{ g\in G: gSg^{-1}=S \right\}$
   * $C_G(S)\subset N_G(S)$
   * $C_G(S)\triangleleft G$
   * $N_G(S)\triangleleft G$
   * [wiki-link](https://en.wikipedia.org/wiki/Center_(group_theory)) center of a group $G$: $Z(G)=C_G(G)$
   * when $S$ is a subgroup, $N_G(S)$ is union of those left cosets equal to right cosets
   * normal closure of a subset $S$ of a group $G$: $\mathrm{ncl}_G(S)=\cap \left\{ N \triangleleft G: S\subseteq N \right\}$
9. product
    * [wiki-link](https://en.wikipedia.org/wiki/Direct_product_of_groups) direct product $G_1\times G_2=\left\{ (g_1,g_2):g_1\in G_1,g_2\in G_2 \right\}$
      * $C_6\cong C_2 \times C_3$
    * [wiki-link](https://en.wikipedia.org/wiki/Free_product) free product $G_1*G_2$
10. group homomorphism $f: (G,\cdot)\to(G',*)$
    * $\ker(f)=\left\{ x\in G : f(x)=e' \right\}$
    * $\mathrm{Im}(f)=\left\{ f(x) : x\in G \right\}$
    * $\ker(f)\triangleleft G$
    * $\mathrm{Im}(f)<G'$
    * one-to-one homomorphism: monomorphism, embedding
    * surjective homomorphism: epimorphism
    * multi-to-one homomorphism: quotient
    * example
      * $(GL(n,\mathbb{R}),\cdot)\to (\mathbb{R}^\times,\cdot)$ with $f(A)=\det(A)$
11. [wiki-link](https://en.wikipedia.org/wiki/Conjugacy_class) conjugate, conjugacy class
    * $a\sim b$ iff $\exist g\in G, b=gag^{-1}$
    * class $[a]=\left\{ gag^{-1} : g\in G \right\}$
    * class number $|[a]|=[G:C_G(a)]$
    * if $a\sim b$, then $|a|=|b|$
    * subset $S\subseteq G$: $[S]=\left\{ gSg^{-1} : g\in G \right\}$
    * subgroup $H< G$: $[H]=\left\{ gHg^{-1} : g\in G \right\}$, two conjugate subgroups are isormorphic (reverse is not true)
12. [wiki-link](https://en.wikipedia.org/wiki/Presentation_of_a_group) presentation of a group
    * $\langle S | R\rangle$: isomorphic to the quotient of a free group on $S$ by the normal subgroup generated by the relation $R$
    * [wiki-link](https://en.wikipedia.org/wiki/Absolute_presentation_of_a_group) absolute presentation of a group
13. [wiki-link](https://en.wikipedia.org/wiki/Cayley_graph) Cayley diagram
    * alias: Cayley graph, Cayley color graph, Cayley color diagram, group diagram, color group
    * nodes (group element/action), directed edge (group generator)
    * one group can have multiple Cayley diagrams (via different generators)
    * regular directed graph
14. [wiki-link](https://en.wikipedia.org/wiki/Cayley_table) Cayley table
    * alias: multiplication table
    * [wiki-link](https://en.wikipedia.org/wiki/Light%27s_associativity_test) Light's associativity test: there is no shortcut for determining whether the binary operation in a Latin square is associative
15. [wiki-link](https://en.wikipedia.org/wiki/Cycle_graph_(algebra)) cycle group
    * def: undirected graph that illustrates the various cycles of a group
16. [wiki-link](https://en.wikipedia.org/wiki/Cyclic_permutation) cycle notation
    * `(1 2 3 4)`: `1->2, 2->3, 3->4, 4->1`
    * `(1 2 3)*(3 4)=(1 2 4 3)` (left-to-right convention)
    * transposition: length 2 cycle
    * adjacent transposition
    * permutation: a bijective function $\phi:X\to X$ on a set $X$
17. [wiki-link](https://en.wikipedia.org/wiki/Automorphism) automorphisim
    * [wiki-link](https://en.wikipedia.org/wiki/Automorphism_group) automorphism group
    * $\mathrm{Aut}(C_3)\cong C_2\cong \mathrm{Aut}(\mathbb{Z})$
    * [wiki-link](https://en.wikipedia.org/wiki/Inner_automorphism) inner automorphism
    * must map generators to generators
    * $\mathrm{Aut}(C_n)\cong U(n)$
    * $\mathrm{Aut}(D_3)\cong D_3\cong\mathrm{Aut}(V_4)$

theorem

1. [wiki-link](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)) Lagrange theorem: $H<G$, then $|H|$ divides $|G|$
   * $|G|=|H|\cdot [G:H]$
2. [wiki-link](https://en.wikipedia.org/wiki/Cayley%27s_theorem) Cayley's theorem: every group is isomorphic to a subgroup of a symmetric group
   * construct from Cayley diagram
   * 重排定理: $gG=G$, left-multiplication by $g$ is a permutation of $G$
3. [wiki-link](https://en.wikipedia.org/wiki/Isomorphism_theorems) fundamental isomorphism theorem
   * (fundamental homomorphism theorem) first: let $f:G\to H$ be a homomorphism, then $G/\ker(f)\cong \mathrm{Im}(f)$
   * (diamond isomorphism theorem) second: let $N\triangleleft G$ and $S<G$, then $SN/N\cong S/(S\cap N)$
   * (freshman theorem) third: let $N\triangleleft G$ and $N<K\triangleleft G$, then $(G/N)/(K/N)\cong G/K$
   * (correspondence theorem) fourth: let $N\triangleleft G$, then there is a one-to-one correspondence between the set of subgroups of $G$ containing $N$ and the set of subgroups of $G/N$
4. [wiki-link](https://en.wikipedia.org/wiki/Wilson%27s_theorem) 威尔逊定理 Wilson's theorem: 若$p$是一个奇素数（除了2以外的素数），则 $(p-1)!\equiv -1 \bmod p$
5. [wiki-link](https://en.wikipedia.org/wiki/List_of_small_groups) list of small groups
   * if order is a prime, then the group is cyclic $C_p$
   * 4: $C_4,V_4$
   * 6: $C_6,D_3$
   * 8: $C_8,D_4,Q_8$
6. [wiki-link](https://en.wikipedia.org/wiki/Word_problem_for_groups) word problems for groups
   * computationally unsolvable, equivalent to the halting problem
7. [wiki-link](https://en.wikipedia.org/wiki/Finitely_generated_abelian_group) finitely generated abelian group
   * $C_6=C_2\times C_3$, but $C_4\ne C_2\times C_2$
   * $C_{mn}=C_m\times C_n$ iff $\mathrm{gcd}(m,n)=1$
   * $\mathbb{Z}$ is finitely generated
   * (prime power) every finitely generated abelian group is isomorphic to a direct sum of cyclic groups $A\cong C_{p_1^{k_1}}\times \cdots C_{p_m^{k_m}}$
   * (elementary divisor) every finitely generated abelian group is isomorphic to a direct sum of cyclic groups $A\cong C_{k_1}\times \cdots C_{k_m}$ with $k_1|k_2|\cdots|k_m$
   * 6 abelian groups of order 200:
     * $C_8\times C_{25}\cong C_{200}$
     * $C_4\times C_2\times C_{25}\cong C_{100}\times C_2$
     * $C_2\times C_2\times C_2\times C_{25}\cong C_{50}\times C_2\times C_2$
     * $C_8\times C_5\times C_5\cong C_{40}\times C_5$
     * $C_4\times C_2\times C_5\times C_5\cong C_{20}\times C_10$
     * $C_2\times C_2\times C_2\times C_5\times C_5\cong C_{10}\times C_{10}\times C_2$
8. [wiki-link](https://en.wikipedia.org/wiki/Group_action#Orbit-stabilizer_theorem) orbit-stabilizer theorem, set $S$, group $G$, group action $\phi: G\to\mathrm{Perm}(S)$
   * for any $s\in S$, $\mathrm{Stab}(s)< G$
   * $\mathrm{ker}(\phi)=\cap_{s\in S}\mathrm{Stab}(s)$
   * $|\mathrm{Orb}(s)|\cdot |\mathrm{Stab}(s)|=|G|$
9. misc
   * finite group $G$ of even order, must has an element with order 2

basic

1. concept
   * group: binary operation, associativity, identity, inverse
   * group order, finite group, infinite group, element order
   * abelian group (commutative group), nonabelian group
   * subgroup
   * [wiki-link](https://en.wikipedia.org/wiki/Lattice_of_subgroups) lattice of subgroups
   * generator
   * cyclic subgroup
2. [wiki-link](https://en.wikipedia.org/wiki/Commutator_subgroup) commutator subgroup and Abelianization
   * commutator subgroup $[G,G]=\langle aba^{-1}b^{-1} | a,b\in G \rangle$
3. [wiki-link](https://en.wikipedia.org/wiki/Group_action) group action G on set $S$: $\phi: G\to \mathrm{Perm}(S)$ is a homomorphism
   * orbit of $s\in S$: $\phi(G) x=\left\{ \phi(g) x:g\in G \right\}$
   * stabilizer: $\mathrm{Stab}(s)=\left\{ g\in G : \phi(g) s=s \right\}$
   * fixed point
   * action example: left (right) multiplication, conjugation
   * left group action: $\phi(g)\phi(h)s=\phi(gh)s$
   * right group action: $s\phi(g)\phi(h)=s\phi(gh)$, Cayley diagram
4. 半直积$G = G_1 \otimes_s G_2$
    * 半直积群
    * `G1`是`G`的不变子群
    * D3群具备以`G1={e,d,f}, G2={e,a}`为因子形成的半直积结构
5. isomorphism problem, 4-dimensional sphere problem

点群与空间群

1. 点群基础，晶体点群，晶体点阵，空间群（旋转轴，滑移面），三维实正交群（母体）
2. 对称操作，对称元素
3. $O_h$群
4. 正交变换，保内积，实正交群，$O(3)$群，$SO(3)$群（不变子群，保手性），空间反演群，
5. 点群：第一类点群，第二类点群

4阶循环群的特征标表如下，其中$A^p(a)=exp(2\pi i(p-1)/4)$

| - | $1\{e\}$ | $1\{a\}$ | $1\{a^2\}$ | $1\{a^3\}$ |
| :-: | :-: | :-: | :-: | :-: |
| $A^1$ | $1$ | $1$ | $1$ | $1$ |
| $A^2$ | $1$ | $i$ | $-1$ | $-i$ |
| $A^3$ | $1$ | $-1$ | $1$ | $-1$ |
| $A^4$ | $1$ | $-i$ | $-1$ | $i$ |
