# Coursera Quantum Computations

[caltech-John-Preskill](http://theory.caltech.edu/~preskill/ph219/index.html#lecture)

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

## MIT-OCW

8.370

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
   * what to measure
   * quantum-inspired simulation: density matrix renormalization group (DMRG), PEPS, MERA
7. Lie product formula, Trotterization, Trotter-Suzuki formula
8. simulation of Grover's algorithm
   * Hamiltonian
