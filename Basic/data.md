> * matplotlib:三层结构
>
>   1. 容器层:有Canvas,Figure,Axes组成
>      1. Canvas是位于最底层的系统层，在绘图的过程中充当**画板**的角色，即放置画布(Figure)的工具 
>      2. Figure是Canvas上方的第一层，也是需要用户来操作的应用层的第一层，在绘图的过程中充当**画布**的角色 
>      3. Axes是应用层的第二层，在绘图的过程中相当于画布上的绘图区的角色 
>         1. Figure:指整个图形(可以通过plt.figure()设置画布的大小和分辨率等)
>         2. Axes(**坐标系**):数据的绘图区域
>         3. Axis(**坐标轴**)：坐标系中的一条轴，包含大小限制、刻度和刻度标签
>   2. 辅助显示层:为Axes(绘图区)内的除了根据数据绘制出的图像以外的内容，主要包括Axes外观(facecolor)、边框线(spines)、坐标轴(axis)、坐标轴名称(axis label)、坐标轴刻度(tick)、坐标轴刻度标签(tick label)、网格线(grid)、图例(legend)、标题(title)等内容 **设置该层可使图像显示更加直观更加容易被用户理解，但又不会对图像产生实质的影响**
>   3. 图像层:指Axes内通过plot、scatter、bar、histogram、pie等函数根据数据绘制出的图像 
>
>   * Canvas（画板）位于最底层，用户一般接触不到
>   
>   * Figure（画布）建立在Canvas之上
>   
>   * Axes（绘图区）建立在Figure之上
>   
>     * 辅助显示层: 刻度、标题、图例
>   
>     * 图像层:调节参数：颜色、线条风格
>                               折线图:plt.plot()  变化
>                               散点图:plt.scatter()  规律、关系
>                               直方图:plt.hist()  分布状况
>   
>       ​                        饼图:plt.pie()  占比
>   
>   * 坐标轴（axis）、图例（legend）等辅助显示层以及图像层都是建立在Axes之上

> * 使用plt:**1创建画布2绘制图像3显示图像**
> * 折线图:**呈现各种变化情况**:**画各种数学函数图像**
>
> ```python
> import matplotlib.pyplot as plt
> plt.figure(figsize=(长,宽), dpi=清晰度)  # 创建画布
> plt.plot([1,0,9], [4,5,6])  # 绘制折线图
> plt.show()  # 显示图像
> ```
>
>  ```python
> """创建画布"""
> plt.figure(figsize=(20,10), dpi=100)
> """绘制图像"""
> plt.plot(random(60),[random.uniform(15,18) for _ in random(60)])
> # plt.plot(x,y,color,linestyle,label) 设置label图例时需要在图像辅助层添加代码
>  """辅助显示层"""
> x_label = ["11点{}分".format(range(60))]
> plt.xticks(random(60)[::5], x_label[::5])  # 修改刻度
> plt.yticks(range(40)[::5])
> plt.grid(True, linestyle="--", alpha=0.5)  # args:(True)默认显示网格,显示线条风格,透明度
> plt.xlabel(str)  # 添加描述信息
> plt.xlabel(str)
> plt.title(str)
> plt.lengend()  # 将图例添加至最佳位置 "best\upper right\center left" 
> """显示图像"""
> plt.show()
>  ```
>
>  ```python
> figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(20,10), dpi=100)  # 使用面向对象的方式画图,1行2列
> axes[0].plot(x, y, color="r", label="上海")
> axes[0].set_xticks(x[::5])
> axes[0].set_xticklabels(x_label[::5])  # 正确显示label
> axes[0].set_title("xixixi")
> axes[0].set_xlabel("one hour")
> axes[0].grid(True, linestyle="--", alpha=0.8)
> axes[0].legend()
> plt.show()
>  ```
>
>  