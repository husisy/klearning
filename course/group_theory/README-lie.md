# lie group and lie algebra

1. theorem: let $G$ be a topologically closed subgroup of $GL(n,\mathbb{R})$, define $g=\{X\in gl(n,\mathbb{R}): e^{tX}\in G \forall t\in \mathbb{R}\}$
   * $g$ is a vector space
   * if $x,y\in g$, then $[x,y]\in g$
   * $g$ is parallel to $G$ at $e$
   * $\mathrm{exp}: g\to G$ is locally invertible
2. (most) Lie group: topologically closed subgroup of $GL(n,\mathbb{R})$
   * Lie group but not topologically closed subgroup of $GL(n,\mathbb{R})$
   * topological closure
   * matrix Lie group
3. concept
   * [wiki-link](https://en.wikipedia.org/wiki/Weierstrass_M-test) Weierstrass M-test
   * matrix norm
   * smooth homomorphism, Lie algebra homomorphism
4. [stackexchange-link](https://math.stackexchange.com/a/1592257) if $G$ is a real finite-dimensional Lie group with Lie algebra $\mathfrak{g}$, then the following are equivalent
   * exp is injective
   * exp is bijective
   * exp is a real analytic diffeomorphism
   * $G$ is solvable, simply connected, and $\mathfrak{g}$ does not admit $e$ as subalgebra of a quotient
   * $G$ is solvable, simply connected, and $\mathfrak{g}$ does not admit $e$ or $\tilde{e}$ as subalgebra
   * $G$ has no closed subgroup isomorphic to either the circle $\mathbb{R}/\mathbb{Z}$, the universal covering $\tilde{\mathrm{SL}_2(\mathbb{R})}$, $E$ or $\tilde{E}$

## Lie algebra

example

1. $gl(n,\mathbb{F})$ general linear Lie algebra
   * $[A,B]=AB-BA$
   * center: $Z(gl(n,\mathbb{F}))=\{\lambda I: \lambda\in\mathbb{F}\}$
2. $sl(n,\mathbb{F})$ special linear Lie algebra, trace zero subalgebra of $gl(n,\mathbb{F})$
   * center: $Z(sl(n,\mathbb{F}))=\{0\}$ [stackexchange-link](https://math.stackexchange.com/q/466361)
3. derivation: given an algebra $A$, a linear map $L: A\to A$ is called a drivation if $D(ab)=D(a)b+aD(b)$
   * the set of derivation $\mathrm{Der}(A)$ is a Lie algebra with $[D_1,D_2]=D_1D_2-D_2D_1$
4. Witt algebra [wiki-link](https://en.wikipedia.org/wiki/Witt_algebra)
   * Laurent polynomial [wiki-link](https://en.wikipedia.org/wiki/Laurent_polynomial)
   * witt: $\mathrm{Der}(\mathbb{C}[z,z^{-1}])=\mathrm{span}\{l_n:n\in\mathbb{Z}\},l_n=-z^{n+1}\frac{d}{dz}$
   * $[l_m,l_n]=(m-n)l_{m+n}$
5. $\mathbb{R}^3$ with cross product
6. tangent space to Lie group at identity $\mathfrak{g}=\mathrm{Te}(G)$
7. $b(n,\mathcal{F})$ upper triangular matrices (diagonal could be nonzero)
8. $n(n,\mathcal{F})$ strictly upper triangular matrices (diagonal is zero), $n$ for nilpotent matrices
9. $\mathrm{span}\{l_{-1},l_0,l_1\}\subset \mathrm{witt }$
10. $\mathbb{C}$: one-dimensional Lie algebra

pass

1. link
   * [youtube/mathmajor](https://youtu.be/XgTErplKcKU?si=e_wtfZr2jiSOQmPl)
2. concept
   * non-associative algebra
3. definition: field $\mathbb{F}$, a Lie algebra $L$ is a vector space together with a bilinear map (Lie bracket)
   * $[\bullet,\bullet]: L\times L\to L$
   * alternatiing: $[x,x]=0$
   * Jacobi identity: $[x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0$
   * if characteristic $\mathrm{char}(\mathbb{F})\ne 2$, then alternating identity is equalvalent to $[x,y]=-[y,x]$
4. Lie subalgebra: $L_1\subset L$ is a Lie subalgebra if $[x,y]\in L_1,\forall x,y\in L_1$
5. ideal: $I\subset L$ is an ideal if $[x,y]\in I,\forall x\in I, y\in L$
   * example
     * $L$ is an ideal of itself
     * $sl(n,\mathbb{F})$ is an ideal of $gl(n,\mathbb{F})$
6. center of $L$: $Z(L)=\{x\in L: [x,y]=0,\forall y\in L\}$
   * $Z(L)$ is an ideal
7. quotient Lie algebra: $L/I=\{x+I: x\in L\}$, $[x+I,y+I]=[x,y]+I$
   * $L/I$ is a Lie algebra iff $I$ is an ideal
   * quotient vector space is always a vector space [wiki-link](https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra))
8. Lee algebra homomorphism
9. ideal $I,J\subset L$
   * $I\cap J$ is an ideal
   * $I+J=\{ i+j: i\in I,j\in J \}$ is an ideal
   * $[I,J]=\mathrm{span}\{[x,y]: x\in I, y\in J\}$ is an ideal
10. commutator subalgebra (): $[L,L]=\mathrm{span}\{[x,y]: x,y\in L\}$
    * example: $[gl(2,\mathbb{F}),gl(2,\mathbb{F}))=sl(2,\mathbb{F})$
    * solvable lie algebra [wiki-link](https://en.wikipedia.org/wiki/Solvable_Lie_algebra)
11. Lie algebra homomorphism: $f: L_1\to L_2$ is a Lie algebra homomorphism if $f([x,y])=[f(x),f(y)]$
    * kernel: $\mathrm{ker}(f)=\{x\in L_1: f(x)=0\}$ is an ideal
    * image: $\mathrm{im}(f)=\{f(x): x\in L_1\}$ is a Lie subalgebra
    * isomorphism: $f$ is an isomorphism if $f$ is bijective
    * first isomorphism theorem: $L_1/\mathrm{ker}(f)\cong \mathrm{im}(f)$
    * $gl(2,\mathbb{C})\cong sl(2,\mathbb{C})\oplus \mathbb{C}$
12. second isomorphism theorem: $I,J\subset L$ are ideals, then $I/(I\cap J)\cong (I+J)/J$
13. third isomorphism theorem: $I,J\subset L$ are ideals and $I\subset J$, then $(L/I)/(J/I)\cong L/J$
14. all 1-dimensional Lie algebra is abelian (commutative) $[x,y]=0,\forall x,y\in L$
15. 2-dimensional Lie algebra
    * abelian
    * non-abelian: find a basis s.t. $[x,y]=x$
16. 3-dimensional Lie algebra $L$
    * $\dim([L,L])=0$ iff $L$ is abelian
    * $\dim([L,L])=1, [L,L]\subset Z(L)$, then $L=\mathrm{span}\{x,y,z\},[x,y]=z$
      * Heisenberg Lie algebra
17. given a Lie algebra $L$ and an ideal $I\subset L$, then $L/I$ is abelian iff $[L,L]\subset I$
