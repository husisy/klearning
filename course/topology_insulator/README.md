# Topological insulator

1. link
   * kwant [gitlab](https://gitlab.kwant-project.org/kwant/kwant) [kwant-official-site](https://kwant-project.org/)
   * [readthedocs/topological-insulator](https://topological-insulators.readthedocs.io/en/latest/index.html)
   * [github/topins](https://github.com/oroszl/topins)
   * [blog/guanjihuan](https://www.guanjihuan.com/archives/18572)
   * [scholarpedia/topological-insulators](http://www.scholarpedia.org/article/Topological_insulators)
2. seminar
   * [quantum290](https://math290.com/)

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
    * $H_{BdG}=\frac{1}{2}[[H,\Delta],[-\Delta^*,-H^*]]$, the factor $\frac{1}{2}$ is omitted mostly
    * Particle-hole symmetry, antiunitary operator $P=\sigma_xK$, $PH_{BdG}P^{-1}=-H_{BdG}$
    * conserve the parity of the number of electrons: even or odd
    * Fermion parity switches
    * the Pfaffian invariant: antisymmetric matrices (even dimension)
    * $A=\frac{1}{\sqrt{2}}[[1,1],[i,-i]]$, $\tilde{H}_{BdG}=AH_{BdG}A^\dagger$: antisymmetric, pure-imaginary, hermitian
11. bulk edge correspondance
12. Majorana operators, unpaired Majorana mode
13. Kitaev chain model
    * k-space, particle-hole symmetry in k-space
14. domain wall
15. bulk topological invariant

## chap2 Majoranas I

1. concept
   * topological superconductors
   * fractional particles
   * 3D topological insulator
   * 2D topological insulator
2. semiconductor: low electron density
3. $\mu\to \mu-2t$, $\mu\ll t$, $\Delta\ll t$
4. s-wave pairing: no momentum dependence, `Al,Nb,Pb,Sn`, spin-singlet
5. p-wave pairing: Kitaev chain
6. d-wave or a more exotic $s\pm$ wave: high temperature superconductor, cuprates, pnictides
7. BdG hamiltonian, two basis
   * particle-hole symmetry $H=-\tau_x H^*\tau_x$
   * apply time-reversal symmetry to the holes: s-wave pairing is a unit matrix
8. Majoranas are their own particle-hole partners, and that means that they cannot have any spin (energy, charge, or any other observable property at all)
9. spin-orbit interaction $\alpha \sigma_y k$: invariant under time reversal symmetry (both $\sigma_y$ and $k$ change sign)
10. parameters
    * chemical potential $\mu$: the ovverall electron density
    * induced superconducting gap $\Delta$: particle-hole symmetry
    * spin-orbit coupling $\alpha$: break spin conservation
    * Zeeman field $B$: break kramers degeneracy
11. ferromagnetic atomic chains on superconductor
12. edges of topological insulator in proximity to superconductor
13. zero bias peak: Majorana? others?

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

1. non-Abelian statistics, anyons, braiding: Majorana zero modes
2. quantum statistics is not really well-defined in one-dimension
3. T-shaped nanowire network
4. ground state manifold
5. fermion parity operator
6. basic definition
   * $(\gamma_1\gamma_2)(\gamma_3\gamma_4)=(\gamma_3\gamma_4)(\gamma_1\gamma_2)$
   * $(\gamma_1\gamma_2)(\gamma_2\gamma_3)=-(\gamma_2\gamma_3)(\gamma_1\gamma_2)$
   * $(\gamma_i\gamma_j)^2=-1$
   * $\gamma_i^2=1$
   * $U=exp(\pi\gamma_i\gamma_j/4)$
7. linear combinations of states with different total parity are forbidden
8. the network of nanowires drawn in the figures only allows to exchange neighbouring Majoranas
9. quantum computing [arxiv-9708022](https://arxiv.org/abs/quant-ph/9708022)

## chap3 more parameters: charge pumping

1. parameter: confining potential, magnetic flux
2. Thouless pump (quantum pumps)
   * phase: geometrical, dynamical, topological
3. periodicity of time evolution, the space of parameter values is compact
4. the number of charges pumped in an adiabatic pumping cycle is an integer (possibly 0), independent of the strength $A$, as long as the wire (the bulk of the pump) is gapped
5. Chern number, TKNN number
6. $dq=\frac{d\log(\det(r))}{2\pi i}=Tr\frac{r^\dagger dr}{2\pi i}$

quantum Hall effect

1. quantum Hall effect
   * integer quantum Hall effect
   * fractional quantum Hall effect
2. quantum conductivity $\frac{e^2}{h}$
   * Hall resistivity, longitudinal resistivity
3. temperature dependence $exp(-T_0/T)$, gapped state
4. annular geometry
5. Hall current is special in that it is dissipationless. any system with a Hall effect must somehow break time-reversal symmetry
6. Hall bar (2D)
   * current density $j$
   * electric field $E$
   * $j_\alpha=\sigma_{\alpha\beta}E_\beta$
   * conductivity tensor $\sigma_{\alpha\beta}$
   * resistivity tensor $\rho_{\alpha\beta}$
   * $\alpha\beta\in\{x,y\}$
   * rotational invariance: $\sigma_{xx}=\sigma_{yy}=\sigma_L$, $\sigma_{xy}=-\sigma_{yx}=\sigma_H$
7. classical Hall effect
   * Streda relation: $\sigma_H=\frac{ne}{B}$
   * filling factor $\nu=\frac{nh}{eB}$, $\sigma_H=\nu\frac{e^2}{h}$
   * when the density $n$ is high, $\sigma_H$ scales linearly with gate voltage. when the density $n$ is low, due to the disorder/interactions, $\sigma_H$ varies sample to sample
8. no real difference between conductance and conductivity in 2D: same physical units
9. quantum Hall effect
   * $\sigma_H$ apears to form plateaus at integer filling factors. The longitudinal resistivity apears to vanish except at the transition points between plateaus
   * Numerical systems are so good that the longitudinal conductivity always stays low even at the transition
10. Laughlin argument
    * Lauphlin pumps
    * Corbino disk, Corbino geometry
    * flux quantum $\Phi_0=\frac{h}{e}$
    * Hall cylinder
11. Landau levels
    * classical electrons $r_c=\frac{mv}{eB}$, angular momentum $L=mvr_c=eBr_c^2$
    * quantized $L=n\hbar$, $r_c=\sqrt{n}l_B$, magnetic length $l_B=\sqrt{\hbar/eB}$
    * angular frequency $\omega_c=eB/m$
    * Landau level $E=L\omega_c=(n+\frac{1}{2})\hbar\omega_c$
    * huge degeneracy, proportional to the area of the sample
12. the nonzero longitudinal conducitivity
    * when stop turning the flux on, the accumulated charge relaxes and energy is dissipated in the bulk
    * the closure of the bulk energy gap at the transition of the integer

$$
j_x = \sigma_L E_x + \sigma_H E_y\\
j_y = \sigma_L E_y - \sigma_H E_x\\
\sigma_L = \frac{j_x E_x + j_y E_y}{E_x^2+E_y^2} = \frac{j_xE_x}{E_x^2+E_y^2}\\
\sigma_H = \frac{j_x E_y - j_y E_x}{E_x^2+E_y^2} = \frac{j_xE_y}{E_x^2+E_y^2}
$$

edge state

1. chiral edge states
   * skipping orbits
   * confining electrostatic potential
   * $E=\hbar v(k-k_F)$, $k_F=2\pi N/L$, the number of electrons in the system $N$, **WHY**
   * local electric field $\varepsilon_y=-\partial_y V$
   * drift velocity of the skipping state $v=\varepsilon_y/B$
   * the edge state closer to the edge, its drift velocity is faster, because the local electric field there is stronger
2. local density of states
3. chiral anomaly
