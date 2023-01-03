# matrix

TODO 放到`course/linear_algebra`中去

```text
matrix (svd)
├── diagonalizable 可对角矩阵
│   ├── normal 正规矩阵
│   │   ├── unitary 幺正矩阵
│   │   ├── special unitary
│   │   ├── hermitian 厄米矩阵
│   │   ├── skew-hermitian 斜厄米矩阵
│   │   └── circulant 循环矩阵
│   │   └── other
│   └── diagonalizable but unnormal 可对角但非正规矩阵
└── defective matrix
    └──Jordan norm form

matrix (svd)
├── invertible 可逆矩阵
└── non-invertible 不可逆矩阵
```

1. link
   * eigendecomposition [wiki](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix)
   * skew-hermitian matrix [wiki](https://en.wikipedia.org/wiki/Skew-Hermitian_matrix)
   * unitary matrix [wiki](https://en.wikipedia.org/wiki/Unitary_matrix)
   * special unitary matrix [wiki](https://en.wikipedia.org/wiki/Special_unitary_group)
   * singular value decomposition
   * polar decomposition
2. invertible matrix: $det(A)\ne 0$
   * `min(svd)=0`
3. 可逆矩阵和可对角化没有包含或者被包含关系
   * 可逆但不可对角化：约当矩阵Jordan matrix
   * 可对角化但不可逆：`diag{1,0}`
4. diagonalizable matrix: $A=USU^{-1}$，其中$U$可以是任何可逆矩阵，该分解称作特征值分解eigen decomposition
   * 每个特征向量有一个缩放自由度
   * 当无重根时，且每个特征向量归一化时，特征分解唯一
   * 对于重根的特征子空间内（特征值相同），特征向量可以彼此正交
   * 特征值不同的特征向量，无正交约束
5. normal matrix: $AA^\dagger=A^\dagger A$, 即$[A,A^\dagger]=0$
   * 充要条件：特征值分解$A=USU^{-1}$中的$U$是幺正矩阵，该分解称作谱分解spectral decomposition
   * 正规矩阵近似可以看做厄米矩阵和幺正矩阵的奇奇怪怪组合
   * **强调**正规矩阵对于矩阵加法不封闭
   * **强调**正规矩阵对于矩阵乘积不封闭
   * $A=U^\dag \Lambda U=U^\dag r e^{i\theta} U=U^\dag r V$, $V=e^{i\theta}U$
6. diagonalizable but unnormal matrix
   * 简单谐振子中的产生湮灭算符
   * 特征值分解$A=USU^{-1}$中的$U$不是幺正矩阵，即特征向量不正交
   * （猜想）normal matrix选取部分行部分列可以构成unnormal matrix，即其特征矢量在子空间的投影是不正交的。但并非一定unnormal matrix
   * （猜想）unnormal matrix总是可以拓展高维空间编程normal matrix，pseudo-inverse?
7. hermitian matrix: $A=A^\dagger$
   * 特征值恒实数
8. skew-hermitian $A^\dagger=-A$
   * 特征值纯虚（包含0）
   * 与hermitian matrix同构`A=iB`
9. unitary matrix: $UU^\dagger=I$
   * 等价定义：列向量正交归一，行向量正交归一
   * 特征值模为1
10. special unitary matrix $det(A)=1$
11. TODO
    * Symplectic matrix [wiki](https://en.wikipedia.org/wiki/Symplectic_matrix)
