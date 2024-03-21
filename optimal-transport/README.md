# optimal transport

1. link
   * [youtube-link](https://youtube.com/playlist?list=PLJ6garKOlK2qKVhRm6UwvcQ46wK-ciHbl&si=MeJXJuGHf6xwQQmq)
2. Monge problem
   * $\min\int |x-T(x)|f(x) dx$
     * transport plan: $T(x)$
     * density: $f(x)$
   * $\min \int c(x,T(x))f(x) dx$
     * cost: $c(x,T(x))$
3. source measure $\mu$, target measure $\nu$, source support $X$, target support $Y$
   * global conservation: $\mu(X) = \nu(Y)$
   * local conservation: for any measurable set $A\subset Y$, $\mu(T^{-1}(A)) = \nu(A)$
4. $\mu(T^{-1}(A))$: pushforward measure of $\mu$ by $T$
5. Monge formulation of OT
   * $\min \int c(x,T(x))d\mu(x)$
   * $T_{\# \mu} = \nu$
   * not allow to split mass
   * example:
     * book moving problem
6. kantorovich formulation
   * source measure $\mu$, target measure $\nu$, source support $X$, target support $Y$
   * product measure $\pi$ on $X\times Y$
   * $\pi(A, Y) = \mu(A)$, $\pi(X, B) = \nu(B)$
   * $\mu$ is the marginal of $\pi$ on $X$, $\nu$ is the marginal of $\pi$ on $Y$
   * $\inf \int c(x,y)d\pi(x,y)$, $\pi \in \Pi(\mu,\nu)$
   * example
     * discrete OT
     * continuous OT
     * semi-discrete OT
