# Algebraic topology

notation

1. disk $D^n=\{x\in\mathbb{R}^n:\lVert x\rVert_2\leq 1 \}$
   * $D^0$: one point
2. sphere $S^n=\{x\in\mathbb{R}^{n+1}:\lVert x\rVert_2=1 \}=\partial D^{n+1}$
   * $S^0$: two points
   * $\chi(S^n)=1+(-1)^n$
   * $D^2\times S^1$: solid torus (solid)
   * $D^1 / S^0=S^1$
   * $D^2 / S^1 = S^2$
3. cylinder $S^1\times [0,1]$
4. moebius strip
5. Klein bottle
   * $\chi=1-2+1=0$
6. torus $T^n=S^1\times S^1\times \cdots\times S^1$, $n$ times
   * $\partial T^n=\emptyset$
   * $\chi(T^n)=0$
7. genus-$g$ surface
   * 1-holed torus: 4-sided 2-edge (2-loop) 1-vertex polygon
   * 2-holed torus: 8-sided 4-edge (4-loop) 1-vertex polygon
   * $g$-holed torus: $4g$-sided $2g$-edge ($2g$-loop) $1$-vertex polygon
   * $\chi=2-2g$
8. real projective space $\mathbb{R}P^n=S^n/\sim$, $\sim$ is the antipodal equivalence relation
   * $\mathbb{R}P^0$: one point
   * $\mathbb{R}P^1=S^1$: $\mathbb{R}P^0+D^1$
   * $\mathbb{R}P^2$: $\mathbb{R}P^1+D^2$ ??
   * $\mathbb{R}P^n=D^0+D^1+\cdots+D^n$
   * $\chi(\mathbb{R}P^n)=1$ if $n$ is even, $0$ if odd

pass

1. link
   * @book Algebraic topology, Allen Hatcher
2. cell complex (CW complex, closure finiteness week topology complex)
   * 0-skeleton $X^0$: a finite set of points
   * 1-skeleton $X^1$: a finite set of line segments $D^1$, attaching map $\varphi:\partial D^1 \to X^0$
   * 2-skeleton $X^2$: a finite set of disks $D^2$, attaching map $\varphi:\partial D^2 \to X^1$
3. Euler characteristic $\chi(X)=\sum_{i=0}^n(-1)^i\mathrm{rank}(H_i(X))$
4. boundary: $\partial (X\times Y)= (\partial X\times Y)\cup (X\times \partial Y)$
5. wedge
   * $X\vee Y$: $X\cup Y$ with a common point
   * example
     * $S^2/S^1=S^2\vee S^1$
6. deformation retract from space $X$ to subspace $A$, continuous family of maps $f_t:X\to X$ such that ($t\in[0,1]$)
   * $f_0=\mathrm{id}_X$
   * $f_1(X)=A$
   * $f_t|_A=\mathrm{id}_A$
7. homotopy is an equivalence relation
   * $f\simeq g$ if there exists a continuous map $H:X\times [0,1]\to Y$ such that $H(x,0)=f(x)$ and $H(x,1)=g(x)$
   * relative homotopy: $f\simeq g$ through maps that fix $A$
8. homotopy equivalence
9. the fundamental group, topological space $X$, base point $x_0\in X$
   * $\pi_1(X,x_0)$: set of homotopy classes of loops in $X$ based at $x_0$
   * binary operation: loop concatenation $[f][f']=[f\circ f']$
10. Brouwer fixed-point theorem
    * every continuous map $f:D^n\to D^n$ has a fixed point
11. Borsuk–Ulam theorem [wiki-link](https://en.wikipedia.org/wiki/Borsuk%E2%80%93Ulam_theorem)
