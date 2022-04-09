# Coursera Quantum Computations

[caltech-John-Preskill](http://theory.caltech.edu/~preskill/ph219/index.html#lecture)

[UNLV-quantum-computing-mma](https://www.physics.unlv.edu/~bernard/MATH_book/Chap9/chap9_link.html)

## QML

1. link
   * [gitlab/QML-mooc](https://gitlab.com/qosf/qml-mooc/-/tree/master)

## topological quantum computer

1. link
   * [wiki/topological-quantum-computer](https://en.wikipedia.org/wiki/Topological_quantum_computer)
   * [youtube/caltech/topological-quantum-computing](https://youtu.be/qj-w6ISQL5Y)
   * Delft-course/topological-materical
   * web-of-science review paper
   * arxiv introduction and newest paper
2. arxiv link
   * [link0](https://arxiv.org/abs/2111.00355)
   * [link1](https://arxiv.org/pdf/1802.06176.pdf)
   * [link2](https://arxiv.org/abs/1705.04103)

## coursera00

1. [coursera - The Introduction to Quantum Computing](https://www.coursera.org/learn/quantum-computing-algorithms)
2. course material
   * John Preskill's lecture notes on quantum computing
   * Umesh Vazirani's lectures on quantum computing
   * Popular science books of David Deutsch
3. computation: a physical process, finite in time, fixed set of states
4. information: fixed set of distinguishable states
5. quantity of information (Cloude Shannon): $I=-\sum_iP_i\log_b(P_i)$

## coursera01

introduction to quantum information, KAIST

1. preparation, transmission, detection, interpretation
2. quantum communication, quantum computing, quantum information
3. Hilbert space: vector space with inner product
4. state, dynamics, measurement, observables
   * POVM: positive operator valued measure
   * dynamics: unitary, pauli matrix, Hadamard
5. computational basis
6. Hadamard, hadamard basis
7. universality
8. mixed state
9. quantum state discrimination
   * Helstrom Measurement
   * [wiki](https://en.wikipedia.org/wiki/Quantum_state_discrimination)
   * minimum error discrimination
   * unambiguous discrimination
   * paper
10. No-go theorem
    * no-cloning theorem: [paper](https://www.nature.com/articles/299802a0) A single quantum cannot be cloned

week3

1. entangled and product state
   * LOCC: local operation, classical communication
   * Schmidt decomposition (SVD decomposition)
2. qubit gate
3. joint measurement and individual measurement
   * convert $\phi^+$ measurement to $00$ measurement
4. post selection
   * partial trace
5. quantum teleportation, protocol
   * one-time pad
   * Bell measurement

week4

1. qubit gate: CNOT
   * Clifford `S=sqrt(Z)=P(pi/2)`, Clifford group `{H,CX,S}`
   * `Z=P(pi)`
   * Toffoli gate `T=sqrt(S)=P(pi/4)`
2. Grover algorithm
   * `H^n (000)` generate super-position of all computation basis
   * quantum amplitude amplification
   * unsorted items (databases)
   * `O(N)`, `O(sqrt(N))`
3. Shor, quantum prime number factorization algorithm
   * quantum Fourier transformation, `n` qubits need `n**2` gates, classically need `n*(2**n)` operation (FFT)
4. Deutsch algorith, David Deutsch
   * constant or balanced
   * phase kickback
   * ancilla
   * unitary (channel) discrimination
5. phase estimation
   * modular exponentiation

week5

1. quantum channel, reduction of unitary matrix
   * subsystem
   * Kraus operator
   * POVM
2. isometry
3. depolarization channel `D[rho]=I/2`
4. quantum teleportation as quantum channel
   * preserve positivity
   * trace preserving (TP)
   * completely positive (CP)
5. Choi–Jamiołkowski isomorphism [wiki](https://en.wikipedia.org/wiki/Choi%E2%80%93Jamio%C5%82kowski_isomorphism)
6. bit flip channel
7. quantum channel is monogamous

week6

1. entanglement
   * entanglement swap
2. entanglement manipulation
3. maximum entangled state
4. single-copy entanglement manipulation, entanglement manipulation
5. typical sequence
6. Schmidt coefficient
7. twirling
8. quantum steering
9. quantum nonlocality
10. quantum error correction code

TODO

1. experiment with IBMQ `H-P(a)-H`

## MIT-OCW 8.370

week1

1. concept
   * unit1: circuits, reversible circuit, quantum state (vector), quantum evolution (matrix), measurement, tensor product, quantum weirdness
   * unit2: quantum protocol and algorithm, teleportation, factoring, Grover search
   * unit3: noise, code, QECC (), application
   * unit4: model of quantum computation, measurement, distributed quantum algorithm, quantum adiabatic algorithm
2. historical development
   * models classical computation: finite automaton, turing machine, lambda calculus, circuit (super-universal)
   * 1936 Turing universal computation
   * circuit are only designed for specific finite size input (12-bit circuit not good for 10-bit task)
   * uncomputable task on Turing machine: whether input i halts, can be solved by family of circuits model
3. circuit model
4. quantum mechanics
   * 1900-1930 development
   * 1936 Einstein, Podolski, Rosen said QM is incomplete
   * 1964 Bell, no classical explanation for the the behavior EPR
   * 198? Aspect's experiments
   * 1982 Herbert, FLASH, First Laser-Amplified Superluminal Hookup, faster than speed of light (wrong)
   * 1982 no-cloning theorem: a single unkown quantum state cannot be duplicated
   * 1982 Feymann, Manin, diffcult to simulate quantum mechanics, QC might be faster
   * 1985 David Deutsch, quantum Turing machine
   * 1992 Deutsch-Josza, QC good at some classicial problem
   * 1993 Bernstein, Vazirani
   * 1993 Simon, exponentially faster on QC, periodicity
   * 1994 factoring and discrete log
   * 1995 Lov Grover, search algorithm
5. classical fault tolerance
   * checkpointing, the Little Hammer and the Big Hammer
   * error correcting code
   * massive redundancy
6. conceptual models of classical computation
   * mechanics: abacus, difference engine差分机, differential analyzer, curta calculators科塔计算器, electrical circuit
   * conceptual models: Turing machine, probablistic TM, Universal TM, Minsky machine, cellular automata, Von Neumann, DNA-based
7. Universality, classical
   * and, not
   * fanout
   * crossover
   * `2**(2**n)` distinct `n`-input boolean circuit
8. complexity
   * Strong Church-Turing thesis: any model of computation can be simulated on a specific kind of machine
9. decision problem, Entscheidungsproblem
   * Rabin's primality testing algorithm
   * factoring: given a composite integer `m` and an integer `l (l<m)`, does `m` have a nontrival factor which is less than `l`
   * witness, verifier
   * 3-SAT
   * P, NP, co-NP, NP-complete, BQP
10. thermodynamics and computation
    * Maxwells Daemon: energy requiredto move the door? measurement? need for intelligence?
    * 1929 Szilard's engine: getting rid of randomness (erasing the memory) takes work
    * 1961 Rolf Landauer, n-bit register has `2**n` configuration, clearing register to go to a final state cost energy $kT\log_e(2)$ per bit
    * exorcism of Maxwell's daemon
    * modern computers consume something like `500kT log(2)` joules per bit erased. DNA computer roughly `120 kT log(2)` joules per operation
11. reversible computing
    * `and` gate is irreversible
    * 1982 Fredkin, Toffoli, Billiard ball model, susceptible to small imperfections that cause cascading errors (primary issue)
12. reversible gates
    * CNOT: exclusive or, addition modulo 2
    * Toffoli gate: universal
    * Fredkin gate: universal
    * theorem: the amount of garbage needed to reversibly simulate any boolean if of the order of the width of the circuit, not the depth
    * theorem: any boolean circuit of `n` gates can be simulated by a reversible circuit of order of polynomial in `n` reversible gates, approximately as `n**2`
    * [arxiv1504.05155](https://arxiv.org/abs/1504.05155) The Classification of Reversible Bit Operations
    * Toffoli gate can make Fredkin gate

Charles Bennett: information is quantum [link](https://www.youtube.com/watch?v=EqXv40kCahM&t=76s)

week2 quantum mechanics

1. vector space, complex field
2. gate, `X,Y,Z,S^2=Z,T^2=S`
3. unitary matrix
4. Copenhagen interpretation of quantum mechanics, Niels Bohr
5. measurements
   * orthogonal vectors are distinguishable
   * Von Neumann measurement
6. tensor product
7. n-qubits has `2**n-2` freedom: 1 for normalization, 1 for global phase
8. seperable state, entangled state
9. no-cloning theorem
   * proof: unitary transform preserve inner product, otherwise `x=x**2`
10. FANOUT: `0->(0,0)`, `1->(1,1)`
11. identity
    * `HXH=Z`
    * backaction: `CNOT(2,1)= HH CNOT(1,2) HH`
    * `CZ(0,1)=CZ(1,0)`
12. measurement
    * hermitian matrix
    * non-negative eigenvalue
    * Von Neumann measurements is not POVM
13. statement: square matrix always has one eigenvector over complex field
14. Bell state
    * all are entangled state
    * spin expectation is zero in any direction

week3

1. quantum weirdness
2. 1935 EPR, Einstein, Podolski, Rosen, QM is incomplete
3. CHSH game
4. Mermin magic square game
   * any entry in same row/column commutes
   * the product of all entries in one row/column is `I/-I`
   * mark `red` if measure `-1`, green if `1`
   * (Alice/Bob) the number of red in one row/column will be even/odd
   * classical strategy: win probability is `8/9`
   * with two bell states: win probability is `1`

```bash
XI, IX, XX
IZ, ZI, ZZ
-XZ, -ZX, YY
```

week4

1. quantum protocol
2. historical development
   * Asher Peres, Bill Wootters, Mercedes Benz' states
   * history of quantum teleportation [IBM](https://researcher.watson.ibm.com/researcher/view_group.php?id=2862)
3. teleportation
   * bell state measurement
   * measurement can always move to last step
4. superdense coding
   * send one qubits, pass 2 bits information
5. message, transmission, entanglement
   * teleportation: 1 qubit, 2 cbits, 1 EPR
   * superdense coding: 2 cbits, 1 qubit, 1 EPR
6. optimality of superdense coding and teleportation
   * missed.....
   * Holevo's theorem
7. Vaidman bomb detection
   * interferometer

```txt
phi+ = 00 + 11
phi- = 00 - 11
psi+ = 01 + 10
psi- = 01 - 10
```

teleportation circuit

```txt
012: zeta + 0
cnot(1,2)
cnot(0,1)
cnot(1,2)
cnot(2,0)
012: 0 + zeta
```

week5 quantum algorithm

1. Deutsch-Jozsa algorithm
   * 1980s, Richard Feynman, Yuri Manin, simulate quantum mechanics using QC
   * 1985 David Deutsch, Quantum Turing Machine
2. Deutsch-Jozsa algorithm
   * `log(n)` bit function, `f` is a constant or balanced function
   * promise function
   * oracle: classical oracle, quantum oracle, phase oracle, xor oracle
   * xor oracle can turn into a phase oracle
   * if `f` is not constant/balanced function, the probablity of `0000` will be `0` or `1`
   * `H^n 0000` is all bit string with equal amplitude
3. classical algorithm
   * `n/2+1`
   * randomized algorithm `2 - n/2+1`, expectation query is `3`
4. classical computer
   * NAND is universal
   * fanout (copy) is take for free
   * CMOS: NAND, NOR, NOT
5. QC
   * all two-qubits gate are universal
   * CNOT, all 1-qubit gate are universal
   * better: CNOT, H, X, Y, Z, T, S. get arbitrary close to any gate, Solovay-Kitaev theorem
   * with Toffoli gate, any permutation gate can be build
   * two-level gates
   * X gate can be create from CNOT
   * Toffoli can be create from H, T, CNOT
   * CNOT can be create from Toffoli
6. Simon's algorithm
   * `f(x)=f(x+c)`, one-to-one or two-to-one
   * classical random query time: expectation `2**(n/2+1)` for `n` bits
   * quantum oracle function: `(x,y)->(x,y+f(x))`
   * linear algebra over finite fields (binary numbers)
   * converge probablity `1/sqrt(e)`
   * Gaussian elimination
   * always check `f(0)=f(c)`

week6 quantum Fourier Transform (QFT)

1. Simon's algorithm is the FT over $Z_2^{\otimes n}$ group
2. QFT
   * for `n`-qubit circuit, need roughly `n` single-qubit gates (Hadamard and swap), `n**2` double-qubits gates
   * `R_k=diag{1,exp(-2j*pi/2**k)}`
   * cutoff
3. Cooley-Tukey FFT (classical)
4. quantum factor algorithm
   * 1970s Rivest, Shamir, Adelman, public key crypotosystem based on factoring
5. order finding problem
   * `f=f(x+c)`, function over integer $\mathcal{Z}$ not $\mathcal{Z}_2$, find periodic in time `O(log(c)**2)`
6. classical algorithm (see @book-QCQI)
   * quadratic Sieve algorithm
   * Euclidean algorithm
   * continued fraction algorithm: converged, overestimate and underestimate alternatively
   * repeated squaring
7. reduce factoring to order finding
   * when go wrong: order is odd
   * probability to sucess is larger than `0.5` for a random pick `y`
   * longhand multiplication
   * modular exponentiation
8. quantum algorithm for periodicity
9. phase estimation
   * discrete log
   * Kitaev algorithm for factoring, unitary `(x)->(gx (mod N))`

Order finding algorithm measurement result as a geometric sum **LOST**

gate reduction

1. `cphase(a,b)=cphase(b,a)`

number theory

1. fundamental thoerem of arithmetic $a=p_1^{a_1}p_2^{a_2}\cdot p_n^{a_n}$
2. ordinary arithmetic, modular arithmetic
3. greatest common divisor (gcd): Euclidean algorithm
   * representation theorem: `min(abs(ax+by))=gcd(a,b))`, the gcd of two integers `a` and `b` is the least positive integer that can be written in the form `ax+by`
   * if `c|a` and `c|b`, then `c|gcd(a,b)`
   * if `a|b` and `b|a`, then `a=b`
4. multiplicative inverse `ab=1 (mod n)`, $a^{-1}$
   * co-primality: integers `a` and `b` are co-prime if their gcd is `1`
   * an integer `a` has a multiplicative inverse modulo `n` if and only if `gcd(a,n)=1`
   * unique if exist
5. let `a` and `b` be integers, and let `r` be the remainder when `a` is devided by `b`, if `r!=0` then `gcd(a,b)=gcd(b,r)`
6. Euclidean algorithm
   * gcd
   * multiplicative inverse
7. Chinese remainder theorem
8. Fermat's little theorem
9. Euler phi function $\phi(n)$: the number of positive integers less than `n` which are co-prime to `n`
10. order-finding problem: let `N` positive integer, `x` is co-prime to `N`, `1<=x<N`, the order of `x` modulo `N` is defined to be the least positive integer `r` such that `x**r=1(mod N)`

week7 Grover's quantum search algorithm

1. historical
   * 1995 @paper a fast QM algoirhtm for the database
   * quantum memory
   * `x**4 + y**4 + z**4 = w**4`
   * `414560**4 + 217519**4 + 95800**4 = 422481**4`
2. Grover algorihtm
   * phase oracle
   * Grover step: apply oracle $x\to(-1)^{\delta_{x\beta}}x$, $H^{\otimes n}$, apply $x\to -(-1)^{\delta_{x0}}x$, $H^{\otimes n}$
   * `pi*sqrt(N)/4` step. `sin(theta/2)=1/sqrt(N)`
   * `1` solution in `N` items, faster with `M` solutions; if `M` is large, no need to use Grover algorithm, just random pick one
   * assumption: the number of solution is exactly known
3. nitrogen fixation `N2 + 3H2 = 2NH3`
4. 1911 Haber-Bosch process, metal catalyst
5. bacteria enzyme, nitrogenase
   * iron molybdenum complex, `FeMoCo`
6. quantum simulation
   * generate goal Hamiltonian from QC Hamiltonian
   * analog deformation
   * what to measure: precision issue
   * quantum-inspired simulation: density matrix renormalization group (DMRG), PEPS, MERA
7. Lie product formula, Trotterization, Trotter-Suzuki formula
8. simulation of Grover's algorithm
   * Hamiltonian
9. [@paper2016](https://arxiv.org/abs/1605.03590) elucidating reation mechan isms on quantum computers
10. Trotter expansion, simplectic integrators
11. quantum chemistry, VQE
    * phase estimation: ground state, required long coherence time
    * variational quantum eigensolver
12. Jordan-Wigner transformation, Bravyi-Kitaev transformation

week8 error correction

1. history
   * determine longitude: three chronometers (take majority)
   * 1948 Shannon information theory, capacity
   * 1950 Hamming code
2. binary symmetric channel
   * binary: two inputs and two outputs `0,1`
   * symmetric: readout error matrix is symmetry
3. capacity of a channel
   * `0.9/0.1` with capacity `0.531` bit per channel bits
   * block encoding
4. Hamming code `(7,4)`
   * linear code, generating matrix
   * message, parity check
   * codeword length `7`, data bits `4`
   * Hamming weight: number of `1`
   * Hamming distance
   * fact: the minimum Hamming weight of a non-zero codeword not equal to zero is `3`
   * Hamming code correct `1` error
   * syndrome
   * (useful for quantum Hamming code) the dual code of Hamming code is a subset of Hamming code
5. general linear code `GH=0`
6. dual code, self-dual
7. noisy quantum state
   * density matrix
   * ensemble of quantum state
8. project measurement
9. density matrix
   * ensemble of quantum states
   * throw away half of a pure state
   * bloch sphere
10. partial trace on A measures A in canonical basis get a probability distribution of pure state of B
11. 环 [wiki](https://zh.wikipedia.org/wiki/%E7%8E%AF_(%E4%BB%A3%E6%95%B0))

coding theory

1. link
   * [wiki/linear-code](https://en.wikipedia.org/wiki/Linear_code)
   * [wiki/Hamming-code](https://en.wikipedia.org/wiki/Hamming_code)

week9 quantum channel

1. probability mixture of simple channel
2. dephasing channel
   * $(1-p)\rho + p\sigma_z\rho\sigma_z$
   * shrink the bloch sphere
3. deplorizing channel
   * $(1-3p)\rho + p\sigma_x\rho\sigma_x + p\sigma_y\rho\sigma_y + p\sigma_z\rho\sigma_z$
   * $(1-4p)\rho+2pI$
   * $A+\sigma_x A\sigma_x + \sigma_y A\sigma_y + \sigma_z A\sigma_z=2I$
4. quantum version of repitition code, 3 qubit bit error correction
   * $\alpha |0\rangle + \beta|1\rangle \to \alpha |000\rangle + \beta|111\rangle$
5. quantum channel: positive space-preserving maps
6. bit flip error $\sigma_x$
   * error correct: measure which bit is different
7. 3-qubit bit-flip code
8. theorem: if you can correct $\sigma_x,\sigma_y,\sigma_z$ error on any single qubit, than you can correct any one-qubit error
9. classical `[n,k,d]` code: a set of $2^k$ $n-$bit string with minimum Hamming distance $d$
   * Hamming weight $w(x)$: number of `1` in $x$
   * Hamming distance $d(x,y)=w(x\oplus y)$, bitwise xor
   * example: linear code
10. analog signals don't really have error correction
11. 1995 three major objections to the existence of quantum error correction
    * states collapse when measured
    * errors are continuuous
    * no-cloning threm, qubit states cannot be copied
    * (after QEC is found) no way to make it resilient against failures in gates (fault tolerance)
12. strategies for QEC
    * never measure states, only measure the effect of the environments (error)
    * orthogonalize errors using entanglement (@paper how to fight entanglement with entanglement)
13. quantum code `[[n,k]]`: a $k-$qubit subspace of an $n-$qubit Hilbert space
14. degenerate code and non-degenerate code
15. operator measurement
16. syndrome: a pattern of measurement results
    * parity-check matrix
17. bit-flip channel and bit-flip code
    * codeword: $|0\rangle$ to $|000\rangle$, $|1\rangle$ to $|111\rangle$
    * syndrome operators: $Z_1 Z_2$, $Z_2 Z_3$
    * recovery operators: $X$
18. independent and identically distributed channel (no memory in channel)
19. phase flip code
    * codeword: $|0\rangle$ to $|+++\rangle$, $|1\rangle$ to $|---\rangle$
    * syndrome operators: $X_1 X_2$, $X_2 X_3$
    * recovery operator: $Z$
20. Shor's 9-qubit code
    * codeword: $|0\rangle$ to $\frac{(|000\rangle+|111\rangle)^{\otimes 3}}{\sqrt{8}}$, $|1\rangle$ to $\frac{(|000\rangle-|111\rangle)^{\otimes 3}}{\sqrt{8}}$
    * syndrome operators: $Z_1 Z_2$, $Z_4 Z_5$, $Z_7 Z_8$, $Z_2 Z_3$, $Z_5 Z_6$, $Z_8 Z_9$, $X_1 X_2 X_3 X_4 X_5 X_6$, $X_4 X_5 X_6 X_7 X_8 X_9$
21. quantum error correction criteria, Manny Knill, Raymond Laflamme
22. Kraus operator $\sum_k{E_k\rho E_k^\dagger}$, $\sum E_k^\dagger E_k=I$
23. projective measurement
24. phase damping and phase flip are equivalent (see exercise)

week10 quantum key distribution, Quantum Cryptography

1. @paper brief history of quantum cryptography, a bpersonal perspective, Gilles Brassard
2. history
   * RSA
   * 1984 BB84 Charles Bennett, Brassard
3. one-time pad
4. Ekert-Chau-Lo entanglement based QKD protocol
5. (lost)
6. CSS code
7. Ekert91
8. conjugate code
9. quantum money, quantum banknote

week11 distributed quantum computation

1. communication complexity
   * upper bound
2. disjointness problem
3. distributed Deutsch-Jozsa problem
   * oracle: lookup table
   * classical algorithm can decide probably in `O(log(n))` time
   * classical algorithm can decide determinately in `O(n)` time
   * quantum algorithm can decide determinately in `O(log(n))` time
4. (lost)

## MIT-OCW 8.371

[website](https://web.mit.edu/8.371/www/index.html)

week1

Aram Harrow

1. classical information: bit
   * RAM, magnetic tape, abacus
2. quantum information: qubit
   * spin, photon, electron level, superconductor
3. 8.370 content
   * basic of quantum information
   * quantum algorithm
   * quantum error correction
   * model of computation: adiabatic model, measurement-based model
4. 8.371 content
   * noise
   * error correction
   * fault tolerant quantum computing
   * quantum complexitty theory: some very near-term quantum circuits cannot be simulated
   * quantum algorithm: quantum walks, Hamiltonian simulation, linear system of equation
   * quantum information theory
5. quantum state, operation, ensemble, density matrix, observable
6. density matrix $\rho$: $tr(\rho)=1,\rho\geq0$, positive semidefinite (PSD)
   * hermitian
   * non-negative eigenvalues; non-negative expectation; $\rho=A^\dagger A$
   * no phase
   * $\rho = \frac{1}{2}(I+a_i\sigma_i), |a|\leq 1$
7. Bloch ball/sphere
   * maximally mixed state
8. operation
   * classical
     * deterministic: $f:{1,2,\cdots}\to{1,2,\cdots,d}$, could destroy information
     * random: transition (stochastic) matrix, Markov process $p=pT$, $\sum_i{T_{ij}}=1$, $T_{ij}\geq 0$, could destroy information
   * quantum
     * deterministic: unitary matrix
     * random: quantum operation, random unitaries
   * quantum operation: unitary operation, random substitution of $|0\rangle\langle 0|$, projective measurement, measurement of two of three qubits, etc.

| - | deterministic | random |
| :-: | :-: | :-: |
| classical | ${1,2,\cdots,d}$ | $p \in \mathcal{R}^d, \sum_x{p_x}=1, p_x\geq 0$ |
| quantum | $\mid \phi \rangle\in \mathcal{C}^d,\langle \phi \mid \phi \rangle=1$ | density matrix |

stochastic matrix

1. alias: probability matrix, transition matrix, substitution matrix, Markov matrix
2. kind
   * right stochastic matrix $P1=1$, $\sum_j{P_{ij}}=1$ (mainly focus on this one)
   * left stochastic matrix $1P=1$
   * doubly stochastic matrix $P1=1, 1P=1$
3. property
   * $P_1P_2$ is still a stochastic matrix
   * eigenvector, stationary probability vector $\pi$, $p\pi=\pi$
   * all eigenvalues of a stochastic matrix have absolute values less than or equal to one
   * one trival eigenvector $1$ with eigenvalue $1$
4. left eigenvalue and right eigevalue for a square matrix is same

quantum computing

1. density matrix
   * ensemble of quantum states
   * throw away half of a pure state

week2

1. Schrondinger equation says physics dynamics is unitary (closed system)
2. add/drop system: tensor product, partial trace
3. vector space, super-operator
4. defition-1 of quantum operation, Stinespring representation
   * (Stinespring's dilation theorem) composition of unitaries, adding sys, partial trace
   * isometry: preserve length
   * isometry include: unitaries, adding sys
   * isometry is a group
   * any quantum operation can be written as an isometry, then partial trace
   * partial trace can always be delayed
   * the Church of the larger Hilbert space
5. Kraus operator representation
6. example
   * unitary
   * random unitary
   * partial trace
   * QC initialize operation (no mixture of unitary): $|0\rangle\langle 0|$
   * depolarizing
   * amplitude damping (no mixture of unitary)
7. TPCP representation (axiomatic approach): trace perserving completely positive map
   * linear Hermiticity perserving
   * trace preserving
   * positivity: $\rho\geq 0 \to N(\rho)\geq 0$
   * completely positivity: $\rho\geq 0 \to (N\otimes \text{id})(\rho)\geq 0$
   * example of positive but not compltely positive: transpose on part of system
8. measurements
   * quantum operation: quantum state to probability distribution
   * $N(\rho)=\sum_{x=1}{p_x|x\rangle \langle x|}$
   * $p_x=\mathrm{tr}\left[ \rho M_x \right]$
   * $M_x\geq 0$
   * $\sum_x{M_x}=I$
9. generalized measurement
   * non-demolition measurement
   * relation between measurement and Kraus operator
10. norms
    * homogeneous
    * triangle inequality
    * seperating
    * L1-norm: probability distribution
    * L2-norm (Euclidean norm): pure state
11. Schatten p-norm: `L_p(svd(A))`
    * S1-norm: density matrix
    * S-infinite: measurement
    * S1-norm for PSD matrix: `trace(A)`
12. duality: given norm `f(x)` on a vector space, can define dual norm $g(x)=\max_{f(y)\leq 1} |(x,y)|$
    * L2-norm is dual to L2-norm
    * L1-norm and L-infinity are dual
    * same as Schatten norm
13. trace norm: metric on the set of states
    * $T(\rho,\sigma)=\frac{1}{2}S_1(\rho-\sigma)$, value between $[0,1]$
14. Choi-Jamiołkowski state

week3

1. classical codes `[n,k,d]`: encoding, noise, decoding
   * codeword: the length of codeword set is `2**k`, the length of each codeword is `n`, the minimum distance `d`
   * `decode(x)`: the nearest codeword
   * Hamming distance: `distance(x,y)=L_1(x,y)` for n-bit string
   * error-correcting performance: code distance, minimum distance between all pairs of codewords
2. classical code, n-bit repitition code
   * decoding: take majority
   * correct `(n-1)/2` bits flip error
   * Chernoff bound [wiki](https://en.wikipedia.org/wiki/Chernoff_bound)
3. classical `[n,k,d]` can correct up to `(d-1)/2` errors, and detect up to `d-1` errors
4. finite field $F_2$ [wiki](https://en.wikipedia.org/wiki/Finite_field)
   * $F_2^n$: mod-2 arithmetic
5. classical linear code
6. (lost-note)
7. McEliece cryptosystem [wiki](https://en.wikipedia.org/wiki/McEliece_cryptosystem)
8. the space of errors corrected is a linear space
9. low-weight errors
   * typical choice of error set $S={\text{errors on up to } l=\frac{d-1}{2} \text{ qubits}}$
10. QEC condition
11. concatenated QEC code

week4 stablizer code

1. pauli group
2. stabilizer group
3. stabilizer subspace
4. every stabilizer cuts down the dimension by a half
5. simplectic inner product
6. normalizable subgroup `N(S)`: undetectable error
7. `[[5,1,3]]` qubit code
   * correct 1 error or 2 erasure error
8. `[[n,k,d]]`
   * stabler group `n-k`
   * normalizer `N(S)`, `n+k`
   * logical operators, `2k`
9. trival code
10. code transformation
11. Clifford group: $\text{Cl}_n=\{U: UP_nU^\dag=P_n\}$ where $P_n$ is Pauli Group [wiki](https://en.wikipedia.org/wiki/Pauli_group)
    * $P_n\subset \text{Cl}_n$
    * $\text{Cl}_n$: $\langle X Z H S \text{SWAP} \text{CNOT} \rangle$
    * $SXS^\dag=XZ$
    * $T=\sqrt(S)$ not a member
12. symplectic inner product
13. symplectic group $M$
14. maximum likelihood decoding
    * NP-complete in the worst case
15. CSS codes
16. iterative decoding (LTPC code)
17. Gottesman-Knill theorem, Clliford circuits

week5 fault-tolerant quantum computation

1. 1941 Shannon communication channel compacity: channel + noise
2. 1956 von Neumann, gates + noise
3. the threshold theorem: a (uniform) circuit of $N$ error-free gates can be simulated with probablity $<\epsilon$, using $O(\text{Poly}(log\frac{N}{\epsilon})N)$ gates, which fail with some probability $p$ provided $p<p_{\text{th}}$, where $p_{\text{th}}$ is independent of $N$ and $\epsilon$
4. recursive construction
5. classical circuits
   * 1950 von Neumann: $p_{\text{th}}\geq 0.073$, 3-input
   * 1991 Hajck, Weller: $p_{\text{th}}\geq 0.167$, 3-input
   * 1998 Evans, Piinger: $p_{\text{th}}\geq 0.089$, 2-input
   * 2008 Evans, Piinger: $p_{\text{th}}< \frac{1}{2}-\frac{1}{2\sqrt{k}}$, $k$-input
6. fault tolerant (FT) procedure
7. transversal gates
8. Calderbank-Shor-Steane (CSS) code
   * `[[7,1,3]]`
   * logical operation: $X_L=X^{\otimes 7}$, $Z_L=Z^{\otimes 7}$, $H_L=H^{\otimes 7}$
   * CNOT is transversal
   * every CSS code has a transversal CNOT
   * every code with a transversal CNOT is a CSS code
9. 2007: no stabilizer code has a universal set of transversal gates
   * stabilizer code is analogy to classical linear code
10. FT estimate for QC: `1/3081=3.2e-4`
