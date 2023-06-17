# quantum money

## cryptography

misc

1. link
   * [wiki/category/cryptography](https://en.wikipedia.org/wiki/Category:Cryptography)
2. abbreviation
   * PPT: probabilistic polynomial-time
   * QPT: quantum polynomial-time
   * iO: indistinguishable obfuscation
   * PRG: pseudorandom generator
   * PRF: pseudorandom function
   * CSPRG: cryptographically secure pseudorandom generator
   * MAC: message authentication code
   * CCA: chosen ciphertext attack
   * CPA: chosen plaintext attack
   * iO: indistinguishability obfuscation
3. default math symbol (maybe overwriten by local context)
   * $\mathbb{Z}_p^n=(\mathbb{Z}/p\mathbb{Z})^{\otimes n}$
   * $U_k$: uniform distribution over $\mathbb{Z}_2^k$
   * $x\leftarrow_r P$: $x$ is a random variable from distribution $P$
4. open problem
   * do one-way functions exist? [wiki-link](https://en.wikipedia.org/wiki/One-way_function)
5. computational hardness assumption [wiki-link](https://en.wikipedia.org/wiki/Category:Computational_hardness_assumptions)
   * Diffie-Hellman asumption
   * integer factorization
   * lattice problem
   * ring learning with errors
   * etc.
6. cryptography primitive [wiki-link](https://en.wikipedia.org/wiki/Cryptographic_primitive)
   * one-way hash function: SHA-256
   * symmetric key cryptography: AES
   * public key cryptography: RSA
   * digital signature
   * mix network
   * private information retrieval
   * commitment scheme
   * CSPRG
7. if one-way function exists, then
   * one-way permutation exists (Feistel network)
   * PRG
   * PRF
   * MAC
   * digital signature scheme
   * private-key encryption schemes secure against adaptive CCA
8. NP problem
   * tensor network: optimal order of contraction

Definition

1. negligible, noticeable, overwhelming, function $f:\mathbb{Z}^+\mapsto\mathbb{R} [0,1]$
   * negligible: $\forall c\in\mathbb{Z}^+$, there exists $n_c\in\mathbb{Z}$, such that $\forall n>n_c,f(n)<n^{-c}$
   * noticeable: $\exists c\in\mathbb{Z}^+,n_c\in\mathbb{Z}^+$, such that $\forall n>n_c,f(n)\geq n^{-c}$
2. PRG $G:\mathbb{Z}_2^l\mapsto \mathbb{Z}_2^n,l<n$ [wiki-link](https://en.wikipedia.org/wiki/Pseudorandom_generator)
   * seed length $l$, the stretch of the PRG $n-l$
   * $A$: statistical tests
   * statistical distance between $A(G(U_l))$ and $A(U_n)$ is negligible
3. PRF $f_s: \mathbb{Z}_2^{|x|}\mapsto\mathbb{Z}_2^{\lambda_{|x|}}$ [wiki-link](https://en.wikipedia.org/wiki/Pseudorandom_function_family)
   * $f_s(x)$ is PPT
   * $\mathrm{F}_n$: distribution of function $\left\{f_s: s\leftarrow_r U_n\right\}$
   * $\mathrm{RF}$: uniform distribution over the set of  all function from $\mathbb{Z}_2^{|x|}$ to $\mathbb{Z}_2^{\lambda_{|x|}}$
   * $\mathrm{F}_n$ and $\mathrm{RF}_n$ are PPT indistinguishable
4. one-way function $f_c:\mathbb{Z}_2^n\mapsto\mathbb{Z}_2^m$ [wiki-link](https://en.wikipedia.org/wiki/One-way_function)
   * $f_c$ can be computed PPT
   * any PPT algorithm $F$ to inverse $f_c$ succeeds with negligible probability
   * $\mathrm{Pr}[f_c(F(f_c(x)))=f_c(x)]<n^{-c}$ with the probability taken over the choice of $x\leftarrow_r\mathbb{Z}_2^n$ and the random coins of $F$
5. one-way permutation: bijective one-way function
6. trapdoor one-wary function (permutation) $(f=\mathrm{Enc}:D_k\mapsto R_k,\mathrm{Gen},\mathrm{Dec})$
   * $(k,t_k)\leftarrow_r\mathrm{Gen}$ is PPT, public key $k$, trapdoor $t_k$
   * $x\leftarrow_r D_k$ can be PPT sampled
   * $y=\mathrm{Dec}(k,f_k(x),t_k)$ is PPT such that $f_k(y)=f_k(x)$
   * For any PPT algorithm $F$, the probability to invert $f_k$ is negligible
   * example: RSA, discrete log, Rabin's quadratic residue
7. collision-free hash function: the probability to find a **distinct** value such that $f(x)=f(y)$ is negligible
   * example: SHA-256
   * kinds [stackexchange-link](https://crypto.stackexchange.com/a/80463)
     * preimage resistant (first preimage resistant)
     * second preimage resistant (weakly collision free)
     * collision resistant (strongly collision free)
     * indistinguishable from a PRF
8. $\mathrm{iO}$ is called an indistinguishability obfuscator if
   * completeness (functionality): for all boolean function (circuit) $f:\mathbb{Z}_2^n\mapsto \mathbb{Z}_2^m$, the random sampled function $g\leftarrow_r \mathrm{iO}[f]$ satisfy $\forall x\in\mathbb{Z}_2^n,g(x)=f(x)$
   * indistinguishability: every pair of circuits $f_0,f_1$ of the same size $k$ that implement the same functionality, for all statistical tests $A$, statistical distance between $A(\mathrm{iO}[f_0])$ and $A(\mathrm{iO}[f_1])$ is negligible
   * [wiki-link](https://en.wikipedia.org/wiki/Indistinguishability_obfuscation)
   * [github/obfusc8](https://github.com/tum-i4/indistinguishability-obfuscation)
   * can construct most cryptography primitives (exception: collision-resistant hash function)

## lattice crypto

lattice and hard lattice problem

1. reference
   * Joseph H. Silverman [homepage](http://www.math.brown.edu/johsilve/) [youtube-link](https://youtu.be/j30GwMRXWek) [lecture-book](https://www.ias.edu/sites/default/files/Silverman_PCMI_Note_DistributionVersion_220705.pdf)
   * 知乎-稀有气体 [link](https://zhuanlan.zhihu.com/p/161411204)
   * unimodular matrix [wiki](https://en.wikipedia.org/wiki/Unimodular_matrix)
2. lattice history
   * 1982 LLL basis reduction theorem
   * 1996 Ajtai-Dwork, average-case, worst-case complexity, lattice-based one-way functions, lattice-based collision-resistant hash functions
   * 2005 Regev, Quantum resistant, public-key encryption
3. lattice: discrete additive subgroup
   * $L=\langle v_1,v_2,\cdots,v_m\rangle _\mathbb{Z}=\left\{\sum_{i=1}^n a_iv_i:a_i\in\mathbb{Z},v_i\in\mathbb{R}^n\right\}\subset\mathbb{R}^n$
   * lattice of maximal rank (non-maximal rank lattice is not covered here)
   * basis $B=\left\{v_1,v_2,\cdots,v_n\right\}$
   * fundamental domain: $F(B)=\mathbb{R}^n/L=\left\{\sum_{i=1}^n t_iv_i:t_i\in[0,1) \right\}$
   * the absolute determinant (volume) of $L$ is $\mathrm{det}(L)=\mathrm{volume}(F(B))=|det(v_1|v_2|\cdots |v_n)|$
   * density
   * the first minimum $\lambda_1=\min_{x\in L\setminus\left\{0\right\}}\lVert x \rVert$
   * the k'th successive minimum $\lambda_k=\inf\left\{\lambda>0:\mathrm{dimSpan}\left\{v\in L:\lVert v\rVert\leq\lambda\right\}\geq k\right\}$
   * Parallelepiped
4. fundamental hard lattice problems
   * shortest vector problem (SVP): find shortest nonzero vector in $L$
   * closest vector problem (CVP): given a target vector $t\in\mathbb{R}^n$, find a vector in $L$ that is closest to $t$
   * approximate shortest vector problem (apprSVP)
   * approximate closest vector problem (apprCVP)
   * shortest independent vectors problem (SIVP)
   * bounded distance decoding (BDD)
   * absolute distance decoding (ADD)
5. geometry of numbers
6. hadamard's inequality: $\mathrm{det}(L)\leq \prod_{i=1}^n\|v_i\|$
7. Minkowski theorem: for all lattice $L\subset\mathbb{R}^n$, Hermite's constant $\gamma_n=\frac{4}{\pi}\Gamma(\frac{1}{2}n+1)^{2/n}\approx \frac{2n}{\pi e}$, there exists a bases $B=\left\{v_1,v_2,\cdots,v_n\right\}$
   * $1\leq k\leq n$, $\prod_{i=1}^{k} \lVert v_i\rVert \leq \gamma_n^{k/2} \mathrm{det}(L)^{k/n}$
   * the exact value of $\gamma_n$ is known only for $n\leq 8$ and $n=24$
8. lattice point lemma (minkowski): let lattice $L\in\mathbb{R}^n$, then every compact convex symmetric region $R$ of volume at least $2^n\mathrm{det}(L)$ contains a nonzero lattice point
   * compact: closed and bounded
   * convex: $v,w\in R$, then line segment $\bar{vw}\subset R$
   * symmetric: $x\in R$, then $-x\in R$
9. Minkowski's theorem part a:
