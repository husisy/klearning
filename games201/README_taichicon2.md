# taichicon2

Special Interest Group (SIG)

## 用taichi编写不可压缩流体模拟器

1. 基于FVM和SIMPLE格式
2. 以往编程语言存在计算效率和编程效率的冲突
3. 卡门涡街Kármán vortex street：流体在绕过障碍物的过程中，满足一定条件时产生的振动现象
   * [wiki](https://en.wikipedia.org/wiki/K%C3%A1rm%C3%A1n_vortex_street)
   * 冯·卡门Theodore von KármánX 哥廷根大学
   * 大约雷诺数大于`50`时开始 $Re=\frac{\rho U D}{\mu}$
   * ~~非常好看~~在工程中有很多重要意义（防止流体振动引起的结构破坏）
4. Computational Fluid Dynamics (CFD)
   * 辅助设计，辅助实验，辅助研究
5. 与计算机图形学中流体仿真的区别于联系
   * 更强调物理正确性，守恒特性，方程的严格满足
   * 不那么强调计算的实时性和交互性
   * 基本的计算思路非常类似
6. 空间离散方法
   * 有限体积法finite volume method (FVM)
   * 有限元法finite element method (FEM)
   * 有限分析法finite analytic method (FAM)
7. 有限体积法的特点
   * 物理含义明确，守恒特性好
   * 被主流CFD商用软件广泛使用
   * 学术研究历史丰富，资源广泛
   * 计算过程略微繁琐，计算量大
8. 控制方程
   * 质量守恒 $\nabla\cdot\vec{u}=0$
   * 动量守恒 $\rho\frac{D\vec{u}}{Dt}=-\nabla p + \mu\nabla^2\vec{u}$
9. Biconjugate gradient stabilized method (bicgstab) [wiki](https://en.wikipedia.org/wiki/Biconjugate_gradient_stabilized_method)
10. 错位网格
    * 在网格的中心保存标量，在边界保存矢量
11. 压力场与速度场的耦合问题 Semi-Implicit Method for Pressure Linked Equations (SIMPLE)
    * 假定初始速度分布、压力场
    * 根据速度场和压力场计算动量离散方程的系数、常数
    * 解出动量离散方程
    * 求得压力修正方程以满足质量守恒方程
    * 对压力和速度进行修正
    * 判断是否收敛，不收敛的话则计算下一次迭代（区别于Robert Bridson实现）

## Packed Mode-effectively reducing memory costs of noon-power-of-two fields

Yi Xu

1. 在`packed=False`时，`(4180,6264,3)`会补齐为`(8192,8192,4)`
2. 2幂次的优点：bitwise operations for access (fast and convenient)
3. 使用2幂次的场景
   * memory layout
   * field access
   * struct for (range for)
