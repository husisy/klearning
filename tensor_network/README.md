# tensor network

1. resource
   * tensors.net [link](https://www.tensors.net/)
   * tensornetwork.org [link](https://tensornetwork.org/)

## 张量网络前沿选讲

1. link
   * @paper A Practical Introduction to Tensor Networks: Matrix Product States and Projected Entangled Pair States [link](https://arxiv.org/abs/1306.2164v3)
   * [tensor-network-initiative](https://perimeterinstitute.ca/tensor-networks-initiative)
   * [youtube/European-tensor-network](https://www.youtube.com/channel/UCYCOGWQN5ZBT96b-WEBI9pQ/videos)
   * [google-blog/tensornetwork](https://ai.googleblog.com/2019/06/introducing-tensornetwork-open-source.html), [github](https://github.com/google/TensorNetwork)
   * [arxiv-link0](http://arxiv.org/abs/1407.6552), [arxiv-link1](http://arxiv.org/abs/1603.03039), [arxiv-link2](http://arxiv.org/abs/1008.3477), [arxiv-link3](http://arxiv.org/abs/1812.04011), [arxiv-link4](http://arxiv.org/abs/2011.12127)
   * [bilibili/首都师范大学-冉仕举-张量网络基础介绍](https://www.bilibili.com/video/BV17z411i7yM)
   * [前沿关注](http://quattro.phys.sci.kobe-u.ac.jp/dmrg/condmat.html)
2. outline
   * 传统张量网络基础
   * 张量网络新领域应用
   * 专题选讲（经典综述，重要方法，新进展）
   * coding and revisit

### 20210914 传统张量网络基础

1. 课程slide不分享
2. notation
   * scale, vector, matrix, rank-3 tensor
   * internal line, external line
3. tensor network: MPS, PEPS, TTN, MERA
4. @paper(2012) PRB.80.155131 [link](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.80.155131)
5. 弱关联（金属，半导体），强关联（高温超导体）
6. (lost)
7. Hilbert space of a N-body many-body system
8. 面积定理area law: 两部分之间的纠缠熵
9. map state to tensornetwork
   * exact constructing: Kitaev's Toric code (star operator, plaquette operator), 2d Ising model (partition function)
   * tensor decomposition: SVD, @paper(2011) SIAM-J.Sci.Comput.33.2295
   * variational ansatz
10. typical workflow
    * choose a wave function ansatz
    * determine the wave function
    * evaluate physical observable
    * choose an TN structure
    * determine the value of tensors
    * contract the TN
11. challenge
    * determine the value of tensor
    * contracting tensor network
    * projection, variational, coarse graining
    * TEBD, TRG, loop-TNR
12. 1D TN
    * imagenary time evolution: time evolution block decimation (TEBD)
    * energy minimization: density matrix renormalization (DMRG)
13. DMRG
    * the original view: numerical RG: blocks which have renormalizaed Hamiltonians and operator-matrices in that basis
    * MPS variational state point of view
    * 最大限度保留纠缠熵
14. MPS
    * canonical forms
    * any state can be represented as MPS
    * hierarchical: matrix size related to degree of entanglement
    * renormalization groups
15. 2D TN
    * entanglement entropy
    * area-law in 2D
    * PEPS(bond=4)的表达能力可以大于MPS(bond=4000)
16. determine the TN value
    * imaginary time evolution: simple/cluster/full/fast-full update
      * fast-full: @paper(2015) PRB.92.035142, 可以进一步和机器学习结合？
    * energy minimization
      * DMRG-like sweeping, @paper(2016) PRB.94
      * CG-approach: @paper(2016) PRB.94
17. contract TN
    * MPS-based: transfer matrix, boundary-MPS（破坏了二维结构的对称性，行列不同）
    * corner tranfer matrix method
    * Tensor Renormalization Group (TRG)
    * tensor network renormalization (TNR) @paper(2015) PRL.115
18. direction of improvement for 2D TN
    * parallelization: quantum computing
    * symmetries
    * Monte Carlo sampling
    * improve extrapolations, finite-D scaling analysis
    * better optimization, contraction algorithm
    * combinations, variational wavefunctions, fixed node MC
19. 其他：environment optimization, RG flow, symmetric TN (gauge freedom) Corner double line, continuous TN, TN fermionisation, thermal system, dynamic system, manifold and TDVP, sign problem, quantum gravity duality (AdS/CFT), quantum computing simulator, quantum machine learning

TODO

1. page31 an wave function, a wave function

## 20210916 张量网络与机器学习

1. (lost)
2. ML四要素：数据、模型、评价函数、优化算法
3. ML+TN
   * arxiv1301.31124
   * arxiv1410.3831
4. arxiv1605.05775把图片编码为MPS，用DMRG来优化
   * 理解：TN和ML都是高维空间函数拟合
   * TN：量子多体，对称性，局域性，面积率
   * ML：多项式参数，神经网络
   * 图片的样本空间是整个空间一个非常小的角落（随机样本是噪音点）
   * arxiv1608.08225
5. mnist对应的互信息的理论上界是396bit
   * 张量网络可以容易的应用到该数据集
   * 神经网络有显著的冗余
   * 《物理杂志》：量子纠缠：从量子物质到深度学习
6. compressing neural network weight layers using TN
7. tensor structure in ML
   * tensor machine learning
   * tensor networks machine learning
8. PEPS - > markov random field, condditional random field
9. 受限玻尔兹曼机和MPS对应 @paper-PRB.97.xxx
10. NN与Tree tensor network对应，copy tensor
11. @paper-PRL.2019 Yoav Leving
    * 神经网络表达能力的上界
12. 小结
    * 机器学习模型的全连接结构有冗余
    * MNIST数据集有稀疏的长程关联
    * TN和图模型有对偶关系，因子图是两者相同之处
13. 张量网络机器学习模型
14. discriminant model of tensor networks
15. supervised learning with PEPS, @paper-arxiv2020-Chen
16. (lost)
17. 张量网络作为生成模型 Born machine
    * PRX1709.01662
    * 直接算出配分函数
    * adaptive learning：参数可动态改变
18. PRB.99.155131, generative model based on tree tensor network
    * capture longer-range correlation than MPS model
    * pixel-pixel correlation
19. 生成模型
    * adaptive learning
    * unbiased learning
    * direct samping
    * two-dimensional hierachical structure
    * barren plateaus in TN based mearning learning, arxiv.2108.08312
20. 张量网络机器学习模型的发展
    * 模型压缩
    * 新训练方法
    * 概率建模
    * 表达能力理论分析

TODO, page98 为什么说PEPS对应CRF呢？

## 张量网络Python编程

terminoligy

1. tensor
   * order n tensor
   * n-way tensor
   * n-dimensional array

chapter 1

1. link
   * [doi-link](https://doi.org/10.1007/978-3-030-34489-4) tensor network contraction ShijuRan
   * [bilibili-link](https://www.bilibili.com/video/BV1AP4y1R75h/)
2. concept
   * index
   * order
   * scalar
   * vectorization
   * Canonical polyadic decomposition (CPD)
   * singular value decomposition
3. python programming trick
   * indexing
   * slice
   * [numpy-link](https://numpy.org/doc/stable/user/basics.indexing.html)
   * Ex: how to create order $n$ identity tensor
4. diagram representation
5. matrix product state $\sum_{\left\{ a_{*}\right\} }I_{a_{0}a_{N}}\prod_{n\in[N]}A_{a_{n}s_{n}a_{n+1}}^{(n)}$
6. tensor norm
   * L-p norm
   * Frobenius norm
7. best rank one approximation of tensor
   * alternating least squares method: local minimum, stationary point, non-increasing at each step
8. [wiki-link](https://en.wikipedia.org/wiki/Tucker_decomposition) Tucker decomposition
   * core tensor: $G_{[n]}G_{[n]}^\dagger=\mathrm{diag}(g_0,g_1,\cdots)$ with $g_0\geq g_1\geq\cdots$
   * [wiki-link](https://en.wikipedia.org/wiki/Higher-order_singular_value_decomposition) higher-order singular value decomposition
   * Tucker rank for each leg
   * Higher Order Orthogonal Iteration (HOOI)
9. canonical polyadic decomposition

chapter 2

1. Hilbert space
2. superposition
   * basis dependent
   * coherence: defined in resource theory
3. thermal state
4. projective measurement
5. global phase factor, guage degrees of freedom
6. reduced density matrix and quantum entanglement
7. quantum fourier transformation

chapter 3 variational quantum circuit

1. reference
   * [doi-link](https://doi.org/10.1103/PhysRevA.104.042601) Automatically differentiable quantum circuit for many-qubit state preparation
2. latent gate
   * negative logarithm of fidelity
   * update layer by layer
   * Matrix Product State (MPS) ansatz: 48 qubits, 5 layer, bond dimension 64
