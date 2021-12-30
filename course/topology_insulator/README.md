# Topological insulator

1. link
   * kwant [gitlab](https://gitlab.kwant-project.org/kwant/kwant) [official-site](https://kwant-project.org/)

## Topology in Condensed Matter: Tying Quantum Knots

1. link
   * [edx-course](https://courses.edx.org/courses/course-v1:DelftX+TOPOCMx+1T2016/course/)
   * [official-site](https://topocondmat.org/)
   * [github](https://github.com/topocm/topocm_content)
2. topological insulator reviews
   * [The Quantum Spin Hall Effect: Theory and Experiment](https://arxiv.org/abs/0801.0901)
   * [Topological Insulators](https://arxiv.org/abs/1002.3895)
   * [Topological insulators and superconductors](https://arxiv.org/abs/1008.2026)
3. Majorana fermion reviews
   * [Search for Majorana fermions in superconductors](https://arxiv.org/abs/1112.1950)
   * [New directions in the pursuit of Majorana fermions in solid state systems](https://arxiv.org/abs/1202.1293)
   * [Introduction to topological superconductivity and Majorana fermions](https://arxiv.org/abs/1206.1736)
   * [Random-matrix theory of Majorana fermions and topological superconductors](https://arxiv.org/abs/1407.2131)
4. Fractional particles and topological quantum computation review
   * [Non-Abelian Anyons and Topological Quantum Computation](https://arxiv.org/abs/0707.1889)
   * [Anyons and the quantum Hall effect - a pedagogical review](https://arxiv.org/abs/0711.4697)
   * [Majorana Qubits](https://arxiv.org/abs/1404.0897)
5. Extra review
   * [Floquet topological insulators](https://arxiv.org/abs/1211.5623)
   * [Topological Crystalline Insulators and Topological Superconductors: From Concepts to Materials](https://arxiv.org/abs/1501.00531)

### chap1 topology in toy models

1. presence or absence of particles with zero excitation energy
2. topology and symmetry
3. lead, barrier, quantum dot
4. topologically equivalent: Hamiltonians can be continuously deformed into each other without ever closing the energy gap
5. topological invariant, the zeroth Chern number: the number of negative eigenvalue
6. topological phase transition
7. unitary symmetry (conservation law): reduce the dimension of the problem
8. time reversal symmetry
   * spinless: $T=UK$ anti-unitary operator
   * spin 1/2 time reversal: $T=i\sigma_yK$, Kramers'degeneracy
9. sublattice symmetry: graphene
   * $\sigma_z H \sigma_z=-H$
   * if $(\phi_A, \phi_B)$ is an eigenvector of the Hamiltonian with energy $E$, then $(\phi_A, -\phi_B)$ is an eigenvector with energy $-E$
10. particle-hole symmetry
    * cooper pairs
    * $H = H_{ij}c_i^\dagger c_j + \frac{1}{2}\Delta_{ij}c_i^\dagger c_j^\dagger + \frac{1}{2}\Delta_{ij}^{*} c_j c_i$
    * $\Delta_{ij}=-\Delta_{ji}$
    * the Bogoliubov-de Gennes Hamiltonian
    * antiunitary operator $P=\sigma_xK$
    * $PH_{BdG}P^{-1}=-H_{BdG}$
    * Fermion parity switches
    * the Pfaffian invariant
11. bulk edge correspondance
12. Majorana operators, unpaired Majorana mode
13. Kitaev chain model
    * k-space, particle-hole symmetry in k-space
14. domain wall

## chap2

1. topological superconductors
2. fractional particles
3. 3D topological insulator, 2D topological insulator
4. semiconductor: low electron density
5. $\mu\to \mu-2t$, $\mu\ll t$, $\Delta\ll t$
6. s-wave pairing: no momentum dependence, `Al,Nb,Pb,Sn`, spin-singlet
7. p-wave pairing: Kitaev chain
8. d-wave or a more exotic $s\pm$ wave: high temperature superconductor, cuprates, pnictides
9. BdG hamiltonian, two basis
   * particle-hole symmetry $H=-\tau_x H^*\tau_x$
   * apply time-reversal symmetry to the holes: s-wave pairing is a unit matrix
10. Majoranas are their own particle-hole partners, and that means that they cannot have any spin (energy, charge, or any other observable property at all)
11. spin-orbit interaction $\alpha \sigma_y k$: invariant under time reversal symmetry (both $\sigma_y$ and $k$ change sign)
12. parameters
    * chemical potential $\mu$: the ovverall electron density
    * induced superconducting gap $\Delta$: particle-hole symmetry
    * spin-orbit coupling $\alpha$: break spin conservation
    * Zeeman field $B$: break kramers degeneracy
13. ferromagnetic atomic chains on superconductor
14. edges of topological insulator in proximity to superconductor
15. zero bias peak: Majorana? others?

how to detect Majoranas

1. topological superconductivity
2. 4-pi periodic Josephson effect, Majorana zero mode, resonant conduction
3. Joosephson junction: superconducting ring, phase difference, flux, excitation spectrum
   * Josephson current: the expectation value of the derivative of the energy operator $I(\Phi)=\frac{1}{2}\frac{dE_{tot}}{d\Phi}$
   * absence of the reservior of electrons
   * fermion parity swith/conservation
   * superconducting phase
4. Andreew reflection
   * normal metal, superconductor interface (NS interface)
   * barrier, energy gap iin superconductor $eV<\Delta$
   * normal and Andreew reflection
   * double barrier transmission, resonant peak
5. topological invariant $Q=det(r_0)=\pm 1$
   * either perfect normal reflection, perfect Andreev reflection
6. tight binding models in a magnetic field: Peierls substitution
7. superconducting flux quantum $\Phi_0=2e/h$
8. electron poisoning, quasiparticle poisoning
   * to avoid electron poisoning, one should quickly tune the phase
   * if too quick, electron may tunnel through a gap, Landau-Zener tunneling

braiding of Majoranas

1. non-Abelian statistics, anyons: Majorana zero modes
2. quantum statistics is not really well-defined in one-dimension
