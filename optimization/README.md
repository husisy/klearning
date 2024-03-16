# optimization

1. link
   * [wiki-link](https://en.wikipedia.org/wiki/Arkadi_Nemirovski), [homepage](https://www2.isye.gatech.edu/~nemirovs/), Arkadi Nemirovski
   * [homepage](https://optimization.cbe.cornell.edu/) Cornell University computational optimization open textbook

## Riemann optimization

1. link
   * [website](https://www.nicolasboumal.net/book/) An introduction to optimization on smooth manifolds (Nicolas2023book)
2. assumption in optimization (Nicolas2023book,page57)
   * globally lower-bounded
   * at each iteration, sufficient decrease is achieved: there exists a constant $c>0$ such that for all $k$, $f(x_k)-f(x_{k+1})\geq c||\mathrm{grad}\,f(x_k) ||$
   * proposition: with the above assumptions, the sequence $\{x_k\}$ converges to a critical point of $f$

## manifold optimization

manifold example

1. SO group
2. special Euclidean group
3. normalized essential manifold
4. noncompact Stiefel manifold of full rank $n\times r$ matrix: $\{x\in\mathbb{R}^{n\times r}: \mathrm{rank}(x)=r\}$ for $r\leq n$
5. (orthogonal, compact) Stiefel manifold $\mathrm{St}(n,r)=\{x\in\mathbb{R}^{n\times r}:x^Tx=I_r\}$
6. generalized Stiefel manifold $\{x\in\mathbb{R}^{n\times r}:x^TBx=I_r\}$ for a symmetric positive definite matrix $B\in\mathbb{R}^{n\times n}$
7. oblique manifold: $\mathcal{OB}=\{x\in\mathbb{R}^{n\times r}:\mathrm{diag}(xx^T)=1\}$
8. flag manifold
9. misc
   * collection $X=\{(x,|x|):x\in\mathbb{R}\}$, then $(X,\mathcal{A})$ is a smooth manifold with $\mathcal{A}=\{(X,\phi)\}$ and $\phi(x)=x_0:X\to\mathbb{R}$, but it's not a submanifold of $\mathbb{R}^2$
   * [exchange-link](https://math.stackexchange.com/a/2181527) figure-eight curve

manifold concept

1. concept
   * immersed submanifold
   * embedded submanifold (regular submanifold)
   * $\phi$-coordinate slice
2. mapping $F:\mathcal{M}_1\to\mathcal{M}_2$, $\mathrm{dim}(\mathcal{M}_1)=d_1$, $\mathrm{dim}(\mathcal{M}_2)=d_2$
   * (def) coordinate representation $\hat{F}=F\circ\phi_1^{-1}\circ\phi_2$
   * (def) $F$ is differentiable (smooth): $\hat{F}$ is differentiable
   * (def) $F$ is a diffeomorphism: bijective differentiable function with differentiable inverse
   * (def) rank: let $x\in\mathcal{M}_1$, the dimension of the range $D\hat{F}(\phi_1(x))[\cdot]:\mathcal{R}^{d_1}\to\mathcal{R}^{d_2}$ is called the mapping rank of $F$ at $x$
   * (def) immersion: rank of $F$ is $d_1$ at all points
   * (def) submersion rank of $F$ is $d_2$ at all points
   * (def) regular value: let $y\in\mathcal{M}_2$, $y$ is called a regular value if rank of $F$ is $d_2$ at all points $x\in F^{-1}(y)$
3. quotient manifolds
   * equivalence relation
   * $\mathcal{M}/\sim=\{[x]:x\in\mathcal{M}\}$
   * natural projection (canonical projection) $\pi:\mathcal{M}\to\mathcal{M}/\sim$
4. tangent vector
   * $\mathfrak{F}_x(\mathcal{M})$: set of smooth real-valued functions defined on $\mathcal{M}$ in a neighborhood of $x$
   * tangent vector $\xi_x$: a mapping from $\mathfrak{F}_x(\mathcal{M})$ to $\mathbb{R}$, $\xi_x(f)=\frac{df(\gamma(t))}{dt}|_{t=0}$ for all $f\in\mathfrak{F}_x(\mathcal{M})$ with a curve $\gamma(0)=x$
   * tangent space $T_x\mathcal{M}$: set of all tangent vectors at $x$, a vector space
   * tangent bundle $T\mathcal{M}=\bigcup_{x\in\mathcal{M}}\{x\}\times T_x\mathcal{M}$, a manifold
   * vector field $X:\mathcal{M}\to T\mathcal{M}$, $X(x)\in T_x\mathcal{M}$ for all $x\in\mathcal{M}$
   * every vector field defines a derivation. every derivation can be realized as a vector field
5. misc
   * all functions are assumed to be smooth unless otherwise stated

pass

1. link
   * [book-link](https://press.princeton.edu/absil) optimization algorithm on matrix manifold
