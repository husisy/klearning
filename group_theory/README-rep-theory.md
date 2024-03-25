# Representation theory

1. link
   * HKUST/MATH5112 [course-website](https://www.math.hkust.edu.hk/~emarberg/teaching/2021/Math5112/index.html) [youtube](https://youtube.com/watch?v=FdOkHznnLIc&feature=shares)
   * [youtube/Richard/representation-theory](https://www.youtube.com/watch?v=Q9OsEZV5YX8&list=PL8yHsr3EFj51AM_VmB0VygPIzcUCH_jUG)

concept

1. icosahedron

## representation of group

1. classify all symmetries of all groups
   * classify all finite groups (impossible)
   * given group $G$, find all things $G$ acts on
     * set: permutation representation
     * module over ring (field): linear representation
2. decomposable representation
   * set $S=S_1\cup S_2$, $S_1$ and $S_2$ acted on by $G$
   * vector space $V=V_1\oplus V_2$, $V_1$ and $V_2$ acted on by $G$
   * indecomposable representation, transitive action, orbit of $G$ on $S$
3. $V$ is reducible if $V$ has a non-trivial $G$-invariant subspace
   * decomposable $\Rightarrow$ reducible
   * for complex representation, reducible $\Rightarrow$ decomposable
4. Burnside's theorem
   * if $|G|=p^aq^b$, then $G$ has a non-trivial normal subgroup (solvable)
   * non-solvable group example $60=2^2\times 3\times 5$

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
