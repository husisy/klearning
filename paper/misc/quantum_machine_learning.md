# quantum machine learning

Parameterized quantum circuits as machine learning models [iopscience](https://iopscience.iop.org/article/10.1088/2058-9565/ab4eb5)

1. QC中的measurement repitition还未实现
2. encoder的选择
   * qubit encoding [PRA2018](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.98.032309) [arxiv2019](https://arxiv.org/abs/1901.11434)
   * random linear map, QNN, [arxiv1904](https://arxiv.org/abs/1904.04767) [arxiv1806](https://arxiv.org/abs/1806.08321)
   * amplitude encoding [PRL2014](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.113.130503)
   * quantum feature space [nature2019](https://www.nature.com/articles/s41586-019-0980-2)
3. variational circuit design
   * 根据硬件连通性 [PRA2018](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.98.062324)
   * tree tensor network (TTN), multi-scale entanglement renormalization ansatz (MERA)
4. variation circuit主要难点
   * gate are unitary and linear
   * 没法获取中间状态，而backpropagation需要存储中间状态
5. 计算导数的方法
   * 有限差分
   * Spall's simultaneoous perturbation stochastic approximation (SPSA)：用随机数来批量估计梯度
   * 加减`pi/2`
   * 额外的qubit再加上indirect measurement，甚至可以得到高阶导数
     * 控制门太复杂
     * 要求高coherence
     * 可以导出`pi/2`方法
6. unitary gate保证梯度不会爆炸，但是量子线路的梯度会出现平台
   * Levy's lemma, concentration of measure：一个依赖于非常多独立随机变量的随机变量就是个常数 [wiki](https://en.wikipedia.org/wiki/Concentration_of_measure)
   * iniitialization来缓解 [arxiv1903](https://arxiv.org/abs/1903.05076)
