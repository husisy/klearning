# GAMES201

课程主页 [link](http://games-cn.org/games201/) [true-link](https://yuanming.taichi.graphics/teaching/2020-games201/)

taichi论坛 [link](https://forum.taichi.graphics/)

课程仓库 [link](https://github.com/taichi-dev/games201)：代码与讲义

课程目标：自己动手大早影视级物理引擎

## lec01

1. 物理引擎physics engine
   * 刚体动力学rigid body dynamics
   * 软体动力学soft body dynamics
   * 流体动力学fluid dynamics
2. 应用：CAD/CAE, visual effects (film), VR/AR, training robots, games
3. 游戏
   * angry birds (2009)
   * the incredible machines (1993)
   * Phun/algodoo (2009)
   * Besieged (2015)
   * the legend of Zelda: Breath of the Wild (2017)
   * Ori and the will of the wisps (2020)
4. 弹簧质点系统
5. keywords: discretization, efficient solver, productivity, performance, hardware architecture, data structure, parallelization
6. tensor: scalar, vector, matrix
7. pointer是万恶之源，编译器难以优化
8. `ti.kernel`: compiled, statically-typed, lexically-scoped, parallel, differentiable
9. `ti.func`: 强行inline，不支持递归
10. scalar math: `ti.random`, `abs`
11. chaining comparison `a<b<=c!=d`
12. `ti.Matrix`仅用于小矩阵
13. `ti.Vector`是仅有一列的`ti.Matrix`
14. range-for loop, struct-for loop
    * 最外层for-loop并行
15. atomic operation `+=`, `ti.atomic_add()`
16. taichi-scope, python-scope
17. phase: initialization, tensor allocation, computation, restart `ti.reset()`
18. debug mode `ti.init(debug=True)`，仅debug mode下, cpu-backend上进行数组越界检查
19. megakernel来缓解访问存储

## lec02

1. yapf,pep8格式化
2. `ti.core.toggle_advanced_optimization(False)`关闭掉一些较高级的优化，来缩短编译时间
3. Lagrangian, Eulerian view
4. 通常来说Lagrangian view是粒子，Eulerian view通常是网格
5. 弹簧质点系统mass-spring systems：布料，头发
6. damping, stiffness
7. 时间积分
   * forward Euler
   * semi-implicit Euler (aka. symplectic Euler, explicit)
   * backward Euler (Newton's method)
8. 显式explicit / 隐式implicit time integrators
   * 显式：容易实现，容易爆炸 $\delta t \leq c  \sqrt{m/k}, c\tilde 1$，越硬的材料越容易炸
   * 隐式：难以实现，难以优化，可以使用更大的步长，numerical damping, locking
9. 隐式积分器：Taylor展开线性化，Jacobi/Gauss-Seidel/conjugate-gradient
10. 解线性方程组：迭代法，sparse matrix, conjugate gradients, precondition, position-based dynamics
    * @paper fast mass-spring system solver
11. smoothed particle hydrodynamics (SPH)
    * 不需要mesh，非常适合free-surface flow
    * 直观上易于理解
    * equation of state (EOS)
    * weakly compressible SPH (WCSPH)
12. Material Point Method (MPM)
13. Courant-Friedrichs-Lewy (CFL) condition：从粒子速度来考虑步长限制
    * SPH `~0.4`
    * MPM `0.3~1`
    * FLIP fluid (smoke) `1~5+`
14. accelerating SPH: neighborhood search, compact hashing
15. other method
    * discrete element method
    * moving particle semi-implicit (MPS)
    * power particles: an incompressible fluid solver based on power diagrams
    * a peridynamic perspective on spring-mass fracture
16. 文章阅读 interlinked SPH pressure solvers for strong fluid-rigid coupling
17. 表面重建: matching cubes (openVDB, levelset)

## lec3 弹性、有限元基础、taichi高级特性

1. elastic material很Q弹，viscoelastic, elastoplastic, viscoplastic
   * 推荐阅读材料：the classical FEM method and discretization methodology, Eftychios Sifakis
   * the material point method for simulating continuum materials, Chenfanfu Jiang et al.
2. 形变deformation：deformation map $\phi$, deformation gradient, volume ratio
3. hyperelasticity material, strain energy density function $\Psi$
   * strain暂且当做是deformation gradient
4. stress: the material's interal elastic forces
   * the First Piola-Kirchhoff stress tensor (PK1): rest space
   * Kirchhoff stress $\tau$
   * Cauchy stress tensor $\sigma$：symmetric because of conservation of angular momentum
5. traction牵引力
6. elastic moduli杨氏模量
7. Poisson's ratio泊松比
   * 橡皮筋的泊松比是正的：拉拽下中间截面积变小
   * auxetics: 负泊松比材料
8. Lame parameters $\lambda$, $\mu$
9. hyperelastic material模型
   * linear elasticity：存在旋转后体积变大的问题
   * Neo-Hookean
   * fixed corotated
10. finite element method (FEM): Galerkin discretization scheme that builds discrete equations using weak formulations of continuous PDEs
11. periodic table of the finite element method [link](https://www-users.cse.umn.edu/~arnold/femtable/)
12. linear tetrahedral FEM
13. 连续介质力学

taichi

1. object data-oriented programming (OOP)
2. `ti.data_oriented`, `ti.kernel`, `tf.func`
3. metaprogramming

## lec4 Euler view

1. spatial discretization
   * cell-centered grid
   * staggered grids: 方便有限差分，避免checkboard pattern
   * bilinear/bicubic interpolation
2. advection scheme: trade-off between numerical viscosity, stability, performance and complexity
   * semi-lagrangian advection
   * MacCormack/BFECC
   * BiMocq
   * particle advection (PIC/FLIP/APIC/PolyPIC)
3. semi-lagrangian advection
   * 越转越小，越来越模糊
   * go back in time: forward Euler, explicit midpoint (RK2), RK3
4. Back and Forth Error Compensation and Correction (BFECC): 解决变糊问题
   * 存在overshooting问题，引入clipping

(lost)

1. chorin-style projection
   * Poisson's equation
   * spatial discretization: Direchlet and Neumann boundary condition
2. top10 algorithm from the 20 century
   * Krylov subspace iteration method
   * fast Fourier transform
   * fast multiple method
3. large-scale linear system
   * direct solver (e.g. PARDISO): 小系统
   * iterative solver: Gauss-Seidel, Jacobi, Krylov-subspace solver(conjugate gradients)
   * good numeric solvers are usually composed of different solvers: multigrid-preconditioned conjugate gradients with damped Jacobi smoothing and PARDISO at the bottom multigrid level
4. 矩阵存储
   * dense matrix
   * sparse matrix
   * matrix-free, don't store it at all
5. Krylov-subspace solvers
   * conjugate gradients (CG)
   * conjugate residuals (CR)
   * generalized minimal residual method (GMRES)
   * biconjugate gradient stabilized (BiCGStab)
   * @book-an-introduction-to-the-conjugate-gradient-method-without-the-agonizing-plain
6. eigenvalues and condition number
7. iterative solver trick: warm starting
   * 对于Jacobi/Gauss-Seidel/CG帮助显著
   * 对于MGPCG帮助不大
8. preconditioning
   * better eigenvalue clustering
   * Jacobi preconditioner `M=diag(A)`
   * Poisson preconditioner
   * (incomplete) Cholesky decomposition
   * multigrid p
   * fast multiple method
9. multigrid design space
10. multigrid preconditioned conjugate gradients (MGPCG)
    * @book(2000) a multigrid tutorial
    * @book(2010) a parallel multigrid poisson solver for fluids simulation on large grids
    * `ti example mgpcg_advanced`
11. `ti example stable_fluid`
12. @paper(2015) combining advection with reflection: IVOCK
13. @paper(2018) advection reflection solver

## lec5 Poisson's equation and fast multiple method

1. fast multiple method
2. tree code
3. m2m transform
4. m2l transform
5. l2l transform, Honer scheme
6. boundary element method
7. PPPM: combining PDE form and summation forms
8. kernel independent FMM

作业1获奖作业 [link](https://zhuanlan.zhihu.com/p/158962220)

## lec6 线性弹性有限元和拓扑优化

1. 有限元，Galerkin methods
   * convert strong-form PDEs to weak forms, using a test function
   * integrate by parts to redistribute gradient operators
   * use the divergence theorem to simplify equations and enforce Neumann boundary conditions
   * discretization (build the stiffness matrix and right-hand side)
   * solve linear system
2. Cauchy momentum equation
3. 三角形网格
   * 方便贴合边界
   * 方便网格密度渐变
4. `Ku=f`
   * `K`: stiffness matrix
   * `u`: degree of freedoms, solution vector
   * `f`: load vector
5. linear elasticity, Cauchy momentum equation
   * strain tensor, Cauchy stress tensor
6. topology optimization: solid isotropic material with penalization (SIMP), optimility criterion (OC)
   * minimal compiance
7. 2D方格点上的FEM $\phi _{ij}=\left( 1-\left| x \right| \right) \left( 1-\left| y \right| \right)$ 详细推导见`draft00.afx`

## lec7 混合欧拉-拉格朗日视角

1. 关键因素
   * conservation of physical quantities: momentum, angular momentum, volume (incompressibility), energy(low dissipation)
   * performance: parallelism, locality on modern hardware
   * complexity
2. hybrid Eulerian-Lagrangian scheme
3. Particle-in-cell (PIC)
4. APIC
5. PolyPIC
6. FLIP
7. material point method (MPM)
   * automatic coupling of different materials (liquids, solids, granular materials)
   * automatic (self-)collision handling
   * automatic ffracture
   * capable of simulating large deformations
8. Moving Least Squares MPM (MLS-MPM)
   * halves the required FLOPs of MPM

## lec8 混合欧拉-拉格朗日视角2

MLS-MPM theory and implementation

1. constitutive models in MPM
   * liquid: equation of states
   * solid: NeoHookean, corotated
   * elastoplastic object (snow, sand): Yield criteria, ad-hoc boxing, Cam-clay, Drucker-prager, NACC
2. MPM: element-free Galerkin (EFG)
   * MPM particles correspond to FEM quadrature points, instead of elements
   * MPM typically uses one-point quadrature rule
   * MPM equations are derived using weak formulation
3. MLS-MPM almost always uses the APIC transfor scheme
4. deformation: velocity gradients
5. boundary condition: sticky, slip, separate
   * gravity
   * collision object
   * coulomb friction

## lec9 高性能计算与引擎

@book-computer-systems-a-programmer's-perspective

@book-what-every-programmer-should-know-about-memory

## lec10 总结

todo

## 个人笔记

1. 是否要绑定数组，还是走全局变量
2. 接触tensor allocation

layout设计

```text
np.array(shape=[], layout=[])
[3,4j,[i32,f32,i32]]
shape=[128,128,128], layout=[(0,0,32),(1,0,32),(2,0,32),(0,1,4),(1,1,4),(2,1,4)]
```
