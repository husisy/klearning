# measure

example

1. length, area, volume
2. $X=\{0,1,2,3\}$, $M=\{\{0\},\{1\}\}$, $\sigma(M)=\{\emptyset,X,\{0\},\{1,2,3\},\{1\},\{0,2,3\},\{0,1\},\{2,3\}\}$
3. counting measure
4. Dirac measure
5. "normal" measure on $\mathbb{R}^n$
   * $\mu([0,1]^n)=1$
   * $\mu(x+A)=\mu(A)$, for all $x\in\mathbb{R}^n$
6. zero measure
7. $(\mathbb{R},P(\mathbb{R}))$ is not Lebesgue measurable
8. $(\mathbb{R},B(\mathbb{R}))$: Borel $\sigma$-algebra on $\mathbb{R}$

notation

1. power of set $P(X)$
2. countable index $\mathbb{N}$
3. index set $I$ (countable or uncountable)
4. $\sigma$-algebra: $\mathcal{F}$
5. calculation rules in $[0,\infty]=[0,\infty)\cup\{\infty\}$
   * $0\cdot\infty=0$ (in most cases in measure theory)
   * $x+\infty=\infty,x\in[0,\infty]$
   * $x\cdot\infty=\infty,x\in(0,\infty]$
6. measurable function: measurable map with image in real with Borel measure, $f:X\to\mathbb{R}$, $f^{-1}(A)=\{x\in X:f(x)\in A\}$
7. $\mu$-ae: almost everywhere with respect to $\mu$

[youtube-link](https://youtu.be/xZ69KEg7ccU?si=S19ZoFKmtpufYIX8)

1. $\sigma$ algebra
   * def: let $X$ be a set, $\mathcal{F}\subseteq P(X)$
     * $\emptyset\in \mathcal{F}$, $X\in \mathcal{F}$
     * closed under complementation: if $A\in \mathcal{F}$, the $X\setminus A \in \mathcal{F}$
     * closed under countable union: if $(A_i)_{i\in\mathbb{N}}$, then $\bigcup_{i\in\mathbb{N}}A_i\in \mathcal{F}$
   * name: let $A\in \mathcal{F}$, $A$ is a $\mathcal{F}$-measurable set
   * prop
     * closed under countable intersection
     * intersection of a collection of $\sigma$-algebra is a $\sigma$-algebra: if $(\mathcal{F}_i)_{i\in I}$ is a family of $\sigma$-algebra, then $\bigcap_{i\in I}\mathcal{F}_i$ is a $\sigma$-algebra
   * smallest $\sigma$-algebra generated by a subset $M\subseteq P(X)$: $\sigma(M)=\bigcap_{M\subseteq \mathcal{F}_i}\mathcal{F}_i$ intersection of all $\sigma$-algebra containing $\mu$
2. Borel $\sigma$-algebra: let $X$ be a topological space, the $\sigma$-algebra generated by the open set
3. measurable space $(X,\mathcal{F})$
4. measure space $(X,\mathcal{F},\mu)$
   * measure map $\mu:\mathcal{F}\to[0,\infty]$
     * $\mu(\emptyset)=0$
     * a disjoint countable collection of subsets $(A_i)_{i\in\mathbb{N}}$ with $A_i\cap A_j=\empty,i\ne j$, then $\mu(\bigcup_{i\in\mathbb{N}}A_i)=\sum_{i\in\mathbb{N}}\mu(A_i)$
5. let $\mu$ be a measure on $P(\mathbb{R})$ with $\mu((0,1])$ finite and $\mu(x+A)=\mu(x)$, $A\in P(\mathbb{R}),x\in\mathbb{R}$, the only possible value for $\mu$ is $\mu=0$
   * axiom of choice of set theory
6. measurable map: let $(X_1,\mathcal{F}_1)$ and $(X_2,\mathcal{F}_2)$ be measurable space, $f:X_1\to X_2$ is measurable if $f^{-1}(A)\in\mathcal{F}_1$ for all $A\in\mathcal{F}_2$
   * characteristic function: given two measurable space $(X,\mathbb{F})$ and $(\mathbb{R},B(\mathbb{R}))$, $\chi_A:X\to\mathbb{R}$ for $A\in\mathbb{F}$, $\chi_A(x)=1$ if $x\in A$ otherwise $0$
   * composition of measurable map is measurable
   * let $(X,\mathbb{F})$, $(\mathbb{R},B(\mathbb{R}))$ be measurable space, let $f,g: X\to\mathbb{R}$ measurable function
     * $f+g,f-g,|f|$ measurable
7. simple functions, step functions, staircase functions
8. Lebesgue integral
   * $f:X\to[0,\infty)$ measurable
   * $\int_X fd\mu$
   * $\mu$-integrable
   * prop
     * $f=g$ equal almost everywhere with respect to $\mu$ ($\mu$-ae), then $I(f)=I(g)$. or say $\{x:f(x)\ne g(x)\}$ is of measure zero
     * monotinicity: $f\le g$ $\mu$-ae, then $I(f)\le I(g)$
     * $f=0$ $\mu$-ae, iff $I(f)=0$