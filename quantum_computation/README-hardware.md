# Quantum Hardware

1. link
   * [edx-link](https://learning.edx.org/course/course-v1:DelftX+QTM2x+2T2023/home) the hardware of quantum computer
2. solid-state qubits
   * silicon spin qubit
   * diamond NV center qubit
   * superconducting transmon qubit
   * topological qubit

module 1

1. reference
   * [doi-link](https://dl.acm.org/doi/10.1145/2903150.2906827) A heterogeneous quantum computer architecture
2. heterogeneous multicore architecture
3. hierarchical structure
   * Q algorithm
   * programming paradigm, language
   * Q arithmetic, runtime, compiler
   * Q instruction set architecture
   * microarchitecture
   * Q to classical
   * Q chip
4. concept
   * Precision in material uniformity, chemical composition and electrical properties
   * Chemical Vapour Deposition
   * Transmission electron microscopy
5. DiVincenzo criteria

module 2 spin qubit

1. reference
   * [doi-link](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.79.1217) Spins in few-electron quantum dots
   * [doi-link](https://doi.org/10.1038/s41534-017-0038-y) Interfacing spin qubits in quantum dots and donors—hot, dense, and coherent
2. history
   * 1947 first transistor
   * 1954 first transistor radio
   * 1958 first integrated circuit
   * 1989 Intel 486 processor
3. low temperature operation
   * charging energy $E_c=\frac{e^2}{8e_re_o R}$ (Coulomb repulsion between electrons)
     * $R=10 \mathrm{nm}$, $E_c=30 \mathrm{meV}$
   * thermal energy $k_B T$
     * $T=4.2 \mathrm{K}$, $k_B T=0.35 \mathrm{meV}$
4. Coulomb blockade
5. charge sensing
   * crosstalk
   * inter-dot capacitance
6. cross bar technology
7. Charge stability diagrams
8. operation
   * initilization: Zeeman energy
   * readout: Elzerman readout
   * manipulation: Rabi osscillation
9. Zeeman energy $E_z=g\mu_B B$, assuming g-factor $g=2$, around hundreds of $\mu eV$
10. sequence to determine quantum coherent
    * Ramsey experiment
    * Hahn echo experiment
    * CPMG sequence
    * about 10 microseconds
11. 2-qubits gate
    * exchange interaction
    * tune tunnel coupling
    * control detuning
12. Using either quantum buses or coupling to photons in superconducting microwave cavities, small arrays can be coupled together

module 3 nitrogen-vacancy centers in diamond

1. reference
   * [doi-link](https://doi.org/10.1038/s41586-018-0200-5) Deterministic delivery of remote entanglement on a quantum network
   * [doi-link](https://doi.org/10.1038/nature15759) Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres
   * [doi-link](https://doi.org/10.1038/s41586-018-0200-5) Deterministic delivery of remote entanglement on a quantum network
2. substituational nitrogen atom in the diamond lattice next to a missing carbon atom (vacancy)
3. feature
   * long coherence time (even at 290 K)
   * couple to nuclear spin in the environment, giving extra qubits to store and process
   * optical interference
   * quantum network
4. setup
   * 4 K cryostat
   * micrometer sized diamond
     * gates to tune wavelength
     * solid immersion lens
     * microwave line
   * 3 level system
   * readout: laser pulse that only resonant with the spinup state
   * single-qubit gate: a wire running next to the qubit emits an AC electromagnetic field on resonance with the qubit's frequency.
   * about `1%` of diamond consists of carbon-13 (spin 1/2), rest is carbon-12 (spin 0)
   * each NV center becomes a system of 5 or more qubits
5. electron spin and nuclear spin
6. spin echo: increase coherence time from about 1 ms to 1 s
7. dipolar magnetic field of the electron spin gives a unique energy splitting to differently positioned nuclear spins, allowing selective control.

module 4 superconducting qubits, transmon qubits

1. reference
   * [doi-link](https://doi.org/10.1103/PhysRevA.76.042319) Charge-insensitive qubit design derived from the Cooper pair box
2. circuit quantum electrodynamics (circuit QED) architecture
3. manmade artificial qubits built from circuits
4. superconducting electrode, island, Josephson junction, LC oscillator
5. Hamiltonian $H=\frac{Q^2}{2C}+\frac{\Phi^2}{2L}-E_J\cos\left(\frac{2\pi\Phi}{\Phi_0}\right)$
   * $Q$ charge on the island (capacitor plate)
   * $\Phi$: magnetic flux through the inductor
   * $[\Phi,Q]=i\hbar$
   * capacitive term: localize Cooper pair
   * inductive term: tunneling
6. setup
   * variety: charge qubit (transmon), flux qubit, phase qubit, fluxonium
   * working frequency: `4-8` GHz
   * transmission line resonator
   * transmon region: energy scale of the inductive term is much larger than the capacitive term
   * feedline
   * form factor: `2mm x 7mm`
7. coil inducotr and Josephson junction
8. similar to cavity QED
   * circuit QED is solid version of cavity QED
   * cavity QED: atom and photon in a cavity
   * circuit QED: qubit, transmission line resonators
     * coplanar waveguide transmission line terminated with either open or shorted end
9. quarter-wave, $\lambda/4$ resonator
10. Jaynes-Cummings model
    * avoided crossing, vacuum Rabi splitting
    * resonant regime, dispersive regime
11. qubit readout: the ladder of photon excitations remains harmonic, but the resonance frequency depends on the qubit state
12. qubit-qubit interaction
13. coupling bus resonator to qubit
14. flux-bias control line
15. microwave drive line
16. readout resonator, feedline
17. air-bridge cross-over technology
18. surface-17
    * 17 qubits
    * 24 bus resonators
    * 17 readout resonators
    * 17 flux-bias control lines
    * 17 microwave drive lines
    * 3 feedlines
    * 40 input/output ports (vertical IO ports)
    * ball-grid array
    * each qubit (Starmon): 4 bus, 1 readout, 1 flux-bias, 1 microwave drive
    * 4 frequencies suffice to control a surface code of any size
