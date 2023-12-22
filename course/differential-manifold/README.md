# differential manifold

1. link
   * [doi-link](https://doi.org/10.1007/978-1-4419-9982-5) Introduction to Smooth Manifolds, John, M. Lee

manifold examples

1. Euclidean space
2. lie groups
3. compact matrix lie group
4. sphere
5. hyperbolic space
6. Stiefel manifold
7. symmetric positive definite matrices

栗子

1. n-sphere $S^n=\{x\in\mathbb{R}^{n+1}:\|x\|=1\}$
   * tangent space $T_xS^n=\{v\in\mathbb{R}^{n+1}:v\cdot x=0\}$
   * embedded submanifold of $\mathbb{R}^{n+1}$
   * closed, compact, connected, simply connected
   * retraction
     * $r_x(tv)=\frac{x+tv}{\sqrt{1+t^2|v|^2}}$
     * great circle, geodesics: $r_x(tv)=\cos(t|v|)x+\sin(t|v|)v/|v|$
2. rank-1 2-by-2 Symmetric matrix $\mathrm{Sym}(2)_1=\{x:x\ne 0,x_{11}x_{22}=x_{12}x_{21},x_{12}=x_{21}\}$
   * embedded submanifold of 2-by-2 symmetric matrices
   * (in the above embedded manifold) not closed, not open, not connected
3. Oblique manifold $\mathrm{OB}(d,k)=(S^{d-1})^{\otimes k}$
4. the relative interior of the simplex $\Delta_+^{d-1}=\{x\in\mathbb{R}^d:x_i>0,\sum_ix_i=1\}$
   * Fisher-Rao metric: $g_x(v,w)=\sum_{i=1}^d\frac{v_iw_i}{x_i}$
   * [arxiv-link](https://arxiv.org/abs/1907.06628)
   * [stackexchange-link](https://math.stackexchange.com/q/4187889)

pass

1. left-translation

concept

1. immersion, submersion
2. tangent vector, tangent space
3. open set
4. level set
5. connections
   * Levi-Civita connection: torsion-free, compatible
   * each Riemannian metric generate a unique Leve-Civita connection
   * Christoffel symbols [wiki-link](https://en.wikipedia.org/wiki/Christoffel_symbols)
6. parallel transport, parallel vector field, geodesic
7. stratified space

## youtube-course

1. link
   * [youtube-link](https://youtu.be/AkVMWhrJxs0?si=j5-gYhGioXUBMkW_)
   * [pdf-link](https://www.math.uni-hamburg.de/home/lindemann/material/dg_lindemann_ss2020_WIP25.pdf)

another-youtube

1. link
   * youtube-link
   * [pdf-link](http://www2.ing.unipi.it/griff/files/dC.pdf)
   * [youtube-link](https://youtu.be/En6zdtX4Dls?si=gK4UdbAt25Lbgd0n)
2. concept
   * curve, non-injective
   * tangent vector $t(s)=\alpha'(s)$
   * normal vector $n(s)k(s)=\alpha''(s)$: $n(s)$ is of unit length
   * binormal vector $b(s)=t(s)\times n(s)$
   * planar curve
   * rigid motion (translation, rotation)
   * one-dimensional object
   * self-intersection. $(t^3-4t,t^3-4)$
   * corner, $(t^2,t^3)$
   * $\left(\frac{3t}{1+t^3},\frac{3t^2}{1+t^3}\right), t\in(-1,\infty)$, $3xy=x^3+y^3$
   * singular point: zero tangent vector
   * regular: no singular point
   * arc length: non differentiable on singular point
3. curve parametrized by arc length $\alpha(s)$
   * tangent vector $t(s)=\alpha'(s)$: unit length
   * curvature $\kappa(s)=\|\alpha''(s)\|$
   * normal vector $n(s)=\frac{\alpha''(s)}{\kappa(s)}$
     * $n(s)\cdot t(s)=0$
   * binormal vector $b(s)=t(s)\times n(s)$
     * unit length
     * $b'(s) \times n(s)=0$
   * torsion $\tau(s): b'(s)=\tau(s)n(s)$
      * can be negative
   * invariant under a change of orientation: $k(s),\tau(s),n(s)$
   * invariant under rigid motion: $k(s),\tau(s),s$
4. Frenet trihedron formula
   * $t'=kn$
   * $b'=\tau n$
   * $n'=-kt-\tau b$
   * osculating plane: plane spanned by $t(s)$ and $n(s)$
   * rectifying plane: plane spanned by $t(s)$ and $b(s)$
   * normal plane: plane spanned by $n(s)$ and $b(s)$
5. fundamental theorem of the local theory of curves
6. global property
   * isoperimetric inequality
   * four vertex theorem
   * Cauchy-Crofton formula

## differential manifold

example

1. matrix manifold: orthonormal, fixed rank, positive definite
2. linear subspaces
3. open subsets of manifold
4. product of manifold

pass

1. link
   * [youtube-link](https://youtu.be/mcC8fvqKZG0?si=3mZW37INvpvl1JJx)
   * [website](https://www.ocf.berkeley.edu/~pengzhou/courses/math214/home)
   * [wiki-link](https://en.wikipedia.org/wiki/Diffeomorphism) Diffeomorphism
2. topological space
   * open set
   * basis
3. concept
   * chart, transition function
   * atlas
   * integral curve
   * tangent vector space, coordinate basis
   * pushback, pullback
4. differential form
   * 0-form: function $\Omega^0(\mathbb{R}^d)=C^\infty(\mathbb{R}^d)$
   * exterior derivative: $d: \Omega^q\to \Omega^{q+1}$
   * 1-form: $C^\infty(M)$ module (vector space over ring)
   * wedge product: $\wedge: \Omega^p\times \Omega^q\to \Omega^{p+q}$, anti-symmetric
5. diffeomorphism

## Riemann optimization

1. link
   * [youtube-link](https://www.youtube.com/live/lK62DwSIjXA?si=Y2OxrGdlyXNqVr9A) An Introduction to Optimization on Smooth Manifolds -- Nicolas Boumal
   * [wiki-link](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions) Karush–Kuhn–Tucker conditions
2. concept
   * search space
   * cost function
   * subset of search space with minimal cost
   * unconstraint optimization if search space is $\mathbb{R}^n$
   * unsmooth: kinds, boundaries
   * smooth example: plane, sphere, torus, hyperboloid
   * if manifold endowed with inner product (Riemannian manifold), then we can talk about gradient, Hessian
   * quotient set
   * quotient manifold
   * isometry between two Riemann manifold
   * smooth map on manifold
   * retraction, metric projection retraction
   * Cartan-Hadamard manifolds
   * geodesic convexity
3. Whitney’s embedding theorems: any smooth manifold can be embedded in a linear space
4. products of manifolds are manifolds
5. $\mathbb{R}_*^n$ (Euclidean space without origin) is a open submanifold of $\mathbb{R}^n$
6. matrix norm: Frobenius norm, induced by the HS inner product
7. manifold
   * oblique manifold $\mathrm{OB}(d,n)=(S^{d-1})^{\otimes n}=\{X\in\mathbb{R}^{d\times n}:\mathrm{diag}(X^TX)=1\}$
   * Stiefel manifold $\mathrm{St}(d,n)=\{X\in\mathbb{R}^{d\times n}:X^TX=I\}$
   * Orthogonal group $\mathrm{O}(d)=\{X\in\mathbb{R}^{d\times d}:X^TX=I\}$
   * Grassmann manifold $\mathrm{Gr}(d,k)=\mathrm{St}(d,k)/\mathrm{O}(k)$: subspaces of dimension $k$ in $\mathbb{R}^d$
   * special orthogonal group $\mathrm{SO}(d)=\{X\in\mathrm{O}(d):\det(X)=1\}$
8. invariant: sectional curvature, Ricci curvature, and scalar curvature

## course-xxx

smooth manifold example

1. Klein bottle: $\dim=2$, non-orientable [wiki-link](https://en.wikipedia.org/wiki/Klein_bottle)
2. Euclidean space $\mathbb{R}^n$
   * contains one chart $(\mathbb{R}^n,\mathrm{id})$
3. n-sphere $\mathbb{S}^n$
   * stereographic projector: two charts $(\mathbb{S}^n\setminus\{p_+\},\phi_+)$ and $(\mathbb{S}^n\setminus\{p_-\},\phi_-)$
     * chart transition map $x=\frac{y}{\lVert y\rVert^2_2}$
   * Spherical coordinates (see wiki)
   * polar coordinates (see wiki)
4. torus $\mathbb{T}^n$
5. real projective $n$-space $\mathbb{R}P^n=\{[x]:x\in\mathbb{R}^n\setminus\{0\}\}$ where $[x]=\{tx:t\in\mathbb{R}\}$ (equivalent class)
   * $(n+1)$ charts
   * compact
6. graph of smooth function $f:U\to\mathbb{R}$, $U\in\mathbb{R}^n$ is open, $\mathrm{graph}(f)=\{(x,f(x)):x\in U\}$
   * one chart $(\mathrm{graph}(f),\phi)$ where $\phi(x,f(x))=x$
7. any open subset of a smooth manifold is a smooth manifold
8. Boy's surface [wiki-link](https://en.wikipedia.org/wiki/Boy%27s_surface)

notation

1. $A$ index set
2. $\mathscr{A}$ atlas
3. $\mathcal{M}$ manifold
4. $(\cdot_i)_{i\in A}$ collection of objects indexed by $i\in A$, sometimes written as $(\cdot_i)_i$ or $(\cdot_i)$
5. $C^k$, $C^\infty$: $k$-times differentiable, infinitely differentiable (smooth)
6. diffeomorphism (isomorphism of smooth manifold) $\cong$

[youtube-link1](https://youtu.be/0OauaSkYD44?si=ULkSWinwwluAv7pW) introduction of manifold

1. topological manifold $(\mathcal{M},\mathscr{A})$
   * Hausdorff
   * second countablility
   * locally Euclidean: $\forall p\in\mathcal{M}$, exits open neighborhood $U_p\in\mathcal{M}$ and homeomorphism $\phi_p:U_p\to\phi(U_p)\subset\mathbb{R}^n$
     * chart map $\phi_p$
     * chart domain $U_p$
     * chart $(\phi_p,U_p)$
2. chart transition map: for two charts $(p,\phi_p)$ and $(q,\phi_q)$
   * $\phi_q\circ\phi_p^{-1}:\phi_p(U_p\cap U_q)\to\phi_q(U_p\cap U_q)$
   * homeomorphism (composition of two homeomorphism): continuity $C^0$, bijective, inverse continuous
   * every pair of charts are $C^0$ compatible
   * two charts are $C^k$ compatible: their transition maps are $C^k$ continuous in both directions
   * chart compatiblility is not transitive
   * coordinate function: the $i$-th component of $\phi_p$
3. atlas (smooth structure)
   * atlas def: $\mathscr{A}=\{(U_x,\phi_x):x\in A\}$ such that $\cup_{x\in A} U_x=\mathcal{M}$
   * example $\mathbb{S}^1$, $U_1=(-\pi,\pi)$, $U_2=(0,2\pi)$
   * $C^k$ compatable atlas: $\forall x,y\in A$, $(U_x,\phi_x)$ and $(U_y,\phi_y)$ are $C^k$ compatible (at least $C^0$ compatible)
   * equivalent atlas (not equivalence relation): $\mathscr{A}\sim\mathcal{B}$: $\mathscr{A}\cup\mathcal{B}$ is an atlas
   * maximal comptaible atlas $\mathscr{A}$:if for all $\forall \mathcal{B}\sim\mathscr{A}$, $\mathcal{B}\subset \mathscr{A}$ (partial ordered)
     * [wiki-link](https://en.wikipedia.org/wiki/Zorn%27s_lemma) Zorn's lemma (partially ordered set)
     * every atlas is contained in a maximal atlas
     * [stackexchange-link](https://math.stackexchange.com/a/2930474) two atlases are compatible if and only if their associated maximal atlases are equal
     * every maximal atlas is contains a countable atlas
   * maximal $C^k$ compatable atlas $\mathscr{A}_{\max}^k$
4. $n$-dimensional smooth manifold: $n$-dimensional topological manifold with a maximal $C^\infty$ compatible atlas
5. tangent space basis
   * chart induced basis
6. $m$-dimensional smooth submanifold $\mathcal{M}\subset \mathbb{R}^n$ ($m<n$)
   * for all $p\in \mathcal{M}$, exists an open neighborhood $p\in U\subseteq\mathbb{R}^n$ and smooth map $f:\mathbb{R}^n\to\mathbb{R}^{n-m}$ with Jocabian matrix of rank $(n-m)$ and $M\cap U=\{x\in U:f(x)=0\}$
   * lemma: can be locally written as graph of smooth function $g: V\to \mathbb{R}^{n-m}$ with $V\in\mathbb{R}^m$
   * chart: $F|_{U\cap \mathcal{M}}: (x^1,\cdots,x^n)\mapsto (x^1,\cdots,x^m,0,\cdots,0)$ (possibly reordering coordinates)
7. product of smooth manifold
   * the product of atlases is in general not maximal
8. diffeomorphism, let $M,N$ be two smooth manifold
   * a map $f:\mathcal{M}\to\mathcal{N}$ is call smooth, if for all chart $(\phi,U)\in M,(\psi,V)\in N$, $\psi\circ f\circ\phi^{-1}: \phi(U\cap f^{-1}(V))\to\psi(V)$ is smooth
   * a smooth map $f:\mathcal{M}\to\mathcal{N}$ is a diffeomorphism if it is bijective and its inverse is smooth
   * the set of diffemorphisms on $n$-dimensional smooth manifold $M$ ($n\geq 1$), $\mathrm{Diff}(M)$, forms an infinite dimensional Lie group
9. vector space $C^\infty(M)$ of smooth function on smooth manifold $M$, $f:M\to\mathbb{R}$
   * $C^\infty(M)$ is a commutative ring with unit the constant function $f=1$
   * restriction map
   * local smooth function $C^\infty(U)$: $f|_U$ is smooth for all chart $(\phi,U)$ with $U\subset M$
   * example: coordinate function

[youtube-link](https://youtu.be/AkVMWhrJxs0?si=ByYGcC3sxpcctFIK) differential geometry

lecture 1

1. [wiki-link](https://en.wikipedia.org/wiki/Inverse_function_theorem) inverse function theorem: let $U\in\mathbb{R}^n$ be open, $F:U\to\mathbb{R}^n$ be smooth, and assume that Jacobian matrix $dF|_p$ is invertible for some $p\in U$, then there exists open neighbors $p\in V\subseteq \mathbb{R}^n$ such that $F|_V:V\to F(V)$ is a diffeomorphism
   * not necessary to be global diffeomorphism, e.g. $f(x)=x^2$
   * other version: analytic map, holomorphic function, Frechet-differentiable maps between Banach spaces, smooth map between smooth function
2. implicit function theorem: let $F:\mathbb{R}^n\times \mathbb{R}^m\to\mathbb{R}^m, (x,y)\mapsto f(x,y)$ be smooth, $f(p)=0$ for $p=(x_0,y_0)$ and assume that the Jacobian matrix of $f$ with respect to $y$ at $p$ $d_yf|_p$ is invertible. Then exists open neighborhoods $x_0\in U\subseteq \mathbb{R}^n$ and $y_0\in V\subseteq \mathbb{R}^m$ such that a unique smooth map $g:U\to V$ satisfying $f(x,y)=0 \leftrightarrow y=g(x)$ on $U\times V$, particularly $y_0=g(x_0)$
3. bump function (test function)
   * compactly embedded with non-empty interior
   * extend local smooth functions to globally defined smooth function
4. tangent vector at $p\in\mathbb{R}^n$
   * equivalence class of curves $\gamma:(-\epsilon,\epsilon)\to\mathbb{R}^n$ with $\gamma(0)=p$: $\gamma_1\sim\gamma_2$ if $\gamma_1'(0)=\gamma_2'(0)$
   * directional derivative
   * tangent space of $\mathbb{R}^n$ at $p$
   * tangent space: disjoint union of tangent space at each point: isomorphic to $\mathbb{R}^n\times\mathbb{R}^n$
5. tangent vector on smooth manifold $M$
   * a tangent vector $v$ at $p\in M$ is a linear map $v:C^\infty(M)\to\mathbb{R}$ fulfils the Leibniz rule $v(fg)=v(f)g(p)+f(p)v(g)$
