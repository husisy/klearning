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

$\sup$ and

## chap0 introduction

1. (math) optimization
   * `s.t.` subject to
   * optimization variables
   * objective function
   * constraint functions
   * optimal solution
2. example
   * portofolio optimization
   * device sizing in electronic circuits
   * data fitting
3. optimization problem
   * general: different, computation time, not always finding the solution
   * exception (easy to solve): least-square problems, linear programming, convex optimization
4. least squares
   * $\min ||Ax-b||_2^2$
   * $A\in \mathbb{R}^{k\times n}$
   * analytical solution $(A^T A)^{-1}A^T b$
   * computation time: $O(n^2k)$, less if structured
   * a few standard techniques increase flexibility: including weights, adding regularization terms
5. linear programming
   * $\min c^T x$
   * $s.t. a_i^T x\leq b_i, i=1,\cdots,m$
   * no analytical formula for solution
   * reliable and efficient algorithm and software
   * computation time: $O(n^2m)$ if $m\geq n$, less with structure
   * a few standard tricks used to convert problems into linear programs
6. convex optimization
   * $\min f_0(x)$
   * $s.t. f_i(x)\leq b_i, i=1,\cdots, m$
   * $f_0,f_i$ are convex functions $f(\alpha x + \beta y)\leq \alpha f(x) +\beta f(y), \alpha+\beta=1,\alpha\geq 0, \beta \geq 0$
   * special case: least  squares, linear programs
   * no analytical solution
   * reliable and efficient algorithm
   * computation time (roughly): $max{n^3,n^2m,F}$, $F$ is cost of evaluating $f_i$ and their first and second derivatives
   * difficult to recognize a convex optimization problem
   * many tricks for transforming problems into convex form
   * surprisingly many problems can be solved via convex optimization
7. hints
   * the correct thing to estimate is not the co-variance. The correct parameter to estimate is the inverse co-variance
   * the correct thing to estimate is not the mean of a bunch of vectors. It's the co-variance inverse times the mean
8. nonlinear optimization: local optimization methods
   * find a point that minimizes $f_0$ among feasible points near it
   * fast
   * requre initial guess
   * no information about distance to global optimum
9. nonlinear optimization: global optimization methods
   * worst-case complxity grows exponentially with problem size
10. integer linear programming (ILP)
11. algorithm history
    * 1947: simplex algorithm for linear programming (Dantzig)
    * 1960s: early interior-points methods (Fiacco, McCormick, Dikin)
    * 1970s: ellipsoid method and other subgradient methods
    * 1980s: polynomial-time interior-point methods for linear programming (Karmerkar 1984)
    * late 1980s-now: polynomial-time interior-point methods for nonlinear convex optimization (Nesterov, Nemirovski, 1994)
12. application history
    * before 1990: mostly in operations research
    * since 1990: in engineering (control, signal processing, communications, circuit design), semidefinite and second-order cone programming ,rebust optimization

## chap1 convex sets

1. affine set
   * $x=\theta x_1 + (1-\theta) x_2, \theta\in \mathbb{R}$
   * example: $\{x | Ax=b \}$
   * every affine set can be expressed as solution set of system of linear equations
2. convex set
   * $x=\theta x_1 + (1-\theta) x_2, 0\leq \theta\leq 1$
3. convex combination
   * convex combination $x=\theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k, \theta_1+\cdots +\theta_k=1,\theta_i\geq 0$
   * convex hull $\mathrm{conv} S$: set of all convex combinations of points in $S$
4. convex cone
   * conic (nonnegative) combination: $x=\theta_1 x_1 + \theta_2 x_2, \theta_1\geq 0, \theta_2\geq 0$
   * convex cone: set that contains all conic combinations of points in the set
5. hyperplane and halfspace
   * hyperplane $\{ x | a^Tx=b \}, a\ne 0$, affine and convex
   * halfspace $\{ x | a^Tx\leq b \}, a\ne 0$, convex
   * $a$ is the normal vector
6. (Euclidean) ball with center $x_c$ and radius $r$: $B(x_c,r)=\{ x | \; ||x-x_c||_2\leq r \}= \{ x_c+ru | \; ||u||_2\leq 1 \}$
7. ellipsoid
   * $\{ x | (x-x_c)^TP^{-1}(x-x_c) \leq 1 \}$, unique representation
   * symmetric positive definite $P\in S^n_{++}$
   * $\{ x_c + Au | \; ||u||_2\leq 1 \}$ with $A$ square and nonsingular, non-unique
8. norm: $|| \cdot ||$ satisfy
   * $|| x|| \geq 0$; $||x||=0$ if and only if $x=0$
   * $|$tx$|=|t|\; ||x||$ for $t\in \mathbb{R}$
   * $||x+y||\leq ||x|| + || y||$
9. norm ball with center $x_c$ and radius $r$
   * $\{ x | \; ||x-x_c||\leq r \}$
   * convex
10. norm cone
    * $\{ (x,t) |\; ||x||\leq t \}$
    * convex
11. polyhedra
    * solution set of finitely many linear inequalities and equalities $Ax\preccurlyeq b; Cx=d$, $A\in \mathbb{R}^{m\times n}, C\in \mathbb{R}^{p\times n}$
    * intersection of finite number of halfspaces and hyperplanes
    * $\preccurlyeq$ componentwise inequality
12. positive semidefinite cone
    * $S^n$: set of symmetric $n\times n$ matrices
    * $S^n_+=\{ X\in S^n | X\succcurlyeq 0 \}$: positive semidefinite $n\times n$ matrices
    * $S^n_{++}=\{ X\in S^n | X\succ 0 \}$: positive definite $n\times n$ matrices
13. simple convex sets
    * hyperplane
    * halfspace
    * norm ball
    * etc.
14. operations that preserve convexity
    * intersection
    * affine function
    * perspective function $P(x,t)=x/t,$ $\mathrm{dom} P=\{(x,t) | t>0\}$, both forward and reverse mapping
    * linear-fractional function $f(x)=\frac{Ax+b}{c^Tx+d}$ $\mathrm{dom} f={x | c^Tx+d>0}$
15. affine function
    * $f(x)=Ax+b,A\in\mathbb{R}^{m\times n}, b\in \mathbb{R}^m$, both forward mapping and reverse mapping
    * scaling, translation, projection
    * solution set of linear matrix inequality $\{ x | x_1A_1+\cdots x_mA_m \preccurlyeq B \}$ with $A_i,B \in S^p$
    * hyperbolic cone $\{ x | x^TPx \leq (c^Tx)^2; c^Tx \geq 0\}$ with $P\in S^n_+$
16. a convex cone $K\subseteq \mathbb{R}^n$ is a proper cone if
    * closed: contains its boundary
    * solid: nonempty interior (a ray is not solid)
    * pointed: contains no line (line is not pointed)
17. generalized inequalities defined by a proper cone $K$
    * $x\preccurlyeq_K y \Leftrightarrow y-x\in K$
    * $x\prec_K y \Leftrightarrow y-x \in \mathrm{int} K$
    * example: componentwise inequality $K=\mathbb{R}_+^n$
    * example: matrix inequality $K=S_+^n$
    * partial ordering, incomparable
    * $x\in S$ is the **minimum** element of $S$ with respect to $\preccurlyeq_K$ if $y\in S \Rightarrow x\preccurlyeq_K y$
    * $x\in S$ is a **minimal** element of $S$ with respect to $\preccurlyeq_K$ if $y\in S, y\preccurlyeq_K x \Rightarrow y=x$
18. separating hyperplane theorem
    * if $C$ and $D$ are disjoint convex sets, the there exists $a\ne 0, b$ such that $a^Tx\leq b$ for $x\in C$ and $a^Tx\geq b$ for $x\in D$
    * strict separation requires additional assumptions: e.g. $C$ is closed, $D$ is singleton
19. supporting hyperplane theorem
    * supporting hyperplane: to set $C$ at boundary point $x_0$: $\{x | a^Tx=a^Tx_0\}$ where $a\ne 0$ and $a^Tx\leq a^T x_0$ for all $x\in C$
    * supporting hyperplane theorem: if $C$ is convex, then there exists a supporting hyperplane at every boundary point of $C$
20. dual cone of a cone $K$
    * $K^*=\{y | y^T x \geq 0 \forall x\in K\}$
    * example: $K=\mathbb{R}_+^n=K^*$: self-dual
    * example: $K=S_+^n=K^*$, the inner product of two matrices is defined as $tr(XY)$, self-dual
    * example: $K=\{(x,t) | \; ||x||_2\leq t\}=K^*$, self-dual
    * example: $K=\{(x,t) | \; ||x||_1\leq t\}$, $K^*=\{(x,t) | \; ||x||_\infty\leq t\}$
    * dual cones of proper cones are proper. the generalized inequalities $y\succcurlyeq_{K^*}0 \Leftrightarrow y^Tx\geq 0 \forall x\succcurlyeq_K 0$
21. minimum and minimal elements via dual inequalities
    * minimum element w.r.t. $\preccurlyeq_K$: $x$ is minimum element of $S$ iff for all $\lambda \succ_{K^*} 0$, $x$ is the unique minimizer of $\lambda^Tz$ over $S$
    * minimal element w.r.t. $\preccurlyeq_K$: if $x$ minimizes $\lambda^Tz$ over $S$ for some $\lambda\succ_{K^*} 0$, then $x$ is minimal
    * minimal element w.r.t. $\preccurlyeq_K$: if x is a minimal element of a convex set $S$, then there exists a nonzero $\lambda\succcurlyeq_{K^*}0$ such that $x$ minimizes $\lambda^Tz$ over $S$
22. Pareto optimal

## chap2 convex function

1. convex function
   * $f: R^n\to R$ is convex if $\mathrm{dom} f$ is a convex set and $f(\theta x+(1-\theta) y)\leq \theta f(x) + (1-\theta) f(y)$ for all $x,y \in \mathrm{dom} f, 0\leq \theta\leq 1$
   * chord
   * $f$ is concave if $-f$ is convex
   * strictly convex defintiion: ....
2. convex example
   * affine $ax+b$
   * exponential $e^{ax}$
   * powers $x^\alpha$ on $R_{++}$, $\alpha\geq 1$ or $\alpha \leq 0$
   * powers of absolute vlaue $|x|^p$ for $p\geq 1$
   * negative entropy $x \log(x)$ on $R_{++}$
   * all norm: spectral (maximum singular value) norm (for matrix)
   * quadratic-over-linear $f(x,y)=x^2/y$ for $y>0$
   * log-sum-exp $f(x)=\log(\sum_{k=1}^n e^{x_k})$
   * geometric mean $f(x)=(\prod_k^n{x_k})^{1/n}$ on $R^n_{++}$
3. concave
   * affine $ax+b$
   * powers $x^\alpha$ on $R_{++}$ for $0\leq \alpha \leq 1$
   * logarithm $\log(x)$ on $R_{++}$
   * $\log(\mathrm{Det}(X))$ for $X\in S^n_{++}$
4. extended-value extension
5. first-order condition
   * differentiable $f$ with convex domain is convex iff $f(y)\geq f(x) + (y-x)^T\nabla f(x)$ for all $x,y\in \mathrm{dom}f$
   * first-order approximation of $f$ is global underestimator
6. second-order condition: $f$ is convex if and only if $\nabla^2f(x)\succcurlyeq 0 \forall x\in \mathrm{dom} f$
7. $\alpha$-sublevel set of $f: \mathbb{R}^n\to\mathbb{R}$
   * $C_\alpha={x\in \mathrm{dom}f | f(x)\leq \alpha}$
   * sublevel sets of convex functions are convex (converse is false, non-convex function can have convex sublevel set)
8. Epigraph of $f: \mathbb{R}^n\to\mathbb{R}$
   * $\mathrm{epi} f=\{(x,t)\in\mathbb{R}^{n+1} | x\in \mathrm{dom} f, f(x)\leq t\}$
   * $f$ is convex iff $\mathrm{epi} f$ is a convex set
9. Jensen's inequality: random variables and expectation
10. operations that preserve convexity
    * nonnegative weighted sum
    * composition with affine function
    * pointwise maximum and supremum
    * composition: convex nondecreasing function of a convex function is convex, convex nonincreasing function of a concave function is a convex function
    * minimization
    * perspective
11. Schur complement
12. conjugate function
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
