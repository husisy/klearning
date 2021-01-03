# Excel Beauty of Data

[excel数据之美](https://book.douban.com/subject/26883742/)

## 第一章、琐碎事项

1. 配色
2. 加框（注意力集中、tick向内）、没框（过渡无障碍、tick向外）
3. 坐标轴向内、向外
4. tag cloud
5. author guidelines, [ACS-author guidelines](https://publish.acs.org/publish/author_guidelines?coden=jacsat)
6. ggplot
   * ggplot2 elegant graphics for data analysis
   * R Graphics cookbook

## 配色

1. tableau 10 medium: (96,157,202) (255,150,65) (56,194,93) (255,91,78) (184,135,195) (182,115,101) (254,144,194) (164,160,155) (210,204,90)
2. R ggplot2 set3: (255,108,145) (188,157,0) (0,187,87) (0,184,229) (205,121,255) 主要网格线(255,255,255) 次要网格线(242,242,242)

## 科学图表的基本元素

1. chart area
2. grid line: 主要/次要 水平/垂直 网格线
3. plot area: 背景颜色 Python(234,234,242) MATLAB(255,255,255) R(229.229.229)
4. axis label: 横/纵 单位 字体Times New Roman
5. number axis: 对数，tick，
6. chart title: (a) (b) Figure.1 (a)
7. data marker
8. legend
9. error bars
10. trend line
11. increase/drop line

## 字体

1. 标题使用无衬线字体(Sans serif)
2. 正文使用衬线字体(Serif)
3. 修饰性字体(Ornamental)
4. 图表请使用衬线字体，数字和字母一般选用Times New Roman，汉字一般选用宋体

## 案例

1. 坐标轴调整：轴线条，轴范围，主要单位，次要单位
2. 坐标轴tick、label，字体times new roman，字号
3. 坐标轴标题，位置，字体斜体times new roman，
4. 绘图区，背景色(229,229,229)，边框，网格线(255,255,255)，主轴次要网格线(242,242,242)，网格线宽度
5. 数据标签，点类型，大小，颜色，线宽，颜色，透明度

## 图表类型

1. 散点图和气泡图：分类比较
2. 柱状图、条形图、直方图、排列图（帕累托图）、瀑布图、漏斗图
3. 面积图、折线图
4. 雷达图、南丁格尔玫瑰图
5. 饼形图、旭日图
6. 箱型图、树状图、其他
7. 地图系列图

## 密度散点图

scatter + MarkerFaceAlpha

## 滑珠散点图（可以用来替代表格）

可以画

## 双纵坐标轴

一个自变量，两个因变量
