# quantum computation

## qiskit

1. classical probability
   * probability tree

## qiskit quantum machine learning

1. type of QML
   * CC: classical data, classical computers, quantum-inspired algorithm, such as recommendation system
   * CQ: classical data, quantum machine learning algorithm
   * QC: quantum data, classical machine learning algirhtm, such as qubit characterization, control and readout
   * QQ: quantum data, quantum machine learing algorithm
2. QC type QML
   * qRAM-based QML algorithm: qPCA, qSVM, qClustering
   * not qRAM-based QML algorithm
3. parameterized quantum circuits (PQC), parameterized trial states, variational forms, ansatzes
4. the measures of expressibility and entangling capability to discriminate between different PQCs
5. Meyer-Wallach measure [arxiv-link](https://arxiv.org/abs/1905.10876)
   * entangling capability of a parameterized quantum circuit
   * *TODO* how to calculate MW measure
6. [arxiv-link](https://arxiv.org/abs/2003.09887)
   * a strong correlation between classification accuracy and expressibility
   * a weak correlation between classification accuracy and entangling capability
7. hardware: limited qubit connectivity, coherence time, and gate fidelityies,
   * hardware efficiency circuit [arxiv-link](https://arxiv.org/abs/1704.05018)
8. data encoding, data embedding, data loading, a dataset consisting of $N$ data points $x^{(i)},i=1,2,\cdots,M$, with each data of length $N$
   * basic encoding: encode the whole dataset into one state vector *strange*
   * amplitude encoding: requires $log_2(NM)$
   * angle encoding, dense angle encoding
   * arbitrary encoding
9. feature map
   * `EfficientSU2`
   * `NLocal`
   * `TwoLocal`
   * `ZZFeatureMap`
   * `PauliFeatureMap` [arxiv-link](https://arxiv.org/abs/1804.11326), when $k=2,P_0=Z,P_1=ZZ$, it becomes `ZZFeatureMap`
10. optimization algorithm: evolutionary, gradient-free methods
    * gradient-based: (vanilla) gradient descent
11. gradient
    * finite difference: volatile on noisy functions
    * parameter shift rule (exact formula): stable
    * quantum Fisher information (quantum natural gradient) [arxiv-link](https://arxiv.org/abs/1909.02108): $g_{ij}=\Re \left[ \langle \frac{\partial \psi}{\partial \theta _i}|\frac{\partial \psi}{\partial \theta _j}\rangle -\langle \frac{\partial \psi}{\partial \theta _i}|\psi \rangle \langle \psi |\frac{\partial \psi}{\partial \theta _j}\rangle \right]$
    * simultaneous perturbation stochastic approximation (SPSA)
    * quantum natrual gradient with SPSA
    * exponentially decreasing learning rate
12. limitation: exponentially vanishing gradients (barren plateaus)
    * layerwise training (comment by zhangc: almost useless)
13. supervised learning: classification and regression
14. quantum variational classification: quantum feature map $|\Psi \left( x_i,\theta \right) \rangle =W\left( \theta \right) |\Phi \left( x_i \right) \rangle$
    * variational eigensolver, quantum approximate optimization algorithm, variational quantum classifier
    * parity function
15. quantum kernel estimation $K(x^{(i)},x^{( j)}) =| \langle \phi ^{( i)}\left|\phi ^{( j)}\rangle \right|^2$
    * kernel alignment: quantum feature maps can have variational parameters which can be optimizaed using the kernel alignment technique
    * quantum kernel support vector classification algorithm
    * adhoc dataset [arxiv-link](https://arxiv.org/abs/1804.11326)
    * support vectors: the nearest training data points to the separating hyperplane in each class
    * [arxiv-link](https://arxiv.org/abs/1803.07128) [arxiv-link](https://arxiv.org/abs/2010.02174) [arxiv-link](https://arxiv.org/abs/2011.01938) [arxiv-link](https://arxiv.org/abs/2001.03622)
16. unsupervised learning
    * application: high-resolution visual, composing music
    * principal component analysis (PCA)
    * clustering
    * variational autoencoders (VAE)
    * generative adversarial networks (GAN)
17. GAN
    * generator: latent space, noise vector
    * discreminator: receive data from both the generator and real distribution
    * Nash equilibrium (from game theory), zero-sum game
    * adversarial training
18. quantum GAN
    * [arxiv-link](https://arxiv.org/abs/1804.08641), [arxiv-link](https://arxiv.org/abs/1804.09139), [arxiv-link](https://arxiv.org/abs/1904.00043)
    * generative model vs predictive model
    * typess of QGAN [arxiv-link](https://arxiv.org/abs/1901.00848)
    * most of the hyperparameters chosen in QML are still driven by loose heuristics
    * equip the variational quantum generator with a latent space to allow to model continuous distributions [arxiv-link](https://arxiv.org/abs/1901.00848)
19. QGAN potential application
    * sampling and manipulation of classically intractable probability distribution
    * efficient approximate data loading [qiskit-tutorial](https://qiskit.org/documentation/stable/0.24/tutorials/machine_learning/04_qgans_for_loading_random_distributions.html) [qiskit-tutorial](https://qiskit.org/documentation/finance/tutorials/10_qgan_option_pricing.html)
20. project
    * quantum conditional GAN
    * data-reuploading classifier [link](https://quantum-journal.org/papers/q-2020-02-06-226/pdf/) [link](https://journals.aps.org/pra/pdf/10.1103/PhysRevA.104.012405)
    * QGAN mnist [arxiv-link](https://arxiv.org/abs/2012.03924)

## qiskit textbook

1. circuit diagram, gates
2. global phase, relative phase
3. Bloch vector
4. RAM model, Turing machine, digital computer, analog computer
5. Q-sphere
6. phase kickback
7. Fault-tolerant schemes typically perform these rotations using multiple application of H and T gate

raw idea

1. quantum gradient descent
2. H/T gate QECC
