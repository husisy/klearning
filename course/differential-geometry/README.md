# differential geometry

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
