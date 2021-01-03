# 群论

*备注*：关于群论，我暂时没有想到该如何代码验证

1. link
   * 课程讲义，[群论-李新征](http://faculty.pku.edu.cn/_tsf/00/0F/yEVrEjjaaEza.pdf)
   * [蔻享视频](https://www.koushare.com/video/videodetail/7557)
   * 《群论》 韩其智，孙洪洲，北京大学出版社 [豆瓣link](https://book.douban.com/subject/3584574//)
   * 《群论讲义》 王宏利，未出版
   * 《群论及其在固体物理中的应用》 徐婉棠，喀兴林，高等教育出版社
   * 《Group Theory: Application to the Phsycics of Condensed Matter》 M. S. Dresselhaus, G. Dresselhaus, A. Jorio, Springer
   * 《Group Theory for Physicists》 Zhongqi Ma（马中骐）, World Scientific
   * 《Group Theory in a Nutshell for Physicists》 Anthony Zee
2. 重要人物
   * Emmy Noether (1882-1935, 德国犹太人)：理体系的对称性与守恒量之间得关系
   * Eugene Paul Wigner（1902-1995，匈牙利人，后加入美国籍）
   * Hermann Klaus Hugo Weyl（1885-1955，德国人）
   * Linus Carl Pauling
3. 有限群理论、转动群、双群、利群，群基础理论，群表示理论
4. 规范场理论：连续变换下的对称性与守恒量的关系

## chapter1 群的基本概念

1. 群：集合、乘运算、封闭性、结合律、单位元、逆元
2. 按群元个数（阶order）分为有限群、无限群
3. 按乘法是否可交换分为Abel群、非Abel群。前者乘法表是对称的
4. 重排定理：给定群G，对于任意元素`a`，对于所有元素`b`，则`ab`给出且仅给出一次G中所有元素
5. 子群、显然子群/平庸子群`{e}`、固有子群/非平庸子群
6. 群元的阶：对任意一个有限群，从中取元素a，从a出发作幂操作，总是可以构成G的一个循环子群
7. 陪集，左陪集，右陪集
8. 陪集定理：设群H是群G的子群，则H的两个左陪集或者完全相同，或者没有任何共同元素，右陪集同理
9. 拉格朗日Lagrange定理：有限子群的阶必为群阶的因子
10. 共轭：给定群中的两个元素`f,h`，如果存在元素`g`，使得`gfg^(-1)=h`，则称`f,h`共轭，记作`f~h`
    * 相互性：`f~h`则`h~f`
    * 传递性：`f~h,h~i`则`f~i`
11. 类：群G中所有相互共轭的元素形成的集合
    * 构造方法：给定元素`a`，遍历所有元素`b`，构造集合`{bab^(-1)`
    * 单元元自身构成一类
    * Abel群每个元素构成一类
    * 共轭元素的阶相等
    * 有限群的每个类中元素的个数都是群阶的因子
    * 类**不是**群：这个集合没有单位元
12. 共轭子群：G的两个子群H和K，若存在元素g使得`K=gHg^(-1)`，则称H和K为共轭子群
    * 两个共轭子群里必有同类的元素
    * 传递性
    * 共轭子群类
13. 不变子群/正规子群：G的一个子群H，若H中所有元素的同类元素都属于H，则称H是G的不变子群
    * G的一个不变子群H，对于任意G中元素g，`gHg^(-1)=H`
    * Abel群的子群都是不变子群。因为每个元素自成一类
    * 不变子群的左陪集与右陪集相等
    * G的不变子群H的任意两个不同陪集元素的乘积，必为第三个陪集中的元素，即`aH x bH = cH`
14. 商群G/H：群G有不变子群H，将H的陪集分解称作G对其不变子群H的商群
15. 例子
    * 空间反演群：`{E,I}`, `Er=r`, `Ir=-r`
    * n阶置换群：阶是`n!`
    * D3群：阶是`6`，三角形的纯转动群，3阶置换群
    * n阶循环群：`{a,a^2,a^3,...,a^n=e}`，一定是Abel群
    * SO(3)群：绕某点的转动，无线群
16. TODO page38
