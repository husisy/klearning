# zcnote

梯度反向传播求解优化问题

优点：提速`N`倍，N是参数个数

缺点：对内存有要求

1. 容易处理的约束
   * 非负：`x>=0`, `x=relu(y)`
   * 半正定：`A>0`, `A=exp(B)` B厄米
   * 厄米: `A=A^dag`, `A=B+B^dag`
   * 幺正: `A A^dag=I`, `A=exp(i B)` B厄米
   * unit p-norm: `norm(v)=1`, `v=u/norm(u)`
2. 极难处理的约束
   * 等式约束`Ax=b`，给定`x`和`b`优化`A`
   * `PPT>0`
   * 交换对称性Boson/Fermion
   * transition matrix, doubly stochastic matrix
3. 什么操作是可导的
   * `1-norm`: yes
   * `bbox`: yes
   * indexing: no
   * sort: no
4. BFGS hard
   * the i-th eigenvalue
5. loss landscape
   * sum of L1-loss is a disaster
   * boundary of separable state is hard
6. how to select optimizer
   * BFGS：参数量大约少于`1000`，不能处理随机batch的情形
   * L-BFGS-B：不能处理随机batch的情形，不能处理separable state的边界（大量的切平面交）
   * Adam/SGD: 存在random batch
7. 存在凸优化容易而非线性优化困难的问题
8. 凸优化可以和梯度优化结合：cvxpylayer
