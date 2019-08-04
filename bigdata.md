> * keepalived:实现高可用,两台ngnix上部署两个keepalived
>
>   1. vrrp:虚拟路由冗余协议,是由IETF提出的解决局域网中配置静态网关出现单点失效现象的路由协议 
>
>   2. ```shell
>      systemctl daemon-reload  # 重新加载
>      
>      systemctl enable keepalived.service  # 设置开机自动启动
>      
>      systemctl disable keepalived.service  # 取消开机自动启动
>      
>      systemctl start keepalived.service  # 启动
>      
>      systemctl stop keepalived.service  # 停止
>      ```
>
>      

> * zookeeper:分布式协调服务,就是为用户的分布式应用程序提供协调服务
>   * zookeeper是适合用在奇数台机器上

> * RPC: 远程过程调用协议,一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的协议
>
>   * 阻塞 block IO与 非阻塞Non-block IO :BIO&NIO
>
>     * 阻塞和非阻塞是进程在访问数据的时候，数据是否准备就绪的一种处理方式，当数据没有准备的时候阻塞：往往需要等待缞冲区中的数据准备好过后才处理其他的事情，否則一直等待在那里 
>
>   * 同步(Synchronization)和异步(Async)的方式 
>
>     * 同步和异步都是基于应用程序私操作系统处理IO事件所采用的方式，比如同步：是应用程序要直接参与IO读写的操作。异步：所有的IO读写交给搡作系统去处理，应用程序只需要等待通知 
>
>     | IO模型 | IO                 | NIO                                |
>     | ------ | ------------------ | ---------------------------------- |
>     | 方式   | 从硬盘到内存       | 从内存到硬盘                       |
>     | 通信   | 面向流（乡村公路） | 面向缓存（高速公路，多路复用技术） |
>     | 处理   | 阻塞IO（多线程）   | 非阻塞IO（反应堆Reactor）          |
>     | 触发   | 无                 | 选择器（轮询机制）> *              |

> * HADOOP:服务器集群,对海量数据进行分布式处理
>   1. HDFS:分布式文件系统
>   2. YARN:运算资源调度系统
>   3. MAPREDUCE:分布式运算编程框架