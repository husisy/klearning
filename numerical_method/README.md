# naumrical method

## 偏微分方程

1. link
   * [NTNU/numerical-methods-for-engineers](https://folk.ntnu.no/leifh/teaching/tkt4140/._main000.html)
   * [Neumann-boundary-condition](https://folk.ntnu.no/leifh/teaching/tkt4140/._main056.html)
   * [github/lrhgit/tkt4140](https://github.com/lrhgit/tkt4140)
2. concept
   * predictor and corrector
   * generic explicit numerical scheme
   * exact differential operator
   * approximate differential operator
   * local truncation error (LTE)
   * Runge-Kutta-Fehlberg scheme with variable time step (RKF45)
   * Newton's first differential equation
3. Numerical amplification factor, absolute stability。考虑`a<0`的指数pde方程`y'=ay`，当数值求解的`h`过大时会导致解振荡（正负交替）
   * 从稳定性的角度来说，高阶RK方法不会显著提高稳定性
4. stiff equation
   * ODE solution has different time scales `y_fast + y_slow`
   * `y'=f(x,y)`中Jacobian matrix $\frac{\partial f}{\partial y}$的条件数较大
5. boundary value problem (BVP)
   * shoting method, finite difference method
   * 线性BVP问题，一个未知初始条件通过两次`s`猜测便可以求解出`s_star`，两个未知初始条件需要三次`(s,r)`猜测
   * 非线性BVP问题，需要通过割线法secant method求解`s_star`
   * Picard linearization: 简单，收敛不快，初值猜测
   * Newton linearazation：比Picard收敛快
   * 线性化再二阶导，二阶导再线性化 [link](https://folk.ntnu.no/leifh/teaching/tkt4140/._main047.html)
6. heat diffusion problem, Boltzmann transformation
7. 迭代停止条件：相对误差，绝对误差
8. incompressible fluid Navier-Stokes方程
   * transport term: nonlinear, first-order derivative
   * diffusive term: linear, second-order derivative
9. 常见pde: Poisson, diffusion, wave, advection
10. first linear order pde, characteristic curve, compatibility equation
11. burger's equation 没看懂
12. second order pde
    * nonlinear, quasi-linear, semi-linear, linear
    * hyperbolic, parabolic, elliptic
    * hyperbolic pde: region of influence, region of dependency
    * elliptic pde: 完全有边界条件决定, Dirichlet/Neumann/Robin boundary condition
    * parabolic pde: characteristic curve特征曲线与坐标轴平行，划分为region of influence, region of dependency
13. elliptic pde: Laplace/Poisson/Helmholtz pde
    * 对于Neumann边界条件，需要引入ghostcell
14. 迭代方法：Jacobi, Gauss-Seidel, successive over-relaxation (SOR)
    * optimal relaxation parameter, Garabedian's estimate
    * initial guess
15. parabolic pde, heat diffusion problem
    * Forward Time Central Space (FTCS) scheme, Euler scheme
    * stability, PC-criterion, Bender-Schmidt formula, von Neumann analysis, generalized von Neumann analysis （考虑heat sink/source）
    * Dufort Frankel scheme (1953)
    * Crank-Nicolson scheme, $\theta$ scheme：`theta=1/2`对应CN scheme，`theta=0`对应FTCS scheme。CN scheme依旧可能出现振荡，可以通过增大theta来缓解
    * truuncation error, consistency, convergence
    * Lax's equivalence theorem: Given a well-posed linear initial value problem and a consistent numerical scheme, stability of the same scheme is a necessary and sufficient condition for convergence
16. hyperbolic pde, convection problem, conservative scheme
    * FTCS-scheme: unconditional unstable，几乎不可用
    * Courant–Friedrichs–Lewy (CFL) number, [wiki](https://en.wikipedia.org/wiki/Courant%E2%80%93Friedrichs%E2%80%93Lewy_condition)
    * upwind scheme (FTBS): 仅用于convection term，不用于diffusive term，稳定条件`C<=1`
    * numerical viscosity, numerical propagation speed
    * Cauchy-Kowalewsky procedure, Warming-Hyett procedure
    * dissipative error, disperssion error
    * Lax-Wendroff scheme (1960)
    * Lax Friedrich scheme
    * Richtmyer Scheme
    * MacCormack Scheme
    * forward time backward space (FTBS) scheme
    * 为了获得准确率，CFL number需要更接近1，而此时数值方法也会变得更不稳定，尤其是二阶方法（主要体现在波形不连续处）
    * flux limiter, minmod, superbee, Van-leer @TODO
    * Burger's equation @TODO
