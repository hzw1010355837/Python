> * matplotlib:三层结构
>
>   1. 容器层:有Canvas,Figure,Axes组成
>      1. Canvas是位于最底层的系统层，在绘图的过程中充当画板的角色，即放置画布(Figure)的工具 
>      2. Figure是Canvas上方的第一层，也是需要用户来操作的应用层的第一层，在绘图的过程中充当画布的角色 
>      3. Axes是应用层的第二层，在绘图的过程中相当于画布上的绘图区的角色 
>         1. Figure:指整个图形(可以通过plt.figure()设置画布的大小和分辨率等)
>         2. Axes(**坐标系**):数据的绘图区域
>         3. Axis(**坐标轴**)：坐标系中的一条轴，包含大小限制、刻度和刻度标签
>   2. 辅助显示层:为Axes(绘图区)内的除了根据数据绘制出的图像以外的内容，主要包括Axes外观(facecolor)、边框线(spines)、坐标轴(axis)、坐标轴名称(axis label)、坐标轴刻度(tick)、坐标轴刻度标签(tick label)、网格线(grid)、图例(legend)、标题(title)等内容 **设置该层可使图像显示更加直观更加容易被用户理解，但又不会对图像产生实质的影响**
>   3. 图像层:指Axes内通过plot、scatter、bar、histogram、pie等函数根据数据绘制出的图像 
>
>   * Canvas（画板）位于最底层，用户一般接触不到
>   * Figure（画布）建立在Canvas之上
>   * Axes（绘图区）建立在Figure之上
>   * 坐标轴（axis）、图例（legend）等辅助显示层以及图像层都是建立在Axes之上

> * 使用plt
>   * 