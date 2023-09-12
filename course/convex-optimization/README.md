# Convex optimization

edx/convex-optimization

Differentiable Convex Optimization Layers [arxiv](https://arxiv.org/abs/1910.12430)

`@book/convex-optimization` [link](https://web.stanford.edu/~boyd/cvxbook/)

1. notation
   * $\sup$: supremum
   * $\inf$: infimum
2. link
   * Carathéodory's theorem [wiki-link](https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_(convex_hull))
   * Estimating the probability that a given vector is in the convex hull of a random sample [doi-link](https://doi.org/10.1007/s00440-022-01186-1)
   * Farkas's lamma [wiki-link](https://en.wikipedia.org/wiki/Farkas%27_lemma)

$\sup$ and

## optimization problem

[wiki-link](https://en.wikipedia.org/wiki/Second-order_cone_programming)

abbreviation

1. SDP: semidefinite programming, positive semi-definite
2. SOCP: second-order cone programming
3. ILP: integer linear programming
4. LMI: linear matrix inequality
5. LSE: log-sum-exp, real-soft-max, multivariable softplus [wiki-link](https://en.wikipedia.org/wiki/LogSumExp)

```text
optimization
├─ convex programming
│  └─ semi-definite programming
│     └─ quadratic programming
│        └─ linear programming
└── nonconvex

nonlinear optimization
integer linear programming
```

least square programming

$$\min_x\; ||Ax-b||_2^2$$

$$A\in \mathbb{R}^{k\times n}, x\in\mathbb{R}^n, b\in\mathbb{R}^k$$

1. analytical solution $(A^T A)^{-1}A^T b$
2. computation time: $O(n^2k)$, less if structured
3. variant: including weights, adding regularization terms

linear programming

$$\max_x\; a\cdot x$$

$$s.t.\; Bx=b,Cx\leq c$$

$$a\in\mathbb{R}^k,x\in\mathbb{R}^k,B\in\mathbb{R}^{m\times k},b\in\mathbb{R}^m,C\in\mathbb{R}^{n\times k},c\in\mathbb{R}^n$$

1. no analytical formula for solution
2. reliable and efficient algorithm and software
3. computation time: $O(n^2m)$ if $m\geq n$, less with structure
4. a few standard tricks used to convert problems into linear programs

convex programming [wiki-link](https://en.wikipedia.org/wiki/Convex_optimization)

$$\min_x\; f(x)$$

$$s.t. g_i(x)\leq 0, i=1,\cdots, m$$

$$s.t. h_i(x)= 0, i=1,\cdots, n$$

$$x\in\mathbb{R}^k$$

1. $f,g_i$ are convex functions, $h_i$ are affine functions
2. no analytical solution
3. reliable and efficient algorithm
4. computation time (roughly): $max{k^3,k^2m,F}$, $F$ is cost of evaluating $f,g,h$ and their first and second derivatives
5. difficult to recognize a convex optimization problem
6. many tricks for transforming problems into convex form
7. many problems can be solved via convex optimization

set basic concept

1. interior $\mathrm{int}\;S$
   * [wiki-link](https://en.wikipedia.org/wiki/Interior_(topology))
   * the union of all open sets of $X$ contained in $S$
   * the complement of the closure of the complement of $S$
2. closure $\mathrm{cl}\; S$
   * [wiki-link](https://en.wikipedia.org/wiki/Closure_(topology))
   * the smallest closed set containing $S$
3. boundary
   * [wiki-link](https://en.wikipedia.org/wiki/Boundary_(topology))
   * $\partial S=\mathrm{cl}\;S\setminus\mathrm{int}\;S$

convex basic concept

1. convex set
   * $x=\theta x_1 + (1-\theta) x_2, 0\leq \theta\leq 1$
   * convex hull
2. affine set
   * $x=\theta x_1 + (1-\theta) x_2, \theta\in \mathbb{R}$
   * $\{x : Ax=b \}$
   * relative interior [wiki-link](https://en.wikipedia.org/wiki/Relative_interior)
   * affine hull $\mathrm{aff} S$
   * affine function: $f(x)=Ax+b$
3. convex example
   * line
   * line segment
   * ray
   * hyperplane $\{x:a\cdot x=b\}$
   * halfspace $\{x:a\cdot x\leq b\}$
   * norm ball $\{ x : ||x-x_c||\leq r \}$
   * Euclidean ball $B(x_c,r)=\{ x | \; ||x-x_c||_2\leq r \}= \{ x_c+ru | \; ||u||_2\leq 1 \}$
   * ellipsoid
     * $\{ x : (x-x_c)^TP^{-1}(x-x_c) \leq 1,P\succ 0 \}$
     * $\{ x_c + Au : ||u||_2\leq 1,A\in\mathrm{GL}(n) \}$
   * polyhedra
     * $\{x:Ax\leq b, Cx=d$, $A\in \mathbb{R}^{m\times n}, C\in \mathbb{R}^{p\times n}\}$
     * $\{\theta_1v_1+\cdots+\theta_nv_n:\theta_i\geq 0,\theta_1+\theta_2+\cdots+\theta_k=1,k\leq n\}$
     * the size of the second description (convex hull) can be exponential in dimension
   * polytope
     * bounded polyhedra
     * $\{\theta_1v_1+\cdots+\theta_nv_n:\theta_i\geq 0,\theta_1+\theta_2+\cdots+\theta_n=1\}$
   * $k$-simplex [wiki-link](https://en.wikipedia.org/wiki/Simplex)
     * convex hull of $k+1$ affinely-independent points
     * unit simplex $\{x:\sum_{i=1}^n x_i\leq 1,x_i\geq 0\}$
     * probability simplex $\{x:\sum_{i=1}^n x_i= 1,x_i\geq 0\}$
     * $0$-simplex: point
     * $1$-simplex: line segment
     * $2$-simplex: triangle
4. perspective function $\mathbb{R}^n\times \mathbb{R}_{++}\to\mathbb{R}^n:f(x,t)=x/t$
5. convexity preserving operation
   * (infinite) intersection
   * affine function: image and preimage
     * hyperbolic cone $\{ x | x^TPx \leq (c^Tx)^2; c^Tx \geq 0\}$ with $P\in S^n_+$
     * LMI $\{ x : x_1A_1+\cdots x_mA_m \preccurlyeq B \}$ with $A_i,B \in S^n$
   * perspective function: image and preimage
   * linear fractional function $f(x)=\frac{Ax+b}{cx+d},cx+d>0$: image and preimage
6. every closed convex set is the intersection of halfspaces
7. supporting hyperplane

cone

1. cone: $a\geq 0,b\geq 0,x\in A,y\in A\rightarrow ax+by\in A$
2. proper cone
   * convex cone
   * closed cone
   * solid cone (has nonempty interior) $\mathrm{int}\;C\ne\emptyset$
   * pointed cone (has no line) $C\cap (-C)=\{0\}$
3. cone hull of a set
4. norm cone $\{ (x,t) |\; ||x||\leq t \}$
   * second order cone, Lorentz cone, ice-cream cone, quadratic cone
5. definite cone
   * (subspace, not a cone) symmetric matrix $S^n=\{x\in\mathbb{R}^{n\times n}:x=x^T\}$
   * positive semidefinite cone $S^n_+=\{ X\in S^n | X\succcurlyeq 0 \}$
   * positive definite cone $S^n_{++}=\{ X\in S^n | X\succ 0 \}$
6. partial order on a proper cone $K$
   * $x\preceq_K y\leftrightarrow y-x\in K$
   * $x\prec_K y\leftrightarrow y-x\in \mathrm{int}\;K$
   * example
     * nonnegative orthant, componentwise order
     * positive semidefinite cone, Loewner order [wiki-link](https://en.wikipedia.org/wiki/Loewner_order)
     * nonnegative polynomial cone
   * minimum element $S\subseteq x+K$
   * minimal element $S\cap (x-K)=\{x\}$
7. dual cone
   * $K^*=\{y : \forall x\in K,\langle y, x\rangle \geq 0\}$
   * property
     * $K^*$ is convex, closed
     * $K_1\subseteq K_2\rightarrow K_2^*\subseteq K_1^*$
     * if $K$ is solid, then $K^*$ is pointed
     * if $\mathrm{cl}\; K$ is pointed, then $K^*$ is solid
     * $K^{**}=\mathrm{conv\;cl}\; K$
     * if $K$ is proper, then $K^*$ is proper
   * example
     * $K=\mathbb{R}_+^n=K^*$
     * $K=S_+^n=K^*$, matrix inner product $\langle y, x\rangle=\mathrm{Tr}[xy^T]$
     * $K=\{(x,t) : ||x||_2\leq t\}=K^*$, self-dual
     * $K=\{(x,t) : ||x||_1\leq t\}$, $K^*=\{(x,t) : ||x||_\infty\leq t\}$
8. dual generalized inequality
   * $x\preceq_K y$ if and only if $\forall \lambda \succeq_{K^*}0,\langle \lambda,x\rangle\leq \langle \lambda,y\rangle$
   * $x\prec_K y$ if and only if $\forall \lambda \succeq_{K^*}0,\lambda\ne 0,\langle \lambda,x\rangle< \langle \lambda,y\rangle$
9. minimum and minimal
   * minimum w.r.t. $\preceq_K$: $x$ is minimum element of $S$ iff for all $\lambda \succ_{K^*} 0$, $x$ is the unique minimizer of $\lambda^Tz$ over $S$
   * minimal
     * if $x$ minimizes $\lambda^Tz$ over $S$ for some $\lambda\succ_{K^*} 0$, then $x$ is minimal w.r.t. $\preceq_K$
     * if x is a minimal element of a convex set $S$ w.r.t. $\preccurlyeq_K$, then there exists a nonzero $\lambda\succeq_{K^*}0$ such that $x$ minimizes $\lambda^Tz$ over $S$

## chap0 introduction

1. concept
   * optimization variables, objective function, constraint, optimal solution
   * optimization problem: least-square problems, linear programming, convex optimization, SDP, SOCP
   * convex optimization, local optimization, global optimization
   * closure
   * relative boundary
2. insight
   * the correct thing to estimate is not the co-variance. The correct parameter to estimate is the inverse co-variance
   * the correct thing to estimate is not the mean of a bunch of vectors. It's the co-variance inverse times the mean
3. algorithm history
   * 1947: simplex algorithm for linear programming (Dantzig)
   * 1960s: early interior-points methods (Fiacco, McCormick, Dikin)
   * 1970s: ellipsoid method and other subgradient methods
   * 1980s: polynomial-time interior-point methods for linear programming (Karmerkar 1984)
   * late 1980s-now: polynomial-time interior-point methods for nonlinear convex optimization (Nesterov, Nemirovski, 1994)
4. application history
   * before 1990: mostly in operations research
   * since 1990: in engineering (control, signal processing, communications, circuit design), semidefinite and second-order cone programming ,rebust optimization
5. separating hyperplane theorem [wiki-link](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem)
   * strict seperation
6. supporting hyperplane theorem [wiki-link](https://en.wikipedia.org/wiki/Supporting_hyperplane)
7. theorem of alternatives
   * Farkas lemma [wiki-link](https://en.wikipedia.org/wiki/Farkas%27_lemma)
   * strict linear inequalities (eq-2.17)
   * strict linear generalized inequalities (eq-2.21)
8. Pareto optimal

## chap2 convex function

1. convex function
   * (Jensen's inequality) $f(\alpha x + \beta y)\leq \alpha f(x) +\beta f(y), \alpha+\beta=1,\alpha\geq 0, \beta \geq 0$
   * continuous in relatively interior of domain
   * extended-value extension $\tilde{f}$
   * first order condition $f(y)\geq f(x) + (y-x)^T\nabla f(x)$
   * second-order condition $\nabla^2f(x)\succeq 0$
   * convex domain
   * strictly convex, concave, strictly concave
2. convex function example
   * indicator function of a set $I_C(x)=0$ if $x\in C$, otherwise $\infty$
   * (convex and concave) affine function $f(x)=Ax+b$
   * exponential $f(x)=e^{ax}$
   * $f(x)=x^\alpha, x\in\mathbb{R}_{++},\alpha\in (-\infty,0]\cup [1,\infty)$
   * $f(x)=-x^\alpha, x\in\mathbb{R}_{++},\alpha\in [0,1]$
   * $f(x)=|x|^p$， $p\geq 1$
   * $f(x)=-\log(x),x\in\mathbb{R}_{++}$
   * negative entropy $f(x)=x \log(x),x\in\mathbb{R}_{++}$
   * norm: spectral norm (maximum singular value)
   * maximum $f(x)=\max\{x_1,x_2,\cdots,x_n\},x\in\mathbb{R}^n$
   * quadratic-over-linear $f(x,y)=x^2/y, x\in\mathbb{R}, y\in\mathbb{R}_{++}$
   * log-sum-exp $f(x)=\log(\sum_i e^{x_i}),x\in\mathbb{R}^n$
   * geometric mean $f(x)=-(\prod_k^n{x_k})^{1/n}, x\in R^n_{++}$
   * $f(x)=-\log(\mathrm{Det}(X))$ for $X\in S^n_{++}$
   * $f(x,Y)=x^TY^{-1}x:\mathbb{R}^n\times S_{++}^n\to\mathbb{R}$
   * matrix fractional function $f(x,Y)=x^TY^{-1}x:\mathbb{R}^n\times \mathbb{S}^n_{++}\to\mathbb{R}$
   * support function of a set $C$: $S_C(x)=\sup \{x\cdot y:y\in C\}$
3. $\alpha$-sublevel set of function $f$
   * $C_\alpha=\{x\in \mathrm{dom}f : f(x)\leq \alpha\}$
   * if $f$ is convex function, then $C_\alpha$ is a convex set
4. function graph $f:\mathbb{R}^n\to \mathbb{R}$
   * graph $\{(x,f(x))\in\mathbb{R}^{n+1} : x\in \mathrm{dom} f\}$
   * epigraph: $\mathrm{epi} f=\{(x,t)\in\mathbb{R}^{n+1} : x\in \mathrm{dom} f, f(x)\leq t\}$
   * hypograph: $\mathrm{hypo} f=\{(x,t)\in\mathbb{R}^{n+1} : x\in \mathrm{dom} f, f(x)\geq t\}$
   * $f$ is convex iff $\mathrm{epi} f$ is a convex set
5. Jensen's inequality extension: random variables and expectation $f(\mathbf{E} x)\leq \mathbf{E}f(x)$
   * arithmetic-geometric mean inequality $2\sqrt{ab}\leq (a+b)$
   * Holder's inequality [wiki-link](https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality)
6. operations that preserve convexity
   * nonnegative weighted sum $g(x)=\sum_i w_if_i(x),w_i>0$
   * composition with affine function $g(x)=f(Ax+b)$
   * pointwise maximum and supremum $g(x)=\max\{f_1(x),f_2(x),\cdots,f_m(x)\}$
   * $g(x)=\inf_{y\in C} f(x,y)$, $C$ is a convex set, $f(x,y)$ is convex in $(x,y)$, $\mathrm{dom}\;g$ has some constraint
   * perspective
   * composition $h:\mathbb{R}^k\to\mathbb{R}$, $g:\mathbb{R}^n\to\mathbb{R}^k$, $f(x)=h\circ g(x)=h(g(x))$
     * $k=1,f''(x)=h''(g(x))g'(x)^2+h'(x)g''(x)$
7. Schur complement
8. conjugate function
   * dual, conjugate, adjoint, transpose
   * $f^*(y)=\sup_{x\in \mathrm{dom}f} (y^Tx-f(x))$
   * $f^*$ is convex, even if $f$ is not
   * example: $f(x)=-\log(x)$, $f^*(y)=-1-\log(-y)$ for $y<0$ otherwise $\infty$
   * example: $f(x)=x^TQx/2$ with $Q\in S_{++}^n$, $f^*(y)=y^TQ^{-1}y/2$

quasi-

1. quasiconvex functions $f: R^n\to R$
   * $\mathrm{dom} f$ is convex, sublevel sets $S_\alpha=\{x\in \mathrm{dom}f | f(x)\leq \alpha\}$ are convex for all $\alpha$
   * uni-model
   * $f$ is quasiconcave if $-f$ is quasiconvex
   * $f$ is quasilinear if it is quasiconvex and quasiconcave
   * $\sqrt{|x|}$ on $R$
   * $\mathrm{ceil}(x)=\inf\{z\in \mathbb{Z} | z\geq x\}$ is quasilinear
   * $\log(x)$ is quasilinear on $R_{++}$
   * $f(x,y)=xy$ is qusiconcave on $R_{++}^2$
   * linear-fractional function $f(x)=\frac{a^Tx+b}{c^Tx+d};\mathrm{dom}f=\{x | c^Tx+d>0\}$ is quasilinear
   * distance ratio $f(x)=\frac{||x-a||_2}{||x-b||_2}; \mathrm{dom} f=\{x | \; ||x-a||_2\leq ||x-b||_2\}$ is quasiconvex
2. modified Jensen inequality: for quasiconvex $f$: $0\leq \theta \leq 1 \Rightarrow f(\theta x+(1-\theta)y)\leq \max\{f(x),f(y)\}$
3. first-order condition: differentiable $f$ with convex domain is quasiconvex iff $f(y)\leq f(x) \Rightarrow \nabla f(x)^T (y-x)\leq 0$

log-concave and log-convex function

1. log-concave and log-convex
   * $f$ is positive
   * $f(\theta x+ (1-\theta)y)\geq f(x)^\theta f(y)^{1-\theta}; \forall 0\leq \theta\leq 1$
   * $f$ is log-concave if $\log f$ is concave. $f$ is log-concex if $\log f$ is convex
   * example: $x^a$ on $R_{++}$ is log-convex for $a\leq 0$, log-concave for $a\geq 0$
   * Gaussian distribution pdf are log-concave $f(x)=\frac{1}{\sqrt{(2\pi)^n\det \Sigma}}e^{-\frac{1}{2}(x-\bar{x})^T\Sigma^{-1}(x-\bar{x})}$
   * cumulative Gaussian distribution function is log-concave $\Psi(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^x{e^{-u^2/2}du}$
2. property
   * convex domain, twice differentiable, $f$ is log-concave iff $f(x)\nabla^2f(x) \preccurlyeq \nabla f(x) \nabla f(x)^T; \forall x\in \mathrm{dom} f$
   * product of log-concave is log-concave
   * sum of log-concave is **NOT** always log-concave
   * integration: if $f: R^n\times R^m\to R$ is log-concave, then $g(x)=\int f(x,y)dy$ is log-concave
   * convolution: $f*g(x)=\int f(x-y)g(y)dy$ of log-concave function $f,g$ is log-concave
   * if $C\subseteq R^n$ convex and $y$ is a random variable with log-concave pdf then $f(x)=\mathrm{prob}(x+y\in C)$ is log-concave
3. example: yield function $Y(x)=\mathrm{prob}(x+\omega \in S)$

convexity with respect to generalized inequalities

1. K-convex
   * $f: R^n\to R^m$ is K-convex if $\mathrm{dom} f$ is convex and $f(\theta x + (1-\theta)y) \preccurlyeq \theta f(x) + (1-\theta)f(y)$ for $x,y\in \mathrm{dom} f, 0\leq\theta \leq 1$
   * example: $f: S^m\to S^m$, $f(X)=X^2$ is $S_+^m$-convex

## chap3 convex optimization problems

1. optimization problem in standard form
   * optimization variable (decision variable)
   * cost function
   * inequality constraint functions
   * equality constraint functions
   * optimal value
2. feasible, optimal, locally optimal
3. feasibility problem
4. standard form of convex optimization problem: $f_0,f_1,\cdots,f_m$ are convex; equality constraints are affine
5. standard form of quasiconvex optimization problem: $f_0$ is quasiconvex, $f_1,f_2,\cdots,f_m$ is convex
6. any locally optimal point of a convex problem is globally optimal
7. optimality criterion for differentiable $f_0$
   * $x$ is optimal iff it's feasible and $\nabla f_0(x)^T(y-x)\geq 0$ for all feasible $y$
   * unconstrained problem: $x\in\mathrm{dom}f$ is optimal iff $\nabla f_0(x)=0$
   * equality constrained problem: $x$ is optimal iff there exists $\nu$ such that $x\in \mathrm{dom} f, Ax=b, \nabla f_0(x)+A^T\nu=0$
   * minimization over nonnegative orthant (see slides)
8. equivalent
   * eliminating equality constraints
   * introducing equality constraints
   * introducing slack variables for linear inequalities
   * epigraph form
   * minimizing over some variables
9. quasiconvex optimization
   * can have locally optimal points that are not globally optimal
   * convex representation of sublevel sets of a quasiconvex function
10. $\mathrm{LP}\subset \mathrm{QP}\subset \mathrm{QCQP} \subset \mathrm{SOCP} \subset \mathrm{SDP}$
11. linear programming (LP)
    * example: piecewise-linear minimization
    * example: Chebyshev center of polyhedron
    * linear-fractional programming: quasi-convex
    * generalized linear-fractional programming, Von Neumann growth model
12. quadratic programming (QP)
    * least-squares
    * linear program with random cost
13. quadratically constrained quadratic program (QCQP)
14. second order cone programming (SOCP)
    * square is bad (may not PSD)
    * robust linear programming: deterministic model, stochastic model
15. geometric programming (GP)
    * monomial function: $f(x)=cx_1^{a_1}x_2^{a_2}\cdots x_n^{a_n}, \mathrm{dom}f=R_{++}^n,c>0,a_i\in R$
    * posynomial function: sum of monomial
    * GP: minimize $f_0(x)$, subject to $f_i(x)\leq 1, i=1,\cdots, m$ $h_i(x)=1, i=1,\cdots,p$ with $f_i$ posynomial and $h_i$ monomial
    * change variables $y_i=\log (x_i),b=\log(c)$
16. generalized inequality constraints
    * conic form problem: minimize $c^Tx$ subject to $Fx+g\preccurlyeq_K 0$, $Ax=b$
    * extends linear programming $K=R_+^m$ to nonpolyhedral cones
17. semidefinite programming (SDP)
    * linear matrix inequality (LMI)
    * Schur complement
    * eigenvalue minimization
    * matrix norm minimization
18. vector optimization
    * general vector optimization $f_0: R^n\to R^q$ : minimize (w.r.t $K$) $f_0(x)$, subject to $f_i(x)\leq 0, i=1,\cdots m$, $h_i(x)= 0,i=1,\cdots,p$
    * convex vector optimization: minimize (w.r.t $K$) $f_0(x)$, subject to $f_i(x)\leq 0, i=1,\cdots m$, Ax=b$ with $f_0$ K-convex, $f_1,\cdots,f_m$ convex
    * set of achievable object values $O=\{f_0(x) | x \mathrm{feasible}\}$
    * feasible $x$ is optimal if $f_0(x)$ is the minimum value $O$
    * feasible $x$ is Pareto optimal if $f_0(x)$ is the minimal value $O$
    * multicriterion optimization
    * example: regularized least-squares
    * example: risk return trade-off in portfolio optimization
    * scalarization: weighted minimization
19. boolean linear program

## chap4 duality

1. Lagrangian
   * standard form problem (not necessarily convex): minimize $f_0(x)$, subject to $f_i(x)\leq 0, i=1,\cdots m$, $h_i(x)= 0,i=1,\cdots,p$
   * variable $x\in R^n$, domain $D$, optimal value $p^*$
   * $L(x,\lambda,\nu)=f_0(x)+\sum_{i=1}^{m}\lambda_if_i(x) + \sum_{i=1}^{p}\nu_ih_i(x)$
   * Lagrange dual function $g: R^m\otimes R^p\to R$: $g(\lambda,\nu)=\inf_{x\in D} L(x,\lambda,\nu)$
   * $g$ is concave
   * lower bound property: if $\lambda \succcurlyeq 0$, then $g(\lambda,\nu)\leq p^*$
   * connection with conjugate function
2. Lagrange dual problem
   * maximize $g(\lambda,\nu)$ subject to $\lambda \succcurlyeq 0$
   * optimal value denoted $d^*$, with $p^*\geq d^*$
3. duality
   * weak duality $d^*\leq p^*$
   * strong duality $d^*=p^*$: does not hold in general, (usually) holds for convex problem
   * duality gap $p^*-d^*$
   * constraint qualifications: conditions that guarantee strong duality in convex problems
4. Slater's constraint qualification
5. geometric interpretation
6. complementary slackness
7. Karush-Kuhn-Tucker (KKT) conditions
8. perturbation and sensitivity analysis
   * global sensitivity
   * local sensitivity
9. duality and problem reformulation
10. implicit constraints (partial Lagrangian)
11. generalized inequalities
