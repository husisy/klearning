# Density Functional Theory (DFT)

1. electron correlation
   * [wiki](https://en.wikipedia.org/wiki/Electronic_correlation)
   * interaction between electrons
   * 在HF中定义为理论值与HF之间的误差
   * 在DFT中定义为理论值与DFT之间的误差
   * correlation包含: single determinant approximation, finite basisset, Born-Oppenheimer approximation, non-relativistic

## 代码实现

DFT is in shell, let's pull it out

不太大的代码仓库

1. link
   * [github/Gaussium](https://github.com/ChiCheng45/Gaussium)
   * [github/tinydft](https://github.com/theochem/tinydft)
   * [github/dqc](https://github.com/diffqc/dqc)
   * [github/lfdft](https://github.com/brandongc/lfdft)
   * jax-dft @paper-PRL [link](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.126.036401) [github](https://github.com/google-research/google-research/tree/master/jax_dft)
   * @youtube DFT code in one hour with matlab [link](https://youtu.be/bW44gCulrvI)
   * [sisl](https://sisl.readthedocs.io/en/latest/introduction.html)
   * [poisson-summation](https://en.wikipedia.org/wiki/Poisson_summation_formula)

DFT design

1. read input
   * [ ] Poseudopotential
   * [ ] Control parameters
   * [ ] Basis (if LCAO or similar type)
   * [ ] k-space reader and generator
   * [ ] Atomic coordinates and lattice reader and generator
2. save output
   * [ ] logger
   * [ ] save density at least
3. main scf loop
   * [ ] Hamiltonian generator
   * [ ] Momentum oprator (laplacian, derivation)
   * [ ] Generate local potential from density
   * [ ] Generate non-local potential from density
   * [ ] generate XC potential and energy from density
   * [ ] Generate Hartree potential from density (poisson equation)
   * [ ] eigenvalue solver
   * [ ] Generate density from wave function
   * [ ] total energy (could be skipped for simple DFT code)
   * [ ] mixer: Linear at least, pulay or broyden
   * [ ] Check if converge

## YouTube course: TMP Chem computational chemistry (HF)

1. atomic units
   * $m_e=e=\hbar=4\pi\varepsilon_0=a_0=1$
   * mass $m_e=9.109e-11 kg$
   * charge $e=1.602e-19 C$
   * angular momentum $\hbar=1.055e-34 J\cdot s$
   * permittivity $4\pi\varepsilon_0=1.113e-10 \frac{C^2}{J\cdot m}$
   * 导出单位 Bohr radius $a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_ee^2}=5.3e-11 m$
   * 导出单位 Hatree $\frac{\hbar^2}{m_ea_0^2}=\frac{m_ee^4}{16\pi^2 \varepsilon_0^2\hbar^2}=4.36e-18 J=27.21 eV$
2. Born-Oppenheimer approximation
   * nuclei视为classical point particles
3. orbital, occupied, virtual (unoccupied), spatial ($x,y,z$) orbital, spin ($x,y,z,\sigma$) orbital
4. Hartree product: independent uncorrelated electrons
   * issue: distinguishable electron
5. antisymmetry principal
6. Slater determinants
   * $N$ electron, $2K$ spin orbitals, $\frac{(2K)!}{(2K)!(2K-N)!}$ determinants
   * ground state $|\Psi_0\rangle$, single excited $|\Psi_a^r\rangle$, double excited $|\Psi_{ab}^{rs}\rangle$
7. N-electron wavefunction
   * linear combination of all determinants of a complete set of spin orbitals
   * $|\Psi\rangle=c_0|\Psi_0\rangle+\sum_{ar} |\Psi_a^r\rangle + \sum_{a\le b,r\le s}|\Psi_{ab}^{rs}\rangle +\cdots$
   * Hatree Fock (HF): $|\Psi_0\rangle$
   * Configuration Interaction Double (CIS): 和HF是一回事，故不讨论
   * Configuration Interaction Double (CID): $|\Psi_0\rangle,\{|\Psi_{ab}^{rs}\rangle\}$
   * CISD: $|\Psi_0\rangle,\{|\Psi_a^r\rangle\},\{|\Psi_{ab}^{rs}\rangle\}$
   * CISDT, CISDTQ, CISDTQ5, CISDTQ6, full CI
8. restricted determinants: spin-up, spin-down pairs must have same spatial orbital
   * closed shell: `s2, p6, d10`
   * $|\Psi_1\bar{\Psi}_1 \Psi_2\bar{\Psi}_2 \cdots \Psi_{N/2}\bar{\Psi}_{N/2} \rangle$
   * nomenclature $|1\bar{1} 2\bar{2} \cdots N/2\bar{N/2} \rangle$
   * Restricted Hartree Fock (RHF)
   * Restricted Open shell Hartree Fock (ROHF)
9. unrestricted: spin-up spin-down parts can have differencet spatial orbitals
   * open shell
   * lithium `1s2 2s1`: `2s1` electron interacts differently with `1s-up` and `1s-down`
   * Unrestricted Hartree Fock (UHF)
10. one-electron integral
    * 这里选定了单体算符作为basis
    * one-electron operator, core Hamiltonian $h_i=-\frac{1}{2}\nabla_i^2+v_{ext}(r_i)$
    * $\langle \psi |h_i|\psi \rangle =\frac{1}{N}\sum_i{\int{dx\phi_i^*(x) h\phi_i(x)}}$
11. two-electron integrals
    * $\langle \psi_0|\frac{1}{r_{12}}|\psi_0\rangle =\int{dx_1dx_2\phi_1^*(1) \phi_2^*(2) \frac{1}{r_{12}}\phi_1(1) \phi_2(2)}-\int{dx_1dx_2\phi_1^*(1) \phi_2^*(2) \frac{1}{r_{12}}\phi_2(1) \phi_1(2)}$
    * 记作$\langle 12|12\rangle -\langle 12|21\rangle =\langle 12||21\rangle$
    * physicist's notation $\langle ij|kl\rangle =\int{dx_1dx_2\phi_i^*(1) \phi_j^*(2) \frac{1}{r_{12}}\phi_k(1) \phi_l(2)}$
    * chemist's notation $[ik|jl] =\int{dx_1dx_2\phi_i^*(1) \phi_k(1) \frac{1}{r_{12}}\phi_j^*(2) \phi_l(2)}$ **以下采用该记号**
    * Coulomb integral, exchange integral
12. spin integration
    * restricted Hartree Fock *好像不需要这个条件*
    * 单体算符与自旋无关，故不同自旋轨道在单体算符下内积为0
    * 圆括号表示仅包含空间积分，而不包含自旋部分
    * $\langle i|h_1|j\rangle =\sum_\omega{\sigma_i^*(\omega) \sigma_j^*(\omega)}\int{dx\phi_i^*(x) h\phi_i(x)}=\delta_{\sigma_i\sigma_j}(i|h|j)$
    * $[ij|kl]=\sum_{\omega_1}{\sigma_i^*(\omega_1) \sigma_j(\omega_1)}\sum_{\omega_2}{\sigma_k^*(\omega_2)\sigma_l(\omega_2)} \int{dx_1dx_2\phi_i^*(1) \phi_j(1) \frac{1}{r_{12}}\phi_k^*(2) \phi_l(2)}=\delta_{\sigma_i\sigma_j}\delta_{\sigma_k\sigma_l}(ij|kl)$
    * $[ii|jj]=(ii|jj)$
    * $[ij|ji]=\delta_{\sigma_i\sigma_j}(ij|ji)$ (chemist's notation)
13. Hartree-Fock approximation
    * average over "mean field" of other electrons, mean field approximation
    * Fock operator $f(1)=h(1)+v^{HF}(1)$, $f(1)\phi_1(1)=\varepsilon_1 \phi_1(1)$
    * pseudo eigenvalue problem
14. Hartree Fock energy
    * $J_{ij}$: electrostatic interaction
    * $K_{ij}$: exchange interactaction (same spin)
15. example: Boron atom, RHF
    * `1s2 2s2 2p1`
    * $E=2h_1+2h_2+h_3+J_{11}+4J_{12}-2K_{12}+2J_{13}-K_{13}+J_{22}+2J_{23}-K_{23}$
16. Fock operator
    * 见`TMPChem/draft00.afx`
    * permutation operator $P_{12}$
    * 重看`4.16`, `4.17`
17. functional variation
18. minimum determinant energy
19. non-canonical/canonical form of Hartree Fock equation
    * Hatree-Fock equation中的energy对于占据、非占据的计算是不一样的，占据的HF比非占据的少一项（self-interaction那一项）
20. Koopman's theorem
    * ionization potential
    * affinity energy (这个不是太准，一般不用)
21. RHF可以把spin做简化，进而得到一系列公式`4.22`
22. Hartree-Fock-Roothaan equations 引入basisseet
23. 所有做的近似
    * Born-Oppenheimer approximation
    * Fork approximation (mean field approximation): electron interact with the mean field (charge density) of the other electrons
    * basisset: finite set of atomic orbitals
24. density matrix $P_{\mu\nu}=\sum_{a=1}^{N/2}C_{\mu a}^*C_{\nu a}$
    * completely specifies charge density
    * invariant to orbitals given basisset
25. orthogonalization
    * symmetric orthogonalization
    * canonical orthogonalization
    * remove redundant basis
26. self-consistent field
27. population analysis
    * 单体算符期望值：用density matrix, 例如electric dipole moment
    * Mulliken partial charges
    * Lowdin charges

Quantum Chemistry 9.0 [youtube-link](https://youtu.be/mSFMkQrL2ZI)

1. post-HF method: correlation
   * DFT
   * MP2
   * CCSD(T)
2. atomic term symbols `(2S+1) L_J`
3. Hund's rules
   * lagest `S`
   * llargest `L`
   * `>1/2` largest J, `<1/2` smallest J
4. atomic spectral
5. Helium atom energy approximation
   * experimental `E=-2.9033`
   * variational `E=-2.848`
   * perturbative `E_0=-4`, `E_1=-2.75`, `E_2=-2.9077`
   * HF `E=-2.8617`
6. no self-interaction problem in HF method, $J_{ii}$ is cancelled by $K_{ii}$
7. Hartree-Fock operator

## coursera-DFT

1. recommended material
   * A bird's-eye view of density-functional theory [link](https://www.scielo.br/j/bjp/a/dWXh7yLvsDSpZwzVv4wYcxF/?lang=en)
2. Hartree atomic system $\hbar, e, a_0, m_e$ [wiki](https://en.wikipedia.org/wiki/Hartree_atomic_units)
3. many body physics, 状态指数增长
4. approximate wavefunction
   * Hartree Fock
   * Configuration Interaction
   * Quantum Monte Carlo
5. 计算observable
   * 将其视为`Vext`的泛函
6. density作为DFT的最基本变量不是唯一选择，也许可以多个变量
7. functional
   * local
   * semi-local
   * non-local: 两重积分，梯度
   * kinetic energy: Thomas-Fermi, von Weizsacker
8. functional derivative
   * test function
9. DFT基态简并的论述
   * @paper2006-PRA-76-012508 [link](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.76.012508)
10. Hohenberg-Kohn theorem
    * 先论述基态和外势是一一对应的（不考虑简并）：反证法，基态本征方程作差
    * 在论述外势和基态密度一一对应
11. V-representable
    * Levy1982
    * Lieb1982
    * Englisch-Englisch1983
    * ensemble V-representable
    * new HK proof, constrained search
    * from V-representable to N-representable
12. @paper2017-nature-8-872 Bypassing the Kohn-Sham equations with machine learning [link](https://www.nature.com/articles/s41467-017-00839-3)

week3

1. Jacob's ladder
   * Hartree, no xc
   * LDA
   * GGA
   * metaGGA
   * Hybrids
   * RPA
2. jellium: uniformly smeared out positive, homogeneous electron gas of same density
   * kinetic: Thomas-Fermi model $(3\pi^2n)^{5/3}/(10\pi^2)$
   * exchange energy: $(3\pi^2n)^{4/3}/(4\pi^2)$
   * correlation energy: approximate formulas based on quantum Monte Carlo
3. LDA
   * @paper1965-Kohn-Sham: non-emprical xc functional
   * reference system
   * 将空间局部视为homogeneous electron gas
   * 分子总能误差在`0.01-0.05`
   * 固体晶格常数误差在`0.01-0.02` (typically too short)
   * 问题：atomization energies too big (overbinding), no negative ions
4. the exchange correlation hole
   * 电子彼此排斥的机理：classical Coulomb interaction $r^{-2}$, exchange interaction between parallel spin, correlation (both parallel and antiparallel spin)
5. two-body density (pair density), exact constraint
   * $P(r_0,r_1)=n(r_0)n(r)1)+n(r_0)n_{xc}(r_0,r_1)$ xc hole density
   * $n_{xc}(r_0,r_1)=n_x(r_0,r_1)+n_c(r_0,r_1)$: exchange/correlation hole density
   * $n_x(r_0,r_1)\leq 0$
   * $\int{n_x(r_0,r_1)dr_1}=-1$
   * $\int{n_c(r_0,r_1)dr_1}=0$
   * nearsightedness: $n_{xc}(r_0,r_1)$ mostly determined by $n(r_0)$
6. GGA
   * semi-local approximation
   * enhancement factor $F_{xc}$
   * non-empirical
   * PBE @paper1996-PRL-79-3865 (Perdew-Burke-Ernzerhof 1996)
   * BLYP (Becke-Lee-Yang-Parr 1988)
7. coupling constant integration
   * adiabatic connection
   * coupling constant average
   * coupling constant $\lambda$ is a measure of correlation strength
8. metaGGA
   * kinetic energy density $\tau^\sigma(r)=\frac{1}{2}\sum_{i\in occupied}{|\nabla \Psi_i^\sigma|^2}$
   * TPSS (Tao-Perdew-Staroverov-Scuseria 2003)
   * Strongly Constrained Appropriately Normed (SCAN) (Sun-Ruzsinszky-Perdew 2016)
   * 原因：$\tau(r)$ is sensitive to the degree of localization of electrons
   * 原因：$\tau(r)$ helps to distinguish covalent single bonds and metallic bonds
   * 原因：$\tau(r)$ incorporates exact constraints of one- and two-electron densitys
   * semilocal orbital functional, nonlocal density functional
   * 主要使用场景：formation enthalpy of solids (main group binary compounds), but less accurate for transition metal compounds
   * SCAN can describe medium range van der Waals interactions: correct ordering of water hexamer structures
9. GGA/meta-GGA不擅长处理的场景
   * weakly bonded system
   * strongly correlated systems
   * band gap calculation
10. Hybrid functionals
    * Axel Becke(1993)
    * mix a semilocal xc and nonlocal exact exchange
    * PBE0(1999): mixing parameters are determined semi-empirically
    * B3LYP(1994): mixing parameters are determined empirically
    * variation with respect to the orbitals, nonlocal generalized Kohn-Sham equation
    * good at: energetics of molecules, geometries/lattice constants (but GGA/metaGGA often better), band gap
11. band gap
    * fundamental gap (minimum gap)
    * direct gap (optical gap)
12. optimized effective potential method (OEP)

## summer schools putting the theory back in density functional theory

[link](http://www.ipam.ucla.edu/programs/summer-schools/putting-the-theory-back-in-density-functional-theory/?tab=schedule)

## ISTPC school

Hartree-Fock and post-Hartree-Fock methods: Computational aspects [youtube-link](https://youtu.be/mwbk1TfOOfo)

## vergil summer school

[link](http://vergil.chemistry.gatech.edu/opp/summer-lectures.html)

## book: the ABC to DFT

[useful-link](https://dft.uci.edu/learnDFT.php)

知乎专栏-密度泛函理论简介 [link](https://zhuanlan.zhihu.com/p/79570582)

chap1

1. atomic unit
   * $e=\hbar=m=1$
   * Hartree energy $1H=27.2114eV$
   * Bohr radius $0.529A$
2. H2 example
   * Hatree-Fock (HF)对于键长的预测误差还可接受，但是显著高估了基态能预测，因为HF未包含关联能correlation energy
3. 原子轨道线性组合是HF的视角
4. DFT和topological optimization有些相似

Lagrange multiplier (LM)

1. [wiki-Lagrange-multiplier](https://en.wikipedia.org/wiki/Lagrange_multiplier)
2. 名称约定
   * 目标函数`f`
   * 约束函数`g`
   * LM函数`L=f-lambda*g`
3. 引入`lambda`：在目标点，目标函数的梯度可以由约束函数的梯度线性组合得到
4. level set: 两个变量函数的等高线，两个及更多变量则叫做level set [wiki](https://en.wikipedia.org/wiki/Level_set)
5. LM的目标是寻找导数的零点，**不**等价于LM的local minimum/maximum，必须再加上saddle point
6. level set与约束函数相切的点一定是LM的目标，但不相切的点也可能是LM的目标，例如目标函数导数为零的点
7. LM函数甚至没有local minimum/maximum

functional

1. [wiki-functional-derivative](https://en.wikipedia.org/wiki/Functional_derivative)

many body physics

1. 实空间交换对称**不等价**于函数乘积

问题

1. Hohenberg-Kohn theorem. 给定`V_ext`是否唯一决定基态的density？换言之`V_ext`可能具有多个基态波函数，这些波函数是否给出相同的density？
   * a mathematical aspect of Hohenberg-Kohn theorem [arxiv](https://arxiv.org/pdf/1709.07118.pdf)
2. Hohenberg-Kohn theorem. 简并时，基态的不同简并态是否给出相同`V_ext`，如果不，那`V_ext`便不能由基态`rho`唯一确定，即违反HK-theorem

Hohenberg Kohn theorem

1. levy proof
2. 外势可以由density唯一确定
3. 基态简并波函数假设对应不同density，对应的外势只是泛函在不同极值点的变分
   * 多个density对应一个Vext，至少不违背HK定理，但怪怪的
4. 但没有论述「简并基态是否对应不同的density」。但感觉应该不能，例如对简并基态做线性组合，那density应该会连续变化（很不对劲）
