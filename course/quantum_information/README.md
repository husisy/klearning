# quantum information

Reinhard Werner

[youtube-link](https://www.youtube.com/watch?v=vb0ZEsATUcw&feature=share&si=ELPmzJkDCLju2KnD5oyZMQ)

* Lecture 1: Hilbert spaces, scalar product, bra, ket, operators
* Lecture 2: operators, diagonalization, functional calculus, qubit, composite systems, and the tensor product
* Lecture 3: composition, tensor product, channels, Heisenberg picture, Schrödinger picture, complete positivity, channel examples: unitary, depolarizing, von Neumann measurement
Lecutre 4: state space, probabilites, composition, the positive cone, positivity, and the geometry of cones
* Lecture 5: extremal points, pure states
extremal observables, POVMs, and effect operators
* Lecture 6: extremal observables, the Choi-Jamiokowski isomorphism, Kraus operators, and symmetries of the positive cone
* Lecture 7: symmetries of the positive cone
Wigner's theorem, anti unitary operators, symmetry groups, one-parameter groups, and irreducible representations
* Lecture 8: how to construct a Hilbert space, positive kernel, kolmogorov dilation, completion, Naimark dilation, going to the larger Hilbert space, and Stinespring dilation
* Lecture 9: the Stinespring dilation Theorem and proof, Example: Naimark dilation, GNS representation, comparison theorem
* Lecture 10: corollaries for the Stinespring dilation Theorem
* Lecture 11: instruments, statistical structure, Choi isomorphism and channels, classical models, and Bell correlations
* Lecture 12: entanglement
* Lecture 13: tasks and resources
* Lecture 14: quantum teleportation and dense coding 1
* Lecture 15: quantum teleportation and dense coding 2
* Lecture 16: norms and fidelities
* Lecture 17: some semidefinite tasks in QI
* Lecture 18: noisy resources and conversion rates

## Pauli group and Clifford group

Pauli Group

1. link
   * [wiki/pauli-group](https://en.wikipedia.org/wiki/Pauli_group)
   * [github/qiskit-tutorial/clifford-group](https://github.com/qiskit-community/qiskit-community-tutorials/blob/master/terra/qis_adv/Clifford_Group.ipynb)
   * [wiki/clifford-gates](https://en.wikipedia.org/wiki/Clifford_gates)
2. basic knowledge
   * Pauli group $P_n=\left\{ e^{i\theta\pi/2}\sigma_{j_1}\otimes \cdots\sigma_{j_n} : \theta,j_k\in\mathbb{F}_4 \right\}$
   * $P_1=\left\{\pm I, \pm iI, \pm X, \pm iX, \pm Y, \pm iY, \pm Z, \pm iZ\right\}=\langle X,Y,Z\rangle$
   * $P_n=\left\{ \pm x, \pm ix : x\in \left\{IXYZ\right\}^{\otimes n}\right\}=\langle X_i,Y_i,Z_i:i=1,2,\cdots,n \rangle$
   * $|P_n|=4^{n+1}$
   * $P_1 \simeq C_4 \circ D_4$ central product of a cylclic group of order $4$ and the dihedral group of order $8$
   * center: $Z(P_n)=\left\{I,-I,iI,-iI\right\}$
   * $P_n/Z(P_n)\cong (\mathbb{F}_2^{2n},+)$
3. 定义记号 $\sigma(a,b)=X^aZ^b,a\in\mathbb{F}_2^{n},b\in\mathbb{F}_2^{n}$
   * $\sigma(a_1,b_1) \sigma(a_2,b_2)=(-1)^{b_1\cdot a_2}\sigma(a_1+a_2,b_1+b_2)$

Clifford group

1. link
   * [wiki/clifford-gates](https://en.wikipedia.org/wiki/Clifford_gates)
   * Harrow Aram, Clifford group [link](https://web.mit.edu/8.371/www/lectures/lect06.pdf)
   * the classification of clifford gates over qubits [quantum-journal-link](https://quantum-journal.org/papers/q-2022-06-13-734/)
   * Maris Ozols, Clifford group, [homepage-link](http://home.lu.lv/~sd20008/papers/essays/Clifford%20group%20%5Bpaper%5D.pdf)
   * how to efficiently select an arbitrary clifford group element [arxiv-link](https://arxiv.org/abs/1406.2170)
   * Maris Ozols, Clifford group from scratch [link](http://home.lu.lv/~sd20008/papers/essays/Clifford%20group%20[presentation].pdf)
2. basic
   * Clifford group $Cl_n=\left\{ x\in U(2^n) : xP_nx^\dagger=P_n \right\}/U(1)$
   * order $|Cl_1|=24,|Cl_2|=11520,|Cl_3|=92,897,280,|Cl_4|=12128668876800$, $|Cl_5|=25410822678459187200$
   * symplectic group on $\mathbb{F}_2$: $Sp(2n,\mathbb{F}_2)=\left\{ x\in\mathbb{F}_2^{2n\times 2n}: x\Lambda x^T=\Lambda \right\}$, $\Lambda=\sigma_x\otimes I_n$
   * $Cl_n/P_n\cong Sp(2n,\mathbb{F}_2)$
   * $Cl_1$: group of rotational symetries of the cube
   * generator $Cl_n=\langle H_i,S_i,\mathrm{CNOT}_{ij} \rangle/U(1)$, Hadamard $H$, S-gate $S=diag\{1,i\}$

TODO

1. [wiki/Gamma-group](https://en.wikipedia.org/wiki/Higher-dimensional_gamma_matrices)
2. graph states and graph codes [link](https://quantum.phys.cmu.edu/QCQI/qitd452.pdf)
3. package
   * [github/pyclifford](https://github.com/hongyehu/PyClifford)
   * [github/juqst.jl](https://github.com/rharper2/Juqst.jl)
   * [github/python-quaec](https://github.com/cgranade/python-quaec)
   * [github/abp](https://github.com/peteshadbolt/abp)

no idea

1. [github/clifford](https://github.com/pygae/clifford) clifford algebra
