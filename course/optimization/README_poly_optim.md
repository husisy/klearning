# MPO

Jiawang Nie, moment and polynomial optimization [doi-link](https://doi.org/10.1137/1.9781611977608)

example

1. nonnegative orthant $\mathbb{R}_+^n$
2. Lorentz cone, ice cream cone

software

1. GloptiPoly 3 [homepage](https://homepages.laas.fr/henrion/software/gloptipoly3/)
2. SeDuMi [github-fork](https://github.com/sqlp/sedumi)
3. SDPNAL [homepage](https://blog.nus.edu.sg/mattohkc/softwares/sdpnalplus/)

## seminar

1. polynomial function
   * compute global optimizers, if none, find best local ones
   * be able to verify global optimality
   * certify infeasibility, unboundedness
2. truncated moment problem (TMP)
   * polynomial convex hull problem
   * certify for nonexistance
   * most matrix/tensor decomposition
3. tensor computation (TC)
   * spectral norm
   * nuclear tensor norm
4. Borel measure
5. localizing matrix
6. Lasserre Hierarchy of relaxation
7. archimedean condition (AC)
8. sum of squares (SOS)
9. finite convergence of Lasserre's hierarchy
10. saddle point problem (SPP)
11. canonical polyadic decomposition (CPD)

## chapter 1

1. concept
   * affine hull
   * affine subspace
   * closure $\mathrm{cl}(C)$
   * interior $\mathrm{int}(C)$
   * open set, close set
   * convex domain, convex body
   * boundary $\partial C$
   * relative interior $\mathrm{ri}(C)$, relatively open
   * interval $[a,b]$, $(a,b)$
   * extreme point
   * face, trivial face, proper face, exposed face
   * convex hull $\mathrm{conv}(C)$
   * cone hull $\mathrm{cone}(C)$
   * polar
   * cone, pointed cone, proper cone, solid cone, extreme ray, polar cone, dual cone
   * polyhedra, polytope (bounded polyhedra), vertex, facet, edge, ridge
2. Caratheodory's theorem [wiki-link](https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_(convex_hull))
   * exmaple [stackexchange-link](https://math.stackexchange.com/a/4252695)
3. Krein Milman theorem, Minkowski's theorem [wiki-link](https://en.wikipedia.org/wiki/Krein%E2%80%93Milman_theorem)
4. bipolar theorem [wiki-link](https://en.wikipedia.org/wiki/Bipolar_theorem)
5. Farkas lemma [wiki-link](https://en.wikipedia.org/wiki/Farkas%27_lemma)
