# topology

set theory

1. complement $A^c=X\setminus A$
2. equivalence relation $\sim$: reflective, transitive, symmetric
   * $[x]$
   * quotient set $X/\sim$
3. countibility, set $X$
   * at most countably infinite: have injective map $f:X\to\mathbb{N}$
   * countably infinite: have bijective map $f:X\to \mathbb{N}$
   * personal-convention
     * do NOT use "countable"
     * use "finite" or "countably infinite", or "at most countably infinite"
     * notation: index set $(a_i)_{i\in\mathbb{N}}$ means at most countably infinite
   * example: interval $[0,1]$ (real numbers) are uncountable
4. cardinality
   * $\aleph_0$: cardinality of $\mathbb{N}$
   * rational number: $|\mathbb{Q}|=\aleph_0$
5. (personal convention) natural number $\mathbb{N}=\{0,1,2,\cdots,\}$ (including $0$)
6. pre-image

Cateogy theory

1. isomorphism
   * homeomorphism: topological space
   * linear isomorphism: vector space (invertible matrix)
   * group isomorphism: group
   * ring isomorphism: ring
   * graph isomorphism
   * diffeomorphism: smooth manifold
2. push forward, pull back

example

1. Euclidean space $\mathbb{R}^n$
2. n-Sphere $\mathbb{S}^n$
3. open unit ball $\mathbb{B}^n\subset \mathbb{R}^n$: $\{x\in \mathbb{R}^n:\lVert x\rVert< 1\}$ (open ball in Euclidean norm)
   * closed unit ball $\bar{\mathbb{B}}^n$
4. n-torus $\mathbb{T}^n=\mathbb{S}^1\times \cdots\times\mathbb{S}^1$
5. trivial topology $\{\emptyset,X\}$ (coarsest topology)
6. discrete space, let $T$ be the power set $\mathcal{P}(X)$ (finest topology)
7. metric topology $(X,d)$, let $T$ be collection of open sets in the usual sense
   * (def) open set $U$: $\forall x\in U,\exists r>0,B(x,r)\subseteq U$, where $B(x,r)=\{y\in X:d(x,y)<r\}$
8. $\mathbb{R}P^n$: set of 1-dimensional subspace in $\mathbb{R}^{n+1}$
   * equivalence relation $[x]=\{c x:c\in\mathbb{R}\}$ for all $x\in\mathbb{R}^{n+1}\setminus\{0\}$
   * quotient of n-Sphere by relation $x\sim y$ if $x=\pm y$
9. misc
   * Sierpiński space $X=\{0,1\},T=\{\emptyset,\{1\},\{0,1\}\}$ [wiki-link](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_space)
   * $X=\{1,2,3\},T=\{\{1,\},\{1,2\},\{1,2,3\},\emptyset\}$
   * $X=\{1,2,3\},T=\{\emptyset,\{1,\},\{1,2\},\{1,3\},\{1,2,3\}\}$
   * $\mathbb{R}$, $\mathbb{T}=\{(a,\infty):a\in\mathbb{R}\}$
10. open interval $(0,1)$ and a half-open interval $[0,1)$ are not homeomorphic
    * the connectedness is different after removing a point [stackexchange-link](https://math.stackexchange.com/q/1054488)
11. $[0,1]$ is a $1$-dimensional smooth manifold with boundary, $[0,1]\times [0,1]$ is NOT a $2$-dimensional smooth manifold with boundary
    * but $[0,1]\times [0,1]$ is a $2$-dimensional topological manifold with boundary [stackexchange-link](https://math.stackexchange.com/a/1820081)
    * [stackexchange-link1](https://math.stackexchange.com/q/2028877)
12. in the usual topology of $\mathbb{R}$, $\mathbb{Q}$ is neither open nor closed
    * not open: its interior is empty
    * not closed: its closure is $\mathbb{R}$
    * [stackexchange-link](https://math.stackexchange.com/a/116730)

preliminary (notation, etc.)

1. link
   * [youtube-course](https://youtube.com/playlist?list=PLd8NbPjkXPliJunBhtDNMuFsnZPeHpm-0&si=CmOIXC80pw0evcbJ)
   * [wiki/de-morgan-laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws)
   * [doi-link@book](https://doi.org/10.1007/978-1-4419-7940-7) Introduction to Topological Manifolds, John M. Lee
2. index notation
   * at most countable index $\mathbb{N}$
   * index $I$ (finite, countably infinite or uncountable)
3. usually convention
   * continuous function is called map. map usually means continuous function
4. pre-image is compatible with pretty much every set operation
5. surjective map: double-headed arrow $\twoheadrightarrow$
6. abbreviation
   * "i.e.": that is (Latin)
   * "e.g.": for example Latin
   * "s.t.": such that
   * "iff": if and only if
7. set-theoretic topology [wiki-link](https://en.wikipedia.org/wiki/Set-theoretic_topology)
8. Categorical Representation of Set-Theoretic Topology [stack-exchange-link](https://math.stackexchange.com/q/1903917)

basic concept

1. topological space $(X,T)$: $X$ is a set, $T$ is a collection of subsets of $X$
   * $X\in T$, $\emptyset\in T$
   * $T$ is closed under finite intersection
   * $T$ is closed under arbitrary unions
   * nomenclature: $T$ is the topology on $X$. $X$ is a topological space with topology $T$
   * equivalent definition on closed set: $X$ and $\emptyset$ are closed, $T$ is closed under finite union, $T$ is closed under arbitrary intersection
2. neighborhood of $y\in X$ is a subset $V\subseteq X$ that contains an open set $U$ such that $p\in U\subseteq V\subseteq X$
3. closed set $A\subseteq X$: $X\setminus A$ is open
   * example
     * $[a,b]$ in $\mathbb{R}$
     * closed unit ball in metric space
     * any subset in discrete space
4. subset $A\subseteq X$
   * open
   * closed
   * open and closed (e.g. $\emptyset$ and $X$)
   * neither open nor closed
5. point $p\in X$, subset $A\subseteq X$, topological space $(X,T)$
   * closure: $\mathrm{cl}(A)=\cap\{ B: A\subseteq B, B^c\in T \}$
   * interior: $\mathrm{int}(A)=\cup\{ B\in T: B\subseteq A \}$
   * exterior: $\mathrm{ext}(A)=X\setminus \mathrm{cl}(A)$
   * boundary: $\partial A=X\setminus(\mathrm{int}(A)\cup\mathrm{ext}(A))$
     * boundary contains isolated points
     * boundary is closed
   * derived set $A'$: set of all limit points in $A$
     * derived set is closed
   * $p\in\mathrm{int}(A)$: exists $U\in T$ such that $p\in U\subseteq A$
   * $p\in\partial A$: for all open set $p\in U\in T$, $U\cap A\ne \emptyset$ contains points in $A$ and points in $X\setminus A$
   * $p$ is a limit point of $A$: for all open set $p\in U\in T$, $(U\setminus\{p\})\cap A\ne \emptyset$
     * example: limit point of $A=(0,1)$ in $\mathbb{R}$: $[0,1]$
     * example: limit point of $A=\{\frac{1}{n}:n\in\mathbb{Z}_+\}$ in $\mathbb{R}$: $\{0\}$
   * $p$ is a isolated point of $A$ if: exists open set $p\in U\in T$ such that $U\cap A=\{p\}$
     * isolated point of $A=\{\frac{1}{n}:n\in\mathbb{Z}_+\}$ in $\mathbb{R}$: $A$
   * $A$ is dense: $\mathrm{cl}(A)=X$
     * iff every point of $X$ is a limit point of $A$
     * iff every nonempty open set in $X$ intersects $A$ (contains a point of $A$)
     * example: rational number $\mathbb{Q}$ is dense in $\mathbb{R}$
6. space $(X,T)$, sequence of points $(x_i)_{i\in\mathbb{N}}$, $x_i\in X$
   * converge to the limit, $(x_i)_{i\in\mathbb{N}}\to x$ for $x\in X$ if: for all open set $x\in U\in T$, there is $N\in\mathbb{N}$ such that $x_i\in U$ for all $i\geq N$
7. continuous map: space $(X_1,T_1)$, space $(X_2,T_2)$, function $f:X_1\to X_2$
   * $f$ is continuous: for every open set $U_2\in T_2$, its pre-image $f^{-1}(U_2)\in T_1$
     * iff the pre-image of every closed set is closed
     * iff every point of $x\in X_1$ has a open set $x\in U_1$ (exists $U_1$) such that $f(x)\in f(U_1)\in T_2$
     * example: constant map, identity map, domain restriction $f|_U$, composition $f\circ g$
8. homeomorphism $X\cong Y$
   * def: a continuous map $f:X\to Y$ is a homeomorphism if there is a continuous map $g:Y\to X$ such that $g\circ f=\mathrm{id}_X$ and $f\circ g=\mathrm{id}_Y$
   * counter-example, bijective, but both $f$ and $g$ non-continuous: $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x$ is $x$ is rational, $f(x)=x+1$ if $x$ is irrational
   * counter-example, continuous $f$ has inverse, but $g$ non-continuous
     * [stackexchange-link](https://math.stackexchange.com/a/68811)
     * $[0,1]\cup(2,3]\to [0,2]$
     * every bijective map $X\to K$ with $X$ non-compact and $K$ compact cannot have a continuous inverse
   * homeomorphism is equivalence relation
   * example
     * any two open balls in $\mathbb{R}^n$ are homeomorphic: translation, dilation (size is not a topological property)
     * the unit ball $\mathbb{B}^n$ is homoemorphic to $\mathbb{R}^n$ $f(x): x\mapsto \frac{x}{1-\lVert x\rVert}$, inverse $g: y\mapsto \frac{y}{1+\lVert y \rVert}$ (boundedness is not a topo property)
     * the cube $C=\{x\in\mathbb{R}^n:\lVert x\rVert_\infty=1\}$ is homeomorphic to $\mathbb{S}^{n-1}$ (corners are not a topo property)

video05-

1. subspace topology: given topological space $X$ and a subset $S\subset X$, we say $U$ is open in $S$ iff $U=S\cap V$ for some open set $V\in X$
   * example: $X=\mathbb{R}, S=[0,1)$, then $U=[0,\frac{1}{2})$ is open in $S$
2. open map
   * def: a continuous map $f:X\to Y$ is an open map if for every open set $U\in X$, $f(U)$ is open in $Y$
   * counter-example, continuous but not open map: $f:\mathbb{R}\to\mathbb{R}$, $f(x)=0$
3. closed map
   * def: a continuous map $f:X\to Y$ is a closed map if for every closed set $A\in X$, $f(A)$ is closed in $Y$
   * counter-example, contiuous but not closed map: $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$ (neither open nor closed)
4. suppose $f:X\to Y$ is a continuous bijective map, then the following is equivalent
   * $f$ is a homeomorphism
   * $f$ is open
   * $f$ is closed
5. local homeomorphism
   * def: a map $f:X\to Y$ is a local homeomorphism if each point $x\in X$ has a neighborhood $U$ such that $f(U)$ is open in $Y$ and $f|_U:U\to f(U)$ is a homeomorphism
   * counter example, not equivalence relation: $\mathbb{S}^2$ is locally homeomorphic to $\mathbb{R}^2$, there is no local homeomorphism from $\mathbb{S}^2\to\mathbb{R}^2$ [wiki-link](https://en.wikipedia.org/wiki/Local_homeomorphism)
   * counter example, local homeomorphism vs homeomorphism: $f:\mathbb{S}^1\to\mathbb{S}^1$, $f(z)=z^3$
   * proposition: a bijective local homeomorphism is a homeomorphism
6. Hausdorff space (counter example) $Z=\{1,2,3\}, T=\{\emptyset,\{1\},\{1,2\},\{1,2,3\}\}$
   * $\{1\}$ is not closed
   * constant sequence $(2,2,\cdots)$ has $2$ and $3$ as limit
7. Hausdorff space
   * def: a topological space $X$ is Hausdorff if for every pair of distinct points $x,y\in X$, there are disjoint open sets $U,V\in X$ such that $x\in U$ and $y\in V$ (disjoint neighborhoods)
   * example
     * all metric space (spaces that aren't Hausdorff aren't going to be metrizable)
     * discrete space
   * prop: any finite subset of a hausdorff space is closed
   * prop: in Hausdorff spaces, convergent sequences have unique limits
   * prop: suppose $X$ is Hausdorff and $A\subseteq X$. If $p\in X$ is a limit point of $A$, then every neighborhood of $p$ contains infinitely many points of $A$
     * comment: finite subset cannot have limit point, so $A$ must be infinite
8. basis $\mathcal{B}$: a collection of subsets of a topological space $X$
   * def: every $B\in\mathcal{B}$ is open, every open subset of $X$ is the union of elements in $\mathcal{B}$
   * example
     * open balls form a basis for metric space $(\mathcal{M},d)$: $\mathcal{B}=\{B(x,r):x\in\mathcal{M},r>0\}$ (metric space is defined in this way)
     * the collection of all singletons is a basis for the discrete topology on any set
   * (basis criterion) subset $U\subseteq X$ is open iff for each $p\in U$, there is $B\in\mathcal{B}$ with $p\in B \subseteq U$
   * (continuity criterion) a map $f:X\to Y$ is continuous iff $f^{-1}(B)$ is open for each $B\in\mathcal{B}$ (basis for $Y$)
9. unique topology: let $X$ be a set and $\mathcal{B}$ a collection of subsets of $X$. Then $\mathcal{B}$ is a basis for a unique topology on $X$ iff
   * $\cup_{B\in\mathcal{B}}B=X$
   * for each $B_1,B_2\in\mathcal{B}$ and each $p\in B_1\cap B_2$, there is $B_3\in\mathcal{B}$ with $p\in B_3\subseteq B_1\cap B_2$

video09

1. second countable: a topological space is called second countable if it has a countable basis for its topology
   * every Euclidean space is second countable
     * $\mathcal{B}=\{B(x,r):x\in\mathcal{M},r>0\}$ is uncountable
     * $\mathcal{B}=\{B(x,r):x\in\mathbb{Q}^n, r\in\mathbb{Q}_{>0}\}$ is countable
   * necessary for topological manifold
2. neighborhood basis: a collection $\mathcal{B}$ of neighborhoods of $p\in X$ is called a neighborhood basis for $p$ if every neighborhood of $p$ contains some element of $\mathcal{B}$
3. first countable: a topological space is called first countable if it has a countable neighborhood basis for each of its points
   * every second countable space is first countable
   * counter-example, not first countable: cofinite topology on an infinite set [wiki-link](https://en.wikipedia.org/wiki/Cofiniteness#Cofinite_topology)
   * counter-example, first countable but not second countable: $\mathbb{R}$ in a discrete topology $d(x,y)=0$ if $x=y$, $d(x,y)=1$ if $x\neq y$
   * useful in convergent sequence
   * prop: suppose $X$ is first countable, then
     * $p\in \mathrm{cl}(A)$ iff $p$ is a limit of a sequence in $A$
     * $p\in \mathrm{int}(A)$ iff every sequence in $X$ converges to $p$ is eventually in $A$
     * $A$ closed iff every sequence in $A$ converges to a point in $A$
     * $A$ open iff every sequence in $X$ converges to a point in $A$ is eventually in $A$
4. topological manifold
   * manifold with boundary example: cylinder of finite height
   * manifold example: $\mathcal{R}^2$, $\mathbb{S}^2$, $\mathbb{B}^2$
   * def: a space $\mathcal{M}$ is locally Euclidean of dimension $n$ if every point $p\in\mathcal{M}$ has a neighborhood $U$ that is homeomorphic to an open ball $\mathbb{B}^n\in\mathbb{R}^n$ (or any open subset of $\mathbb{R}^n$, or $\mathbb{R}^n$ itself)
   * def: a $n$-dimensional topological manifold is a second countable Hausdorff space that is locally Euclidean of dimension $n$
   * terminology
     * topological manifold $\mathcal{M}$
     * point $x\in \mathcal{M}$
     * coodinate domain $U_x$ (neighborhood)
     * coordinate map $\phi_x$ (local homeomorphism map)
     * coordinate chart $(u_x,\phi_x)$
     * atlas $\mathcal{A}=\{(u_x,\phi_x):x\in \mathcal{M}\}$
5. theorem: if positive integer $m\ne n$, a non-empty space cannot be both a $m$-manifold and $n$-manifold
   * to be proved in algebraic topology
   * homotopy
   * homology
6. upper half-space $\mathbb{H}^n=\{x\in\mathbb{R}^n:x_n\geq 0 \}\subset \mathbb{R}^n$
7. $n$-dimensional manifold with boundary
   * def: a second coutable Hausdorff space in which every point has a neighborhood homeomorphic to an open subset of $\mathbb{R}^n$ or $\mathbb{H}^n$
   * WARNING ambiguity in terminology: boundary of a manifold, boundary of a set in topological space
     * topological interior of a manifold doesn't necessary have to be its interior
   * theorem: no point of a manifold with boundary is both a boundary point and an interior point
8. inclusion map: $A\subseteq B$, $\iota:A\hookrightarrow B$
   * $f\circ \iota=f|_A$
9. subspace topology
   * def: given a topological space $(X,\mathcal{T}_X)$ and any subset $S\subseteq X$ (open, closed, whatever), $\mathcal{T}_S=\{S\cap U: U\in\mathcal{T}_X\}$
   * example
     * $S=[0,1)$ in $\mathbb{R}$
     * $S=\{1/n:n\in\mathbb{Z}_{>0}\}$ in $\mathbb{R}$
   * prop: let $U\subseteq S \subseteq X$
     * if $U$ is open (closed) in $X$, then $U$ is open in $S$
     * if $S$ is open (closed) in $X$, and $U$ is open in $S$, then $U$ is open in $X$
   * (characteristic property) Let $S\subseteq X$ be a subspace, for any space $Y$, a function $f:Y\to S$ is continuous iff $\iota\circ f: Y\to X$ is continous
   * let $X,Y,Z$ be space, and $f:X\to Y$ is continous
     * if $S\subseteq X$, then $f|_S:S\to Y$ is continuous
     * if $T\subseteq Y$ and $f(x)\subseteq T$, then $f:X\to T$ is continuous
     * if $Y\subseteq Z$, then $f:X\to Z$ is continuous
   * let $S\subseteq X$ be a subspace, then
     * if $R\subseteq S$ is a subspace, then $R$ is a subspace of $X$
     * if $\mathcal{B}$ is a basis of $X$, then $\{B\cap S:B\in\mathcal{B}\}$ is a basis of $S$
     * if $(p_i)_i$ is a sequence in $S$ and $p\in S$, then $(p_i)_i$ converges to $p$ in $S$ iff $(p_i)_i$ converges to $p$ in $X$
   * subspace preserve: Hausdorff property, first/second countability
10. product space
    * def: let $X_1,\cdots, X_n$ be spaces, the product topology $X_1\times \cdots\times X_n$ is generated by the basis $\mathcal{B}=\{U_1\times \cdots\times U_n:U_i\in\mathcal{T}_{X_i}\}$
    * (characteristic property) for any space $Y$ and function $f: Y\to X_1\times \cdots\times X_n$, $f$ is continuous iff each coordinate function $f_i=\pi_i\circ f:Y\to X_i$ is continuous
    * product of function: preserve continuity, homeomorphism
    * property
      * each $\pi_i$ is an open map
      * basis product
      * compatibility with subspace topology
      * product preserve: Hausdorff property, first/second countability
      * product of topological manifold
11. disjoint union spaces $\coprod$
    * def: let $(X_\alpha)_{\alpha\in A}$ be an indexed family of spaces, then $\coprod_{\alpha\in A} X_\alpha=\{(x,\alpha):x\in X_\alpha\}$ with topology such that a subset $U\in \coprod_{\alpha\in A}X_\alpha$ is open if $U\cap X_\alpha$ is open for each $\alpha\in A$
    * embedding: $\iota_\alpha: X_\alpha\hookrightarrow \coprod_\alpha X_\alpha$
    * (characteristic property) for any space $Y$ and function $f: \coprod_\alpha X_\alpha\to Y$, $f$ is continuous iff each coordinate function $f_\alpha=f|_{X_\alpha}:X_\alpha\to Y$ is continuous
    * prop:
      * $C\subseteq \coprod_{\alpha}X_\alpha$ is closed iff $C\cap X_\alpha$ is closed in $X_\alpha$ for each $\alpha\in A$
      * each injection $\iota_\alpha:X_\alpha\to \coprod_\alpha X_\alpha$ is an topological embedding
      * disjoint union preserve: Hausdorff property, first countability, second countability (provided $A$ is countable)

video14-

1. quotient space
   * def: let $X$ be a space, $Y$ a set, and $q:X\to Y$ a surjective map. Then $Y$ has a quotient topology with respect to $q$ if a subset $U\subseteq Y$ is open iff $q^{-1}(U)$ is open in $X$
   * immediately from definition, $q$ is continuous
   * pre-image of a singleton $q^{-1}(\{y\})$ is called fiber over $y$
   * partition of $X$ (equivalence relation): $x\sim x'$ iff $q(x)=q(x')$
   * disjoint union of non-empty sets such that the union is the whole set
   * any composition of quotient map is a quotient map
   * an injective quotient map is a homeomorphism
   * a subset $K\in Y$ is closed iff $q^{-1}(K)$ is closed
   * disjoint union of quotient map is a quotient map
2. let $q:X\to Y$ be an open quotient map, then
   * $Y$ is Hausdorff, iff $R=\{(x_1,x_2):q(x_1)=q(x_2)\}$ is closed in $X\times X$
3. saturated w.r.t map: let $q:X\to Y$ (arbitrary set)
   * A subset of the form $q^{-1}(y)$ for $y\in Y$ is called a fiber of $q$
   * A subset $U\subseteq X$ is called saturated w.r.t. $q$, if it is a union of fibers
4. a continuous surjective map $q:X\to Y$ is a quotient map iff it takes saturated open subsets to open subsets, or equivalently, it takes saturated closed subsets to closed subsets
   * if $U\subseteq X$ is a saturated open (closed subset), then $q|_U:U\to q(U)$ is a quotient map
5. example
   * subspace topology $X=[0,1]$ in $\mathbb{R}$, let equivalence relation generated by $0\sim 1$, then $X/\sim\cong \mathbb{S}^1$
   * closed ball $\bar{\mathbb{B}}^2$, let equivalence relation generated by $((x,y)\sim(-x,y))$ (for boundary point only), then $\bar{\mathbb{B}}^2/\sim\cong \mathbb{S}^2$
   * interval $[0,1]\times [0,1]$, let equivalence relation generated by $((x,1)\sim(x,0),(1,y)\sim(0,y))$, then $[0,1]\times [0,1]/\sim\cong \mathbb{T}^2$
   * $\mathbb{S}^2$, let relation be $((0,0,1)\sim(0,0,-1))$
   * cone on $X$: $\mathrm{CX}=X\times [0,1]/\sim$, let relation be $((x,0)\sim(y,0):\forall x,y\in X)$
   * wedge sum: let space $X_1,X_2,\cdots,X_n$, each identity one point $x_i\in X_i$, then $X_1\vee X_2\vee\cdots\vee X_n=X_1\coprod X_2\coprod\cdots\coprod X_n/\sim$, let relation be $((x_i\sim x_j):\forall i,j)$
   * $q:\mathbb{R}^{n+1}\setminus\{0\}\to \mathbb{S}^n$, $q(x)=\frac{x}{||x||}$
6. let $f:X\to Y$ be a continuous map that is either open or closed
   * if $f$ is injective, it is a topological embedding
   * if $f$ is surjective, it is a quotient map
   * if $f$ is bijective, it is a homeomorphism
7. adjunction space
   * def let $X$ and $Y$ be spaces, $A\subseteq Y$ is closed, and $f:A\to X$ a continuous function, define the adjunction space $X\cup_f Y$ to be the quotient space of the disjoint union $X\coprod Y$ obtained by identifying $f(a)\in X$ with $a\in A$, where $a\sim f(a)$ for all $a\in A$
   * quotient map $q: X\coprod Y \to X\coprod_f Y$
     * $q|_X$ is an embedding with closed image
     * $q|_{y\setminus A}$ is an embedding with open image
     * $q\cup_f Y=q(X)\coprod q(Y\setminus A)$
   * example
     * wedge sum
     * $\mathbb{S}^2$ from 2 disks $\bar{\mathbb{B}}^2\cup_f\bar{\mathbb{B}}^2$ with boundary glued
     * attaching manifolds along boundary, "double" of $X$ $X\cup_{\partial X} X$ always a manifold without boundary

(TODO video17 on quotient space-III is skipped for category theory)

video18-

1. connectedness
   * def: a topological space $X$ is disconnected iff it can be expressed as the disjoint union of two non-empty open subsets $U\coprod V=X$
   * a space that is not disconnected is said to be connected
   * example
     * $\mathbb{R}\setminus \{0\}$ is disconnected
     * the disjoint union of two closed disks in $\mathbb{R}^2$ is disconnected
     * $\mathbb{Q}^2$ is disconnected in $\mathbb{R}^2$: $U=\{(x,y)\in\mathbb{Q}^2: x< \sqrt{2}\}$
     * intervals $[a,b]$ are connected
     * open (closed) disks are connected
     * $\mathbb{R}^n$ is connected
   * prop
     * (characterization) $X$ is connected, iff $X,\emptyset$ are the only subsets of $X$ that are simultaneously open and closed (clopen)
     * (characterization) $X$ is connected, iff $X$ is not homeomorphic to a disjoint union of two non-empty spaces
   * continuous image of a connected space is connected
   * any space homeomorphic to a connected space is connected
   * suppose $U,V$ are disjoint open subsets of a space $X$. If $A\subseteq X$ is connected and $A\subseteq U\cup V$, then $A\subseteq U$ or $A\subseteq V$
   * let $X$ be a space and $\{B_\alpha\}_{\alpha\in A}$ be a collection of connected subspaces that share a point, then $\cup_{\alpha\in A}B_\alpha$ is connected
   * any product of finitely many connected spaces is connected
     * TODO infinite product, any counter-example?
   * any quotient of a connected space is connected
   * the connected subsets of $\mathbb{R}$ are $\emptyset$, points, intervals, and $\mathbb{R}$
   * (intermediate value theorem) Let $X$ be a connected space and $f:X\to \mathbb{R}$ continuous. If $p,q\in X$, then $f$ attains every value between $f(p)$ and $f(q)$
2. path
   * def: let $X$ be a topological space and $p,q\in X$, a path in $X$ from $p$ to $q$ is a continuous map $f:[0,1]\to X$ with $f(0)=p$ and $f(1)=q$
3. path connectedness
   * def: A space $X$ is called path-connected iff for all $p,q\in X$, there is a path in $X$ from $p$ to $q$
   * continuous image of a path-connected space is path-connected
   * let $\{B_\alpha\}_{\alpha\in A}$ be a collection of path-connected subspace of $X$ with a point in common, then $\cup_{\alpha\in A}B_\alpha$ is path-connected
     * path composition $\gamma\ast\gamma'$
   * every product of finitely many path-connected spaces is path-connected
   * every quotient of a path-connected space is path-connected
   * path-connectedness implies connectedness (equivalent for topological manifold)
   * path-connected example
     * $\mathbb{R}^n$
     * convex subsets of $\mathbb{R}^n$
     * $\mathbb{S}^n$ for $n\geq 1$
     * $n$-torus
   * counter-example, connected but not path-connected: topologist's sine curve $T_0=\{(0,y):y\in[-1,1]\}$, $T_+=\{ (x,\sin(1/x)):x\in(0,1] \}$, then $T_0\cup T_+$ is connected but not path-connected
4. components
   * def: let $X$ be a topological space, a component of $X$ is a maximal connected nonempty subset of $X$
   * example: $\mathbb{Q}$ in $\mathbb{R}$ has infinite components with each being a singleton
   * prop
     * the components of $X$ form a partition of $X$
     * each component of $X$ is closed in $X$
     * any nonempty connected subset of $X$ is contained in a component of $X$
5. path component
   * def: a path component of $X$ is a maximal nonempty path-connected subset
     * the path components of $X$ form a partition of $X$
     * each path component is contained in a single component, and each component is a disjoint union of path components
     * any nonempty path connected subset of $X$ is contained in a path component of $X$
6. locally (path) connected
   * def: a space $X$ is locally (path) connected if it admits a basis of (path) connected open subsets.
   * prop: any neighborhood of $p\in X$ contains a (path) connected open set of $p$
   * prop: locally path-connected implies locally connected
   * example
     * $\mathbb{R}^n$: locally path-connected
     * all topological manifold: locally path-connected
     * $\mathbb{Q}$ is not locally connected
     * connected does not imply locally connected: topologist's sine curve
   * prop: suppose $X$ is locally connected
     * every open subset of $X$ is locally connected
     * every component of $X$ is open in $X$
   * prop: suppose $X$ is locally path-connected
     * $X$ is locally connected
     * every open subset of $X$ is locally path-connected
     * every path component of $X$ is open in $X$
     * path-connected do NOT imply locally path-connected: topologist's sine curve variant [stackexchange-link](https://math.stackexchange.com/a/135483)
     * the path components of $X$ are the same as its components
     * $X$ is connected iff it's path-connected

video22-

1. def open cover: an open cover $\{U_\alpha\}_{\alpha \in A}$ of a space $X$ is a collection of open subsets of $X$ whose union is $X$
2. def subcover: a subcover $U$ is a subcollection of elements of $U$ that still covers $X$
3. def compact: a space $X$ is compact if every open cover of $X$ has a finite subcover
   * in Euclidean space: compact, iff closed and bounded (Bolzano–Weierstrass theorem) [wiki-link](https://en.wikipedia.org/wiki/Bolzano%E2%80%93Weierstrass_theorem)
   * a subset $A\subseteq X$ is compact if $A$ is compact in the subspace topology
   * example
     * every finite space is compact
     * every space with the trivial topology is compact
     * a subset of a discrete space is compact iff it is finite
   * a subset $A\subseteq X$ is compact iff every collection $\{U_\alpha\}_\alpha$ of open subsets of $X$ such that $A\subseteq \cup_\alpha U_\alpha$ has a finite subcover
     * let $X$ be a space (may not compact) and let $(x_i)_i$ be a sequence in $X$ converging to $y\in X$. then the subset $\{x_i:i\in\mathbb{Z}_{+}\}\cup \{y\}$ is compact
   * theorem: let $X$ and $Y$ be spaces, and $f:X\to Y$ continuous. If $X$ is compact, then $f(X)$ is compact
   * lemma: let $X$ be a Hausdorff space and $A,B\subseteq X$ disjoint compact subsets. then there are disjoint open subsets $U,V$ with $A\subset U$ and $B\subset V$
   * prop:
     * closed subsets of compact spaces are compact
     * compact subsets of Hausdorff spaces are closed
     * compact subsets of metric spaces are bounded
     * finite products of compact spaces are compact
     * quotients of compact spaces are compact

TODO-stop at video23 compactness II, 19:09
