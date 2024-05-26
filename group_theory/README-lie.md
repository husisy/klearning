# lie group and lie algebra

[wiki-link](https://en.wikipedia.org/wiki/Weierstrass_M-test) Weierstrass M-test

## matrix Lie group and matrix Lie algebra

栗子

1. [wiki-link](https://en.wikipedia.org/wiki/General_linear_group) general linear group $GL(n;k)$ with $k=\mathbb{R},\mathbb{C}$: invertible matrix
   * nonzero real number $\mathbb{R}^*\simeq GL(1;R)$
   * nozero complex number $\mathbb{C}^*\simeq GL(1;C)$
   * unit complex number $S^1\simeq U(1)$
   * $(\mathbb{R},+)\simeq GL(1;\mathbb{R})^+$: positive determinant
2. [wiki-link](https://en.wikipedia.org/wiki/Special_linear_group) special linear group $SL(n;k)$ with $k=\mathbb{R},\mathbb{C}$
   * $x\in GL(n,k), det(x)=1$
3. [wiki-link](https://en.wikipedia.org/wiki/Unitary_group) unitary group $U(n)$
   * $xx^\dagger=x^\dagger x=I_n$
   * norm preserving over $\mathbb{C}$
4. special unitary group $SU(n)$
   * $x\in U(n), det(x)=1$
5. [wiki-link](https://en.wikipedia.org/wiki/Orthogonal_group) orthogonal group $O(n)$
   * $x\in GL(n,\mathbb{R}), xx^T=x^x=I_n$
   * norm preserving over $\mathbb{R}$
6. special orthogonal group $SO(n)$
   * $x\in O(n), det(x)=1$
7. complex orthogonal group $O(n;\mathbb{C})$
   * $x\in GL(n,\mathbb{C}),x^Tx=xx^T=I_n$
   * $det(x)=\pm 1$
8. special complex orthogonal group $SO(n,\mathbb{C})$
   * $x\in O(n,\mathbb{C}),det(x)=1$
9. [wiki-link](https://en.wikipedia.org/wiki/Indefinite_orthogonal_group) indefinite orthogonal group $O(p,q)$
   * $x\in GL(p+q,\mathbb{R}),g=diag(1,\cdots,1,-1,\cdots,-1), x^Tgx=g$
   * Lorentz group $O(3,1)$
10. indefinite special orthogonal group $SO(p,q)$
    * $x\in O(p,q),det(x)=1$
11. real symplectic group $Sp(n;\mathbb{R})$
    * $\Omega=(i\sigma_y)\otimes I_n, x\in GL(2n,\mathbb{R}),x^T\Omega x=\Omega$
    * $det(x)=1$
    * TODO how to generate
12. complex symplectic group $Sp(n;\mathbb{C})$
    * $\Omega=(i\sigma_y)\otimes I_n, x\in GL(2n,\mathbb{C}),x^T\Omega x=\Omega$
    * $det(x)=1$
    * TODO how to generate
13. [wiki-link](https://en.wikipedia.org/wiki/Symplectic_group) compact symplectic group $Sp(n)=Sp(n;\mathbb{C}) \cap U(2n)$
    * conjugate operator: $Pz=\bar{z}$
    * $J=(i\sigma_y\otimes I_n)P$
    * 等价定义 $Sp(n)=\left\{ x: x^\dagger x=xx^\dagger=I_{2n}, xJ=Jx \right\}$
    * unitary group over the quaternions
    * norm preserving over quaternion
    * TODO how to generate
14. [wiki-link](https://en.wikipedia.org/wiki/Euclidean_group) Euclidean group $E(n)$
    * $\left\{ (x,R):x\in\mathbb{R}^n,R\in O(n) \right\}$
    * $\left\{ x,R\right\} y=Ry+x$
15. [wiki-link](https://en.wikipedia.org/wiki/Poincar%C3%A9_group) Poincare group, inhomogeneous Lorentz group $P(n;1)$
16. [wiki-link](https://en.wikipedia.org/wiki/Lorentz_group) Lorentz group
17. [wiki-link](https://en.wikipedia.org/wiki/Heisenberg_group) Heisenberg group
    * Heisenberg-Weyl commutation relation
    * Baker-Campbell-Hausdorff ofrmula

concept

1. matrix Lie group: closed subgroup of $GL(n, \mathbb{C})$
   * a non-closed subgroup of $GL(n,\mathbb{C})$: $GL(n,\mathbb{Q})$
   * irrational line in a torus
2. Lie group but not matrix Lie group
   * $G=\mathbb{R}\times\mathbb{R}\times S^1=\left\{(x,y,u):x\in\mathbb{R},y\in\mathbb{R},u\in S^1\subset \mathbb{C}\right\}$
   * $(x_1,y_1,u_1)\cdot (x_2,y_2,u_2)=(x_1+x_2,y_1+y_2,e^{ix_1y_2}u_1u_2)$
3. manifold
4. quaternion algebra $\mathcal{H}$ [wiki](https://en.wikipedia.org/wiki/Quaternion): real linear combination of $I,i\sigma_z,i\sigma_y,i\sigma_x$
5. Jordan-Chevalley decomposition [wiki](https://en.wikipedia.org/wiki/Jordan%E2%80%93Chevalley_decomposition)

example

1. general linear Lie group (invertible matrix) $GL(n,\mathbb{R})$, $GL(n,\mathbb{C})$
   * general linear Lie algebra $gl(n,\mathbb{R})$, $gl(n,\mathbb{C})$
   * matrix exp, matrix logarithm, well-defined around a neighborhood of $0\in gl(n,\mathbb{K})$ and $I\in GL(n,\mathbb{K})$
2. $U(1)=\{e^{i\theta}:\theta\in[0,2\pi)\}$
3. NOT Lie group $H$: let (2-torus) $T^2=\{diag(e^{2\pi i\theta _0},e^{2\pi i \theta _1}):\theta_0,\theta_1\in\mathbb{R}\}$
   * $H=\{diag(e^{2\pi i\theta},e^{2\pi i a \theta}):\theta\in\mathbb{R}\}$ for some irrational number $a\in(\mathbb{R}\setminus\mathbb{Q})$
   * $H$ is not a Lie group in subspace topology, for that $H$ is not a topologically closed (not locally path-connected)
   * $H$ can be a Lie group under different topology
   * [wiki-link](https://en.wikipedia.org/wiki/Closed-subgroup_theorem) [wiki-link1](https://en.wikipedia.org/wiki/Lie_group#Non-example)
4. NOT Lie group $GL(n,\mathbb{Q})$
   * might be algebraic group
5. Lie group but not matrix Lie group
   * universal cover group of $SL(2,\mathbb{R})$ [wiki-link](https://en.wikipedia.org/wiki/SL2(R)#Topology_and_universal_cover)
   * metaplectic group [wiki-link](https://en.wikipedia.org/wiki/Metaplectic_group)
6. orthogonal group $O(n)=\{x\in\mathbb{R}^{n\times n}:xx^T=I\}$
   * $o(n)=\{x\in\mathbb{R}^{n\times n}:x+x^T=0\}$
7. $SL(n,\mathbb{K})=\{x\in\mathbb{K}^{n\times n}: \mathrm{det}(x)=1\}$
   * $sl(n,\mathbb{K})=\{x\in\mathbb{K}^{n\times n}:\mathrm{Tr}(x)=1\}$

preliminary

1. [wiki-link](https://en.wikipedia.org/wiki/Inverse_function_theorem) inverse function theorem

[youtube-link/JonathanEvans](https://youtu.be/kN-LZvrKJck?si=pfEjCoyQxPSuBwFI)

1. matrix exponential $exp(A)=\sum_{n=0}^{\infty}\frac{A^n}/n!$
   * $exp(-i\theta Y)=\cos(\theta)I-iY\sin(\theta)$
   * absolutely convergence
     * can reorder terms
   * uniformly convergence along with all its partial derivatives on any bounded set of matrix
     * can differentiate
     * differentiation op can be exchanged with the sum op
   * $\frac{d}{dt}(exp(tA))=A exp(tA)$
   * if $AB=BA$, then $exp(A+B)=exp(A)exp(B)$
     * [wiki-link](https://en.wikipedia.org/wiki/Cauchy_product) Cauchy product formula
     * $(exp(A))^{-1}=exp(-A)$
   * locally invertible $exp(A): \mathbb{R}^{n^2}\to\mathbb{R}^{n^2}$, $d_A(exp(A))|_{A=I}$ is a $n^2\times n^2$ identity matrix (invertible)
2. matrix logarithm $log(I+A)=\sum_{n=1}^\infty\frac{-(-1)^n}{n}A^n$
3. Baker-Campbell-Hausdorff formula
   * commutator $[A,B]=AB-BA$
   * $\log(e^Ae^B)=A+B + \frac{1}{2}[A,B] + \frac{1}{12}[A,[A,B]] - \frac{1}{12}[B,[A,B]]+\cdots$
   * only involve $A,B,[A,B]$
4. Lie group
   * def: smooth manifold required (TODO)
5. matrix Lie group $G$:
   * def: topologically closed subgroup of $GL(n,\mathbb{R})$
   * let $g=\{X\in gl(n,\mathbb{R}): e^{tX}\in G, t\in \mathbb{R}\}$ (not definition of Lie algebra)
     * $g$ is a vector space
     * if $x,y\in g$, then $[x,y]\in g$
     * $g$ is tangent space to $G$ at identity
     * $\mathrm{exp}: g\to G$ is locally invertible
6. lie algebra: vector space $\mathfrak{g}$ with a bilinear map $[\cdot,\cdot]:\mathfrak{g}\times \mathfrak{g}\to \mathfrak{g}$
   * def:
     * anti-symmetry: $[x,x]=0$, forall $x\in\mathfrak{g}$
       * imply $[x,y]=-[y,x]$
     * Jocabi identity: $[x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0$, forall $x,y,z\in \mathfrak{g}$
   * lie subalgebra
   * theorem: any finite dimensional lie algebra over $\mathbb{K}$ is a Lie subalgebra of $gl(n,\mathbb{K})$ for some $n$

pass

1. [stackexchange-link](https://math.stackexchange.com/a/1592257) if $G$ is a real finite-dimensional Lie group with Lie algebra $\mathfrak{g}$, then the following are equivalent
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
   * [github/specialunitary](https://github.com/xalhs/specialunitary)
   * [github/SU-tools](https://github.com/hellpig/SU-tools)
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

## youtube couse

notation

1. field $\mathbb{K}$

example

1. associative algebra $A$ with commutator $[x,y]=xy-yx$
2. general linear Lie algebra $\mathfrak{gl}_n(\mathbb{K})$: associative algebra $A=M_n(\mathbb{K})$: n-by-n matrix with matrix multiplication

introduction to Lie theory [youtube-link](https://youtu.be/mPccJXKtz_8?si=qWRipw_nsxP7yv9L)

1. finite-dimensional semisimple Lie-algebra $\mathbb{K}$-algebra for some field $\mathbb{K}$
2. associative algebra $A$
   * derivation: $D_x:A\to A, a\mapsto [x,a]$, $[x,yz]=[x,y]z+y[x,z]$
3. derivation of Lie algebra
4. algebraic groups
