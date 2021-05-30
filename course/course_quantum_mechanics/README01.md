# 高等量子力学

田 物理系 凝聚态所 强关联 磁性 超导电性

TODO bilibili-link

`tiangs@pku.edu.cn`

1. 固体物理：
2. 量子力学两种困难：概念，数学基础
3. 教程
   * 曾瑾言-量子力学卷2
   * Landau: Quantum Mechanics non-relavitistic
   * J. Mehra and Rechberg, the historical development of quantum theory
   * 电子版讲义
   * J. D Bjorken, S. D. Drell, Relativistic Quantum Mechanics

## chapter1 粒子数表象

1. 实用量子力学初步
2. 相干态
3. 回顾本科量子力学
   * 波函数，概率振幅，概率
   * 物理量，厄密算符
   * 本征态
   * 完备
   * 力学量平均值
   * 时间演化
4. 多粒子波函数
   * 全同性在非相对论量子力学中是作为假设引入的，在量子场论中从场的量子化推出了的结果 [知乎-为什么微观粒子不可分辨](https://www.zhihu.com/question/26540946)
   * 全同粒子统计规律：Boson, Fermion, Anyon
   * 找一个力学量的满足对称（反对称）规律的全部本征态：能量（哈密顿量）
   * 多体库仑相互作用无法解析解（之后使用微扰法来处理），转向无相互作用的多粒子哈密顿量
   * 单体本征值、本征态：$E_k=\hbar^2(k_x^2+k_y^2+k_z^2)/(2m)$
   * 箱归一化：解决了归一化问题，但人为破坏了对称性
   * 周期性边界条件：部分保留了对称性$k_x=2\pi n_x/L$
   * 热力学极限：边界趋近于无穷大
   * 谐振子势 [wiki/hermite-polynomial](https://en.wikipedia.org/wiki/Hermite_polynomials) TODO
   * 直积：算符直积，波函数直积
   * slater determinet
   * TODO $\pm 1$是如何引入的
5. 置换permutation
   * N阶置换群有$N!$个群元
   * 轮换，对换$P_{ij}$，奇偶性
   * 置换的乘积$P_1P_2=(i,P_1(P_2(i)))$
6. Boson对称多粒子波函数
   * $\phi_{k_1,k_2,\cdots,k_n}=D\sum_{P\in A_n}{\phi_{k_1}\phi_{k_2}\cdots \phi_{k_n}(P \{q_1,q_2,\cdots ,q_n\})}$
   * 交换对称性：群论重排定理
   * 正交性：总有一个粒子所处的波函数不同
   * $D=(N!N_{k_1}!N_{k_2}!\cdots N_{k_n}!)^{-1/2}$
   * 归一化：先把重复项合并，然后不同项之间正交
   * 完备性？：对于K个轨道，N个电子，原本有$K^N$个正交基矢，满足对称性条件的只有$\binom{N+K-1}{K-1}$
7. Fermion反对称多粒子波函数
   * $\phi_{k_1,k_2,\cdots,k_n}=C\sum_{P\in A_n}{(-1)^P\phi_{k_1}\phi_{k_2}\cdots \phi_{k_n}(P \{q_1,q_2,\cdots ,q_n\})}$
   * 不能出现两个粒子处于相同的波函数
   * 交换反对称性：重排定理+置换奇偶性
   * 归一化：$C=(N!)^{-1/2}$
   * 完备性？：对于K个轨道，N个电子，原本有$K^N$个正交基矢，满足反对称性条件的只有$\binom{K}{N}$
   * Slater determinet
8. 粒子数表象
   * V. Fock
   * Jordan-Wigner 1928：产生湮灭算符
   * 真空态vacuum state：约定内积1 `<0|0>=1`
   * 产生算符creation operator，湮灭算符annihilation operator
   * 单粒子态：验证与波函数统一，验证与产生湮灭算符自洽，真空态与单粒子态正交
   * 粒子数算符
   * 对易反对易关系
9. 自旋算符的费米子表象形式，玻色子表象形式
10. 单体算符：动量算符
    * 对于全同粒子的算符单体算符内积：`f(q1)==f(q2)`，全同性，任意子未必成立
    * 算符写成产生湮灭算符
    * Richard D. Mattuck "a guide to feymann diagram in many-body problems"
11. 两体算符：库仑势
    * 注意`1/2`，不能将`a<b`去掉（`a=b`对应单体算符）
    * 注意`g_{ab,cd}`和产生湮灭算符的次序
    * 直接积分，交换积分
12. 波函数表象优势：变分法，分数量子霍尔效应
    * 变分法与神经网络
13. 二次量子化（场量子化），场算符
    * 初衷：相对论量子力学
    * Klein-Gorden equation
    * 粒子数表象是场算符的自然推导结果，但粒子数表象的导出未必需要场算符（就像书中讲的那样），但本质上不同，二次量子化是为了解决相对论量子力学问题，而粒子数是为了解决多体问题
    * 格林函数，准粒子，课程《格林函数理论》

## 第二章 形式化微扰论

1. 微扰论：TODO 补充
2. 相互作用表象
3. 静态微扰，含时围绕
4. Heisenburg picture
   * Heisenburg equation: equation of motion
   * 产生湮灭算符仅在等式时满足对易/反对易关系
5. 积分方程理论
6. 编时算符
   * 此处的`H1`总是偶数个算符(,单体哈密顿量/二体哈密顿量),所以没有符号
7. 准粒子
8. 散射：假设不会形成束缚态
   * 入射粒子能量比较大时：born approximation, 曾谨言卷1-P423
   * 入射粒子能量比较小时：分波法，曾谨言卷1-P434
   * 微分散射截面，总散射截面
   * 曾谨言卷1-P423

## chapter4 两字力学体系中的对称性

1. pass
