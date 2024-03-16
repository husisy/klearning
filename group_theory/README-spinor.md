# Spinor

1. link
   * [youtube-link](https://youtube.com/playlist?list=PLJHszsWbB6hoOo_wMb0b6T44KM_ABZtBs&si=7UW77sYitKW5S03g) spinor for beginners
   * [youtube-link](https://youtu.be/60z_hpEAtD8?si=WVtexBsXiN1ZR1-j) A Swift Introduction to Geometric Algebra
   * [youtube-link](https://youtu.be/e7aIVSVc8cI?si=inbQhoJ2VMYgcHa-) A swift introduction to spacetime algebra
   * [thesis-link](https://scholar.uwindsor.ca/etd/5652/) an interpretation of relativistic spin entanglement using geometric algebra
   * [youtube/bivector](https://www.youtube.com/@bivector)
2. concept
   * spinors as square roots of vectors
   * Lie group, Lie algebra
   * Pauli spinor, Weyl spinor, Dirac spinor, Majorana spinor
   * def: members of minimal left ideal of Clifford algebra
   * spin value: Higgs Boson (0), electron/neutrino/quark (1/2), photon (1), Baryon (3/2), graviton (2)
   * Lorentz group: $SO(3,1)$
   * Jones vector and light polarization, left/right circular polarization, birefringent crystal
   * grassman algebra, exterior algebra, wedge product, bivector, grade
   * Clifford algebra, Clifford product, Geometric product
3. spinors, elements of complex projective line $\mathbb{CP}^1$
4. orthogonal projection, perspective projection
5. real projective space $\mathbb{RP}^n$
6. complex projective space $\mathbb{CP}^n$
7. Poincare sphere, Bloch sphere, Riemann sphere
8. Mobius transformation
9. reflection:  $V\to -UVU $
10. $1$-sphere is double cover of $1$-projective space, $2$-sphere is double cover of $2$-projective space
11. $SU(2)$ is double cover of $SO(3)$, $SL(2,C)$ is double cover of $SO^+(1,3)$ (also called $PSL(2,C)$)
12. spin group
    * spin(2): complex number
    * spin(3): $SU(2)$, unit quaternions
    * spin(1,3): $SL(2,C)$
13. Clifford algebra
    * $Cl(0,1)$: complex numbers
    * $Cl(1,0)$: Split complex numbers, $j^2=1$
    * $Cl(3,0)=\{\sigma_x^2=\sigma_y^2=\sigma_z^2=1, \sigma_i\sigma_j=-\sigma_j\sigma_i,i\ne j\}$: algebra of physical space
    * quaternions are even-grade sub-algebra of $Cl(3,0)$
    * $Cl(1,3)=\{\gamma_0^2=1,\gamma_i^2=-1,\gamma_\mu\gamma_\nu=-\gamma_\nu\gamma_\mu,\mu\ne\nu\}$: Dirac matrices (Chiral basis, Weyl basis), spacetime algebra
    * $Cl(p,q)$
    * $Cl(p)=Cl(p,0)$
    * $Cl(p,q,r)$: $\epsilon^2=0$
    * Clifford product $uv=u\cdot v+u\wedge v$
14. Tensor algebra

## Clifford algebra

example

1. $Cl(2,0)=\langle 1,e_1,e_2,e_1e_2\rangle$, $e_1e_1=e_2e_2=1,e_1e_2=-e_2e_1$
2. $Cl(3,0)=\langle 1,e_1,e_2,e_3,e_1e_2,e_2e_3,e_1e_3,e_1e_2e_3 \rangle$, $e_1e_1=e_2e_2=e_3e_3=1,e_1e_2=-e_2e_1,e_2e_3=-e_3e_2,e_1e_3=-e_3e_1,e_1e_2e_3=-e_2e_1e_3$

misc

1. link
   * [youtube-link](https://youtu.be/60z_hpEAtD8?si=_3L5-fgk9X3e9hz8) a swift introduction to geometric algebra
   * [book-link](https://maa.org/press/maa-reviews/geometrical-vectors) geometrical vectors, gabriel weinreich
   * [book-link](https://doi.org/10.1007/978-94-009-4728-3_2) clifford algebras and spinors, Pertti Lounesto
2. tensor algebra [wiki-link](https://en.wikipedia.org/wiki/Tensor_algebra)
   * def: vector space $V$ over field $F$, tensor algebra $T(V)=\bigoplus_{k=0}^{\infty} T^kV$ with $k$-th tensor power $T^kV=V^{\otimes k}$
3. dot product (inner product) $\vec{x}\cdot\vec{y}=\vec{y}\cdot\vec{x}$
4. wedge product (outter product) $\vec{x}\wedge\vec{y}$
   * $\vec{x}\wedge\vec{y}=-\vec{y}\wedge\vec{x}$
   * $\vec{x}\wedge\vec{x}=0$
   * cross product (3-dimensional only) $\vec{x}\times\vec{y}=\vec{x}\wedge\vec{y}$
5. geometric product $\vec{x}\vec{y}=\vec{x}\cdot\vec{y}+\vec{x}\wedge\vec{y}$
   * $\vec{x}^2=\lVert \vec{x}\rVert$
   * $\vec{x}^{-1}=\frac{\vec{x}}{\lVert \vec{x}\rVert}$
   * $2\vec{x}\cdot\vec{y}=(\vec{x}\vec{y}+\vec{y}\vec{x})$
   * $2\vec{x}\wedge\vec{y}=(\vec{x}\vec{y}-\vec{y}\vec{x})$
6. basis $\{\vec{e}_i\}$
   * $\vec{e}_i^2=1$
   * $\vec{e}_i\vec{e}_j=-\vec{e}_j\vec{e}_i$ for $i\ne j$
7. multivector
8. concept
   * scalar, vector, bivector, trivector
   * norm, basis
