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
