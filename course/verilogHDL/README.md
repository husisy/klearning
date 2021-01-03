# verilog HDL数字继承电路设计原理与应用

1. link
   * [bilibili](https://www.bilibili.com/video/BV1zb411s7bY), 蔡觉平 西安电子科技大学微电子学院
2. 所有backslash用slash替代

## 01 电路设计方法概述

1. 以元件为基础-以单元为基础-以RTL综合为基础-以IP为基础（信号处理与显示控制）
2. 发展阶段
   * 1970 简单微处理器Micro Processor Unit (MPU)，存储器，标准通用逻辑电路
   * 1980 MPU，微控制器Micro Control Unit (MCU)，专用Application-Specific IC (ASIC)，单片机
   * 1990 通用型中央处理器Central Processing Unit (CPU)，信号处理器Digital Signal Processing (DSP)
   * 2000 IP
3. 硬件描述性语言Hardware Description Language (HDL)：根据电路结构的特点，采用层次化的设计结构，将抽象的逻辑功能用电路的方式进行实现
   * Verilog HDL, VHDL
4. 数字集成电路
   * 软核soft core：经过功能验证，5000门以上的可综合verilog HDL/VHDL模型
   * 固核firm core：在ASIC和FPGA期间上，经过综合验证，大约5000门以上的电路网表文件
   * 硬核hard core：在ASIC器件上，经过验证正确的，大于5000门以上的电路结构版图掩模
5. HDL simulator, [wiki](https://en.wikipedia.org/wiki/List_of_HDL_simulators)
   * [modelsim](https://www.mentor.com/company/higher_ed/modelsim-student-edition)
   * [cascade](https://github.com/vmware/cascade)

## 02 数据类型

1. 空白符：空格符`/b`，制表符`/t`，换行符`/n`，换页符。在编译和综合时，忽略空白符
2. 注释符
3. 标识符identifier，verilog区分大小写，VHDL不区分大小写
   * 转义标识符
4. 保留关键字
5. 数值：低电平0，高电平1，不确定或位置的逻辑状态X，高阻态Z
6. 整数及其表示`+/-<size>'<base_format><number>`
   * `base_format: bB oO dD hH`
7. 实数表示：定点/浮点，十进制表示法，科学计数法
8. 物理数据类型：连线型，寄存器型，存储器数据类型
9. 信号强度：数字电路中不同强度的驱动源
   * supply：电源及驱动，驱动
   * strong：强驱动，驱动
   * pull：上拉级驱动，驱动
   * large：大容性，存储
   * weak：若驱动，驱动
   * medium：中型驱动，存储
   * small：小容性，存储
   * highz：高容性，高阻
10. 连线型：wire, tri, wor, trior, etc. `<net_declaration><drive_strength><range><delay>[list_of_variables]`
11. 寄存器类型 `reg<range><list_of_register_variables>`
12. 存储器类型 `reg <range1><name_of_register><range2>`
13. 抽象数据类型：整型integer，时间型time，实型real，参数型parameter

## 03 运算符和表达式

1. 算术操作符`+-*/%`
   * 结果长度由最长的操作数决定
   * 赋值语句瞎，结果长度由被赋值变量决定
   * 有符号和无符号数的使用
2. 关系操作符`> < >= <=`
3. 相等关系操作符`== != === !==`
4. 逻辑运算符`&& || !`
5. 按位操作符`~ & | ^ ^~`
6. 归约操作符`& | ^ ~& ~| ~^ ^~`
7. 移位操作符`<< >>`
8. 条件运算符`<cond>?<expr0>:<expr1>`
9. 连接和复制运算符`{} {{}}`
10. 模块module：模块的开始与结束，模块端口定义，模块数据类型说明，模块逻辑功能描述

## 04 数据流建模
