# knowledge learning

初衷：learning仓库（以下称作toolbox-learning）将一系列的软件（编程语言、第三方包都统称为软件）的使用指南整理堆砌在一块，当这些软件的使用方法连成一片时，工作效率能得到极大提升，例如某项工作需要软件A/B/C/D等协同，倘若A/B/D都已出现在toolbox-learning中，那寻找合适的C也就是一件极其自然的事情了，进而可以将C也补充到toolbox-learning中（所谓“读书破万卷，下笔如有神”？）。toolbox-learning中内容绝大多数是计算机相关技能，所以我想进一步拓展到「knowledge-learning」，个人博士将以物理为中心，所以knowledge-learning也会以物理为主。

我们的目标是~~没有蛀牙~~**将知识系统化**

knowledge-learning区别于toolbox-learning

1. toolbox-learning侧重于工具的学习
2. knowledge-learning侧重于知识体系的构建

个人预期knowledge-learning构建于toolbox-learning之上，因此在knowledge-learning中应该不会去阐述「公式/算法对应的代码为什么是这样」

knowledge-learning预计包含如下四个方面

1. 数学方法
   * 包含基础数学知识，例如线性代数、微分几何
   * 主要包含公式推导与代码验证，例如「normal matrix是diagonalable的充分必要条件」
   * 作为下面模块的基础：例如线性代数知识在算法（优化）、课程笔记（量子力学）、文献阅读中都会使用
2. `algorithm`
   * 包含通用算法：优化方法（共轭梯度）、计算物理方法（有限差分，broyden）、计算机算法（动态规划）等
   * 主要包含算法实现（可直接调用），算法展示（Runge-Kutta优于前向差分），RGF，CPA
   * 这一模块的目的：有一类科研是领域A中的算法用在领域B中取得了好效果，我希望把每个领域中的方法都抽象到这一模块中，从而在探索新领域时能够将这一模块的方法直接拿来使用（深度学习中的autograd也许可用于很多领域）
   * 作为下面模块的基础
3. `course/`
   * 包含各种课程笔记：例如微分几何，量子力学，强化学习等，量子计算
   * 区别于数学方法模块：以量子力学为例，一般性公式推导放在数学方法模块，理论框架放在该模块
   * 这一模块的目的：视频课程不方便检索查阅，文字形式的笔记更合适
4. `paper/`
   * 不限主题，按领域分类：可能包含机器学习，量子输运等等
   * 记录内容可以非格式化（随笔）：例如文章亮点、结论等
   * 建立在以上模块的基础上，如有必要，可以把文章中的数学方法、算法剥离上上述模块
   * 代码复现
   * seminar之类的记录暂不打算纳入knowledge-learning，因为其有显著依赖于时间结点（例如用户检索信息直觉上会使用时间范围来检索该类记录），而该知识库倾向于使用类型/主题来分类而抹去时间信息。一个解决方案是在个人文件夹下记录seminar，然后整理归档后纳入knowledge-learning

TODO

1. [ ] 建立雏形，切入点包括课程笔记，算法CPA/RGF/FastMultipleMethod
2. [ ] github organization
3. [ ] axmath还是lyx，前者一定没法做git管理，那修改记录就没法查看，后者使用还不熟练
4. [ ] 流程图如何整合，processon还是用python代码写 [mermaid](https://mermaid.js.org/)
5. [ ] [github/pywonderland](https://github.com/neozhaoliang/pywonderland)

其他

1. 非git管理的文件
   * **禁止**将课程讲义、视频等版权归属原作者的内容添加至git管理中，但**务必**在文档中添加访问链接
2. 树状tree文件系统也许未必是最适合这一需求的，也许tag-based filesystem更适合
3. 任何一个领域深入展开都会无比庞大，所以上面涉及的模块都很有可能需要将其中的子模块单独拧出到一个独立的仓库管理
