# computer system

1. link
   * [github/CSAPP-labs-note](https://github.com/Exely/CSAPP-Labs)
   * [github/linux-kernel-memory-management](https://github.com/0voice/kernel_memory_management)
   * [github/foxsen/archbase](https://github.com/foxsen/archbase) 《计算机体系结构基础》（胡伟武等，第三版）的开源版本
   * [coursera/computer-architecture](https://www.coursera.org/learn/comparch)
   * book/计算机组成与设计-硬件/软件接口
   * book/computer-architecture-a-quantitative-approach, Patterson and Hennessey
   * book/modern-processor-design-fundamentals-of-super-scalar-processors, Shennon-Leposty
   * [github/riscv-soc-book](https://github.com/cnrv/riscv-soc-book)

## coursera: computer organization

1. book
   * computer organization and design, Patterson and Hennessey
   * The Intel Microprocessors, Barry B. Brey
2. history
   * 1946 ENIAC
   * 1939 ABC
   * 1945 EDVAC 存储程序式计算机
   * 1975 Altair8800
   * 1975 Apple I
3. 冯诺依曼结构
   * 运算器central arithmatical，控制器central control，存储器memory，输入设备input，输出设备output
   * 外部记录介质outside recording medium
   * 数据和程序均以二进制代码形式不加区分地存放在存储器中，存放位置由存储器的地址指定
   * 计算机在工作是能够自动地从存储器中取出指令并加以执行
4. 取址fetch，译码decode，执行execute，回写write-back
5. 系统总线：控制总线，地址总线，数据总线
6. 简化模型（模型机）
   * Memory Address Register
   * Memory Data Register
   * 内部总线
7. 组成
   * 南桥芯片：磁盘，键盘，鼠标，音频，网络，BIOS芯片，USB等多种输入输出设备或接口的控制器
   * 部分性能要求高或者用途特殊的输入输出接口采用独立芯片或板卡的形式，例如显卡
   * 北桥芯片：PCIe控制器，集成显卡，主存控制器
   * 北桥没了，南桥重命名为Platform controller Hub (PCH)

指令系统体系结构

1. 指令
   * 运算类指令`ADD R,M`
   * 传送类指令`LOAD R,M`, `STORE M,R`
   * 转移类指令`JMP L`
2. 通用寄存器，运算单元，CPU访问存储器，三者的位宽一般是相同
3. 8086
   * 16位寄存器，20位地址总线，16位数据总线
   * 寄存器模型：通用寄存器（多功能寄存器），指令指针寄存器
   * 段寄存器
   * 标志寄存器

## coursera: computer architecture

1. concept
   * instructional parallelism
   * thread level parallelism
   * process level parallelism
   * vector parallelism
   * cache coherent system
   * multi-core and many-core system

TODO
