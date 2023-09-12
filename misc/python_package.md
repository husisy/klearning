# Python Package

TODO

写在开头：如果你的代码仅几十行或者说单个 `.py` 文件即可表述完，往往这也是大多数情况，那么保留现有的代码结构往往是最佳选择，例如

1. 一个主程序文件`draft00.py`
2. （也许存在）函数库文件`utils.py`，该文件会在主程序文件中导入

对于这种不太长的代码功能，不讲道理地将其封装成库`XXX`只会带来麻烦

1. 错误调试跨文件：若`draft00.py`中抛出`XXX/utils.py`的错误，只能通过重启解析器来调试，几乎不能在python/ipython命令行下交互式调试错误
2. 过度封装带来的重构困难：`utils.py`里的全局变量、函数接口可能在多个文件中引用，这种情况下的代码重构麻烦远大于单个`draft00.py`文件下的重构

关于命名习惯

1. `draft00.py`, `draft_xxx.py`
   * 主程序入口，类似于`c/cpp`中的`main()`所在的文件
   * 通常没有`__name__=='__main__`
2. `utils.py`, `xxx_utils.py`: 辅助函数库，通常是（出现频率依次降低）纯函数、类定义、常量

关于写Python代码到形成一个Python库

1. `draft00.py`
2. `utils.py`
3. `test_utils.py`
4. `a_utils.py`, `b_utils.py`
5. `python/XXX/__init__.py`, `tests/`
   * 注: 个人不建议在项目根目录使用`XXX/__init__.py`文件结构
6. `docs/`
   * 写文档很头疼

对于经常使用的函数功能、代码片段，可以考虑将其整理为Python库

设计class

1. 相比设计function，需要大量考虑用户的使用场景
2. 坚决反对刚开始写代码时便大量使用class，功能迭代需要大面积修改代码
