# 固体物理

## lecture01

1. 课程内容设置
   * 概述-复习固体物理 2次课
   * 传统固体理论 12次课
   * 低微、介观、拓扑 4次课
   * 强关联
   * 电子板书、视频录播、课下阅读、推演、专题阅读、文献报告
2. general introduction
   * 长程序long-range order：symmetry breaking, phase transition，lattice, SC, SF, FM, AFM
   * 激发excitation：elementary (Fermi liquid theory), collective (phonon), topological (第二类超导体flux，domain wall)
   * low-dimensional system, low-temperature (10Kelvin, liquid helium, `1e-3eV`): quantum fluctuation, quantum coherence
3. method: mean field theory, Greens' function method (equation of motion and Feyman diagram)
4. 参考书
   * @book 李正中-固体理论：数学推导清楚
   * @book Philip L. Taylor and Olle Heinonen - A quantum approach to condensed mater physics：图像清楚
   * @book Basic Aspects of the Quantum theory of Solid：路径积分量子化
   * @book Condensed Matter Field Theory: 研究参考
   * @book P. W. Anderson - basic notions of condensed matter physics：研究参考

## lecture02 从固体理论到固体理论概述

1. paradigm shift：前范式阶段，常规科学阶段，反常阶段，危机阶段，科学革命阶段，新范式阶段
   * @book Thomas Kuhn-"科学革命的结构"
2. 周期结构中波的传播，晶体的平移对称性：晶格动力学+固体能带理论
3. 能带结构
   * 近自由电子图像+周期势场的围绕
   * 原子能级图像+晶体场展宽（紧束缚近似）：便于数值计算，disorder, interaction
   * 光子晶体（不同介电常数的介电体）
4. 无序体系：安德森局域化 1957, P.W. Anderson
5. 量子相干性：介观体系（体系尺度小于非弹性散射平均自由程）
6. Landau：二级相变理论，超导理论，超流Hell理论，Ginzburg-Landau theory，Fermi liquid theory，序参量和对称破缺
7. P.W. Anderson：无序系统理论，磁性杂质的电子理论，电导的标度律，Kindo问题的Poor man标度律，广义刚度，缺陷，重整化群
8. electron-plasmon：有能隙的集体激发，Higgs machanism
9. lattice-phonon：无能隙的集体激发，Goldstone machanism

## lecture03 序参量与相变理论概述

1. 对称性
   *全同粒子
   连续时空变换（平移，旋转，加速，彭加莱群）
   分立变换（空间反演P，时间反演T，粒子-反粒子共轭C）
   规范变换，U(1)（电荷、超荷、重子数和轻子数守恒），SU(2)，SU(3)
2. 准晶
3. 一级相变，二级相变（连续相变），序参量，临界点，临界现象，临界指数，标度律，普适性
   * BKT相变
   * Anderson localization
   * Widom的标度理论 1965
   * Kadanoff的标度理论：关联长度，长程序
   * Wilson 连续相变的重整化群方法

## lecture04 元激发概述

1. 元激发（准粒子）
   * 元激发能谱，统计规律，散射机理
   * 实验：角分辨光电子能谱ARPES，中子非弹性散射
   * 理论：量子场论方法（Green函数，Feynman图，Dyson方法）
2. elemntary excitation (多为Boson): phonon, magnon, 等离激元plasmon, 激化激元ploariton
3. collective excitation （多为Fermion）: quasi-electron, 离子晶体中电子或空穴与极化场形成的极化子plason，半导体中的电子空穴对electron-hole pair/exciton (Boson)
4. topological excitation: 超导/超流体系中的vortex激发/vortice/flux，phase slip, soliton，晶体场中的位错，磁性体系中的domain wall, skymion, meron
5. Anderson广义刚度与缺陷：拓扑缺陷
6. 凝聚态物理的新范式
7. BKT相变，2d XY model：涡旋态，相位子
8. @book Xiaogang Wen, Quantum Field Theory of Many-Body Systems
9. High-Tc SC
10. 整数量子霍尔效应
    * @1980 K.Von Klitzing, 2D electron gas
    * sdH oscillation
    * Hall Resistance
    * TKNN number (chern number), David Thouless 1982
    * Berry Curvature, 1984
    * Haldane model, QAHE, 1988
    * Realization of Haldane's model and QAHE, 薛其坤 2016
11. 分数量子霍尔效应
    * @1982 C. Tsui, H.L. Stomer et al
    * composite fermion with fractional charge, J.K. Jain
12. topological insulator
13. topological semimetal
14. symmetry protected topological insulator (SPT)
15. Kitaev model, Majorana Fermion
16. @book David Deutsch, "The Fabric of Reality", "The Beginning of Infinity"
17. @book Steven Simon, chap-VI

## lecture06-07 能带计算举例

1. tight-binding model
2. nearest neighbouring hopping，见`draft00.afx`
3. metal (half-filled), insulator (full-filled), semimetal/semi-insulator
4. Bloch定理
   * Hamiltonian与点群对称操作元素対易，所以两算符（点群对称操作其实有很多个算符）具有共同的本征函数
   * 点群对称操作是幺正算符（保内积），Abelion Group`O(x)O(y)=O(x+y)`
5. 正格子空间$\Omega$，倒格子空间$(2\pi)^3/\Omega$，每个k点占据倒空间体积$(2\pi)^3/(N\Omega)=(2\pi)^3/V$
6. 弱周期势近似，nearly free electronss近自由电子气（忽略电子相互作用），更适用于s/p电子
7. 紧束缚近似：更适用于d电子
   * 原子轨道线性组合法linear combination of atomic oribitals
   * Wannier function，正交，完备性，局域性：紧束缚近似是在近邻原子相互影响很小是，用原子波函数来近似Wannier function
8. lattice, Bravais lattice, 元胞，Wigner-Seitz Cells，倒格矢（动量空间），Brillouin zone, reduced Brillouin zone
   * 石墨烯：六角格子，bi-particle
   * Fourier Transform in lattice @book-李正中-chap1，static structure factor
   * 晶格中的动量守恒可以差任意个倒格矢
9. 石墨烯能带计算
   * 2D massless Dirac equation (2D Weyl equation)
   * K与K'互为时间反演，Krammers Theorem
10. Gapless, massless, Parabolic, linear
    * monolayer graphene: linear Gapless, relativistic
    * A-B stacking bilayer graphene: parabolic gapless, non-relativistic
11. twisted bilayer / multi-layer graphene

## lecture08 SdHdHvA量子振荡简介

1. dynamics of Bloch electron
2. velocity `<P/m>`
3. 群速度公式推导 TODO
   * 半经典公式推导
   * @book Ziman, Theory of solids
4. 磁场中的Bloch电子
   * 受力（粒子特征），速度（能带特征）
   * 受力垂直与磁场，能量不随时间改变
   * 实空间轨迹：实空间转圈圈，K空间在垂直磁场平面转圈圈，两者面积成比例系数
   * Onsager-Bohr-Sommerfeld量子化条件，geometric factor, generalized WKB approximation
   * 垂直于磁场的费米面面积量子化：为啥是最大的面积（不同面积的`1/B`震荡周期不同混合在一块）；当费米面不闭合（magnetic breankdown, tunnelling）
   * Landau能级：xy方向量子化（每个能级多重简并，理想晶体无穷简并），z方向连续
   * 费米面面积固定（假设能量固定），DOS/磁化率/电阻随着`1/B`震荡 Shubnikov de Hass effect（电阻）, de Hass-Van Alfen（磁化率）
   * 精确测量费米面
   * 磁通量子化
5. 绝缘体
   * 能带绝缘体
   * Mott绝缘体：电子-电子相互作用大于电子动能
   * Anderson绝缘体：杂质强度
   * Peierls transition
   * Hubbard model
   * Scaling theory of localization
   * Quantum Hall insulator
   * TOplogical insulator
   * Kondo insulator

## lecture09 晶格振动与中子散射概述

1. 晶体格波
2. 单原子链晶格振荡，能谱，声速
3. 双原子链：声学支（声速），光学支
4. Peierls transitions: electron-phonon interaction
5. charge density wave：electron-electron / electron-phonon interaction
6. thermodynamic (specific heat比热)；transport (resistance)；spectroscopy（scattering/tunneling，主要针对元激发）
7. 中子的非弹性散射：动力学结构因子（能量守恒，动量守恒）

## lecture10-12 二次量子化及应用举例

1. slater determinant
2. 占据数表象
3. Fock space
4. 从占据数表象定义证明対易关系
5. 单体算符：动能算符，自旋算符，粒子数算符，local density operator $a^\dagger(r)a(r)$，total density operator
6. 两体算符：使用坐标基矢的公式与一般公式略有不同，spin-spin interaction两体算符
7. 电声相互作用
   * 重新定义基态：把费米面以下的产生湮灭算符对换
   * Wannier function基矢，r-space, k-space之间的变换
   * 在位能，最近邻，2D square lattice $E=-2tcos(k_xa)-2tcos(k_ya)$
8. SSH model, Su-Shrieffer-Heeger model
   * @paper, PRL-42-1698(1979)
   * @paper RMP-60-781(1988)
9. 阅读材料
   * @LiZhengzhong chapter3/4/6
   * @Taylor, Heinonen chapter2/3/4/6/7/10
   * @Althand, Simons chapter2
   * @Khomskii chapter5/6/7/8/9/10/11/13

## lecture13-17 磁性系统模型概述

1. 库仑相互作用在Wannier基矢下的二次量子化表示
   * direct term $U_{ijij}, i\neq j$，电荷密度波charge density wave
   * exchange term, spin interaction, 高自旋也成立
   * onsite term, Hubbard model, Mott insulator, half-filled, filling fraction
   * strong-coupling limit, Anderson super-exchange (反铁磁能量更低)
2. 铁磁自旋波理论
   * magnon-magnon interaction
   * HP-transformation
   * 磁化：当维度小于等于2时，非零温下积分发散，即铁磁无长程序Hohenberg-Mermin-Wagner theorem，3维时有临界温度
   * spin-1/2的HP变换近似的正确性，Hard-core Boson，@book-Huang-K.S.-StatisticalMechanics, Matsubara@1956
   * BEC
   * break rotation symmetry
3. 反铁磁自旋波理论
   * Neel State：非本征态
   * Goldstone Mode: gapless
   * break rotation symmetry: gapless excitation mode
   * 非零温：当维度小于等于2时，非零温下积分发散，即反铁磁无长程序
4. BEC： @book-张礼-chap10.1
5. 2维磁性系统，2D-XY model, BKT相变
6. 1维磁性链 @book-张礼-chap7
7. Ising model离散磁性系统 @course-高等统计物理
8. 磁性系统的杂质问题
9. Jordan-Wigner变换（spin-1/2）：映射为费米子算符
   * 1D nonlinear (non-local) transformation
   * 1D-XY model: 无相互作用无自旋系统
   * 可能改变体系的拓扑特征

## lecture17-18 玻色爱因斯坦凝聚概述，弱相互作用的波色系统，Bogoliubov理论

1. 相干态，破坏了`U1`对称性，基态（？）
2. 自发对称性破缺：体系哈密顿量满足某对称性，但本征态不具有该对称性
3. 非对角长程序，BEC，实空间关联 C.N. Yang
4. 对角长程序：晶格
5. 非对角长程序+对角长程序：supersolid
6. 化学势$\mu$趋近于0时，接近BEC
7. thermal wavelength @book-张礼 @wiki-[link](https://en.wikipedia.org/wiki/Thermal_de_Broglie_wavelength)
8. 临界温度$T_E$
9. 弱相互作用的波色系统实现：波色系统一般不带电，所以稀薄波色系统（粒子密度低）的相互作用一般就很弱，只剩下碰撞相互作用
10. 简化
    * ultra-local approximation, pseudo-potential
    * 高阶项$b_k^\dagger b_k$只保留到一阶
    * 基态产生湮灭算符平均值等于$\sqrt N$
11. Bogoliubov transformation
    * 激发谱：线性色散变换
    * ground state
    * 声速
    * compressibility压缩率 $\kappa=\frac{1}{n^2}\frac{\partial n}{\partial \mu}$，无相互作用时：压缩率为无穷大（不符合真实情况）
    * [link](https://www.nii.ac.jp/qis/first-quantum/e/forStudents/lecture/pdf/qis385/QIS385_chap4.pdf)
    * 超流速度上限
12. BEC稳定性
    * 维度dimensionality：非零温时，小于等于2维时BEC不稳定（计算激发态的粒子数），零温时，小于等于1维BEC不稳定，Honhenberg-Mermin-Wagner theorem
    * 拓扑激发topological excitation：flux/vortice（二维中一般称作vortice），flux-flux相互作用会影响超流稳定性
    * 超流速度superfliud velocity：杂质散射（从`q`态散射到零态的能量）
13. BEC local order parameter (Landau-Ginzberg) $\langle \psi^\dagger (r) \rangle =\sqrt{\rho (r)}e^{i\phi(r)}$
    * 发生BEC时，$\phi(r)=\phi$
    * 相位梯度给出超流的速度
14. trapping system光晶格: Gross-Pitaevskii equation
15. Feshbach resonance, tunning interaction strength, unitary limit
16. Fermionic superfluidity (pair of fermions to make a boson)
17. BCS-BEC crossover
18. low-dimension system BKT transmition
19. 强关联极限unitary limit, Efimov trimer state
20. Bose-Hubbard Model

## lecture19-21,23 线性响应与格林函数方法

1. 薛定谔绘景，海森堡绘景，相互作用绘景，相互作用绘景时间演化算符（包含无穷阶微扰）
   * 海森堡绘景下，対易关系仅在等时下可以计算，除非已经对角化了
2. 线性响应只使用相互作用绘景时间演化算符一阶近似，不适用于相变区域、共振区域
3. 运动方程法
4. correlation function; Green's function
   * retarded function，一般是时间差的函数（哈密顿量不含时），为了收敛（时间趋近于正无穷时函数值趋0），引入$\eta$
   * advanced function
5. 热力学平均
6. 线性响应系数：电极化强度charge susceptility，磁性计划强度meganetic susceptibility，电导conductivity
7. Kubo formula
   * $V(t)$是小微扰，影响本征态但不影响本征值分布
   * 没听懂
   * @book-Hydrodynamic-Fluctuations-Broken-Symmetry-and-Correlation-Functions
8. kubo formula for the dielectric function: 电荷电荷关联
   * dielectric function $\epsilon$
   * polarizability function $\chi$
   * dielectric function与condctivity的关系

## lecture22 Anderson

1. 反铁磁自旋波理论：给出了连续对称性破缺产生戈德斯通模式Goldstone mode的雏形
2. 杂质系统的安德森局域化，阐明杂质强度超过某个特定值后，由于量子干涉效应，粒子不在做扩散
3. 超交换作用，阐明磁性绝缘体中反铁磁耦合的来源
4. S波超导体的安德森定理，阐明非磁性杂质不影响S波超导体序参量
5. 局域磁矩的安德森模型
6. 规范对称性破缺与安德森-黑格斯机制，阐明超导体中无质量的相位模式与无质量的光子场耦合会使光子获得质量，进而导致迈斯纳效应
7. 自旋玻璃的统计理论，研究方法在复杂网络系统中产生很大影响
8. 近藤效应的Poor Man标度分析，采用重整化群方法分析近藤问题，其研究方法激发了Michael Kosterlitz和David Thouless对BKT相变的标度分析
9. 安德森局域化的标度理论
10. 铜氧超导体的RVB理论

## lecture24-27 格林函数方法

1. 单粒子格林函数：retarded/advanced/greater/lesser Green's function
2. 自由体系的格林函数
3. Lehmann表示（形式理论）
4. fluctuation-dissipation theorem：greater/lesser格林函数与涨落相关，retarded/advanced格林函数与响应相关
5. spectral function，与态密度类似（但不是）
   * broadening of spectral function
   * Hilbert integral, Kronig-Krammers Relation
   * Sokhotski–Plemelj theorem, [wiki](https://en.wikipedia.org/wiki/Sokhotski%E2%80%93Plemelj_theorem)
   * Kramers-Kronig relations, [wiki](https://en.wikipedia.org/wiki/Kramers%E2%80%93Kronig_relations)，解析延拓
   * 实验上可测量谱函数
   * 动量空间测量ARPES，time-spin-ARPES, quasi-particle interaction
6. 隧道谱tunneling spectroscopy, STM/STS, tunneling junction, point contact measurement
   * 宽带近似band-width approximation
   * differential conductance
   * 假定：针尖对体系影响很小，宽带近似
7. 双粒子格林函数（关联函数）：更多粒子的格林函数没有实验上的测量量
   * 不需要区分波色/费米型
8. 密度算符，电子空穴对激发，plasmon
   * 一维电子空穴对激发：存在禁闭区域，perfect nesting，random phase approximation，密度算符的波色化处理
   * 等离激元振荡
   * 介电函数，磁化率
   * 电流电流关联给出电导率，电荷电荷关联给出极化率/介电函数
9. quantum open system：最简单的情况是导线和一个量子点
10. 零温涨落耗散定理：响应函数，动力学结构因子

## lecture28-29 无相互作用电子的运动方程法

1. 生成一系列微分方程，通常不封闭，所以需要截断
2. 单粒子无相互作用体系格林函数
3. single level electron couple to a continuum lead, @book-Jauho
   * self-energy
4. @book-王顺金-量子多体理论与运动模式动力学
5. Anderson磁性杂质理论
   * 巡游电子itinerant electron
   * 局域磁矩一般是d电子，较强的库仑相互作用
   * 平均场近似，Hartree近似
   * 宽带近似
   * Stoner criterion

## lecture30 RPA的运动方程法

1. 电荷电荷关联函数（不区分Boson/Fermion）
2. Random Phase Approximation (RPA)
   * @1953-Bohm-Pines
   * 可从费曼图/运动方程推出
3. Hartree type mean field approximation
4. 极化率，介电函数
5. plasma oscillation mode等离激元

## lecture31 虚时演化和松原格林函数

1. 松原格林函数：周期性，时间差，虚频
2. 松原格林函数的求和技巧
   * 波色分布/费米分布复数域奇点
   * @book-Braus-and-Flensberg: Many body Quantum Theory in Condensed Matter Physics
   * @book-G.-Rickayzen: Greens' function and Condensed Matter
   * @book-Akkermans-and-Montambaux: Mesoscopic physics of electrons and photons
   * @book-Richar-D.-Mattuck: A Guide to Feynman Diagrams in the Many-body problem
   * @book: AGD
3. Wick theorem: n-particle Green's function
   * eg: 极化率

## lecture34 杂质格林函数的波恩近似和T矩阵近似

1. 弹性散射，Matasubara Green's function
2. 弱杂质：杂质浓度相比载流子浓度，费米波矢乘以平均自由程远大于1
3. 强杂质：高阶格林函数，transfer matrix
4. 费曼规则：图和公式对应规则
5. impurity average导致的平移不变形
6. T矩阵近似：single impurity scattering，可以处理束缚态问题
7. 自洽T矩阵近似，自洽波恩近似

## lecture36 相互作用系统的费曼图规则概述

## 固体物理基础-阎守胜

1. 玻尔半径
2. 精细结构常数
3. 玻尔磁矩
4. 等离子体频率$\omega_p=\frac{ne^2}{m\epsilon_0}$，常见金属$\hbar\omega_p$在`5~15eV`
5. 回旋频率$\omega=\frac{eB}{m}$

### 第一章 金属自由电子气体模型

1. Drude 经典气体模型（准经典模型）
2. Sommerfeld 金属自由电子气体模型 费米-狄拉克统计
   * 假设：忽略电子与离子实相互作用，忽略电子之间相互作用（独立电子近似）（一般情况下，电子之间的散射确实不重要），弛豫时间
   * 独立参量：电子密度（`1e22~1e23/cm^3`），弛豫时间`~1e(-14)s`
   * 由电子密度，每个电子平均占据半径`2~3Angstrom`大小的球体积，与常见金属晶格常数相当（这是必然的）
   * 周期性边界条件，波矢k取值量子化
   * 费米球，费米波矢`~1e8cm^-1`，费米面，费米能`2~10eV`，费米速度`~1e6m/s`，费米温度`1e4~1e5K`
   * 零温下，每个电子平均能量$\frac{3}{5}E_F$
   * 单位空间态密度
   * 低温下化学势：如态密度的导数为正则化学势降低
   * 自由电子气体比热正比于温度，正比于费米面的态密度（晶格比热正比于`T^3`）
3. 电子带有一个玻尔磁子的自旋磁矩
4. 零温下电子Pauli paramagnetic susceptibility正比于费米面态密度
   * 由于离子实具有抗磁性，不用该方法测量费米面态密度
5. 弛豫时间$\tau$：在$dt$时间内，任一电子受到碰撞的概率$\frac{dt}{\tau}$
   * 金属中电子平均自由程大约`10nm`
   * 准经典模型，外场下电子的运动方程，漂移速度，电导率，电流密度，交流电场下（复数电导）
   * 光学效应：吸收区，反射区，透明区
   * 霍尔效应：对二三价金属符合较差
6. 热导率$J_Q=-\kappa\nabla T$
   * G. Wiedemann, R. Franz, L. V. Lorenz, Lorenz数 $\kappa/(\sigma T)$
7. 模型不足
   * 电子密度大但导电性差的二三价金属（能带模型）
   * 无法解释电导率随温度的变化
   * 电导率的各向异性（晶格）
   * 无法解释金属、半导体与绝缘体

### 第二章 晶格结构

1. 晶体结构：基元，晶格crystal lattice
2. 晶格：基矢，原胞（primitive cell）（Wigner-Seitz原胞），配位数
   * Wigner-Seitz保持与晶格完全相同的对称性，也称为对称化原胞
   * 晶向`[2,3,3] <2,3,3>`
   * 晶面：Miller indices `(h1,h2,h3) {h1,h2,h3}`，把基矢分别分成`h1/h2/h3`等分
   * 点群，空间群
3. Bravis lattice：简单立方sc，体心立方bcc，面心立方fcc，简单六角simple hexagonal
4. 点群：
   * 熊夫利符号Schoenflies notation，国际符号International notation
   * 点群中允许的转动对称轴`C1/C2/C3/C4/C6`
   * 32个点群
   * 7种晶系
5. 空间群
   * 简单空间群（73），复杂空间群（230）
   * 螺旋轴，滑移面
   * 14种Bravis lattice
6. 单胞（unit cell）：可能包含多个原胞，晶格常数
   * 区别于基元中包含多个原子（简单晶格与复式晶格）
7. 二维格子：10中点群，4个晶系，5种Bravis lattice
8. 常见的晶体结构
   * `CsCl`，简单立方
   * 立方钙钛矿，`BaTiO3`，简单立方
   * `NaCl`，面心立方
   * 金刚石，四重螺旋轴，面心立方
   * 闪锌矿，面心立方
   * 六角密堆：hexagonal close-packed (hcp), fcc, `c/a=sqrt(8/3)`
9. 倒格矢
   * 具有晶格平移对称性的傅里叶展开中，只存在倒格矢的分量
   * 倒格子的Wigner-Seitz原胞称作第一布里渊区First Brillouin Zone
   * 面心立方格子和体心立方格子互为倒格子
   * 倒格矢$\vec{G}_h=h_1\vec{b}_1+h_2\vec{b}_2+h_3\vec{b}_3$垂直于Miller indices`(h1,h2,h3)`的晶面系，面间距为$2\pi/| \vec{G}_h |$
   * 正格子与倒格子具有相同的对称性
10. X射线衍射：`~1e4eV`
    * 晶格导致的非弹性（热振动）散射可忽略不计`~1e-2eV`
    * Laue condition $k^\prime-k=G_h$
    * Bravis condition $n\lambda=2dsin\theta$，几何结构因子（基元、单胞都可能引入），原子形状因子
    * 实验方法：Ewald球，Laue method（连续波长），转动晶体法，粉末法（德拜法）
11. 电子衍射，`20~250eV`，主要用于晶体表面研究
    * 德布罗意波长：$\lambda=h/p$
12. 中子衍射，`~0.08eV`，热中子，对轻原子（H到C）的分辨率高于X射线，中子有磁矩
13. 扫描隧道显微镜STM
14. 扫描隧道穿谱仪器STS：局域态密度随着能量的变化
15. 准晶

### 第三章 能带论

1. 假设
   * Born-Oppenheimer近似：离子实运动的每一瞬间，电子的运动都快到足以调整其状态到离子实瞬时分布情况下的本征态
   * 单电子近似：用平均场代替电子之间的相互作用，与自由电子近似很相近
   * 周期场近似：进一步假设平均场具有周期性
2. 从头计算ab initio calculation，第一性原理first-principle method
3. 布洛赫定理：周期势场下的平移算符与哈密顿量対易，布洛赫波函数
   * k空间每个k值占据空间$(2\pi)^3/V$
   * 布洛赫波函数是倒空间的周期函数
   * 能谱是倒空间的周期函数的周期函数，所以有上下限，形成能带
   * 简约/重复/拓展布里渊区图示 reduced/repeated/extended zone scheme
   * 能谱：和晶格有相同的对称性（空间群），实数哈密顿量导致时间反演对称性$E(k)=E(-k)$
4. 弱周期势近似（微扰），适用于s/p电子的金属
   * 能隙
   * 能谱垂直于布拉格平面（对称性保证）
   * 能隙的形成来源于两个波的叠加（与劳厄条件相同）
   * 复式晶格的几何结构因子
5. 紧束缚近似：近邻原子的电子波函数相互交叠较小，比较适用于3d电子的金属以及固体的内层电子
   * 假设：不同个点的波函数因交叠小而相互正交
   * 交叠积分
   * 过渡元素的d电子轨道波函数与近邻交叠较小
6. Wannier function瓦尼尔函数
   * 布洛赫函数是k空间的周期函数，自然可以对k进行傅里叶展开
   * 正交性，仅是$r-R_n$的函数
7. Hartree近似：借助平均场将多电子问题转化为单电子问题
   * 密度泛函理论：基态能量仅有基态电子密度决定，局域密度近似，交换势，关联势
   * 缀加平面波，糕模势
   * 正交化平面波 赝势
8. 空晶格模型
9. 高布里渊区：第n个布里渊区是第n-1个布里渊区只经过一次布拉格面，除进入n-2区外的所有点的集合
   * 等能面几乎总是和布里渊区边界面垂直（可能$V_n$等于0）
   * van Hove singularity：$\partial E / \partial k=0$

### 第四章 布洛赫电子的动力学及能带结构的测量

1. 电子的晶体动量
2. 布洛赫电子的平均速度（速度期望值）
3. 半经典模型
   * 速度方程，晶格动量方程（电磁力，推导不严谨，凑出来的）
   * 忽略电子的能带间跃迁，电子视为波包，晶格周期场变化尺度远小于波包大小，波包尺度远小于外场变化尺度
4. 有效质量（张量）：能带低为正，能带顶为负，宽的能带有效质量下（d电子能带的有效质量大），热有效质量
