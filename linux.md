> 1. `netstat -tunlp | grep 端口号` : 
>
>    * ```shell
>       -t (tcp) 仅显示tcp相关选项
>       -u (udp)仅显示udp相关选项
>       -n 拒绝显示别名，能显示数字的全部转化为数字
>       -l 仅列出在Listen(监听)的服务状态
>       -p 显示建立相关链接的程序名	
>       ```
>
> 2. `firewall-cmd --permanent --zone=public --add-port=80/tcp` :永久开放80端口号 
>
>    * **firewall-cmd --reload**   配置立即生效 
>
> 3. ` firewall-cmd --zone=public --add-port=80-90/tcp --permanent` :多端口
>
> 4. `firewall-cmd --permanent --zone=public --remove-port=80/tcp`: 移除80端口号
>
>    ```shell
>    --zone #作用域
>    --add-port=80/tcp #添加端口，格式为：端口/通讯协议
>    --permanent #永久生效，没有此参数重启后失效
>    
>    # 查看防火墙所有信息
>    firewall-cmd --list-all
>    
>    # 查询端口开启信息  ------------
>    firewall-cmd --list-ports
>    
>    # 更新防火墙规则
>    firewall-cmd --reload
>    
>    # 启动|关闭|重新启动 防火墙
>    systemctl [start|stop|restart] firewalld.service
>    
>    # 查看开启服务 --其实一个服务对应一个端口，每个服务对应/usr/lib/firewalld/services下面一个xml文件。
>    firewall-cmd --list-services
>    
>    # 查看还有哪些服务可以打开
>    firewall-cmd --get-services
>    
>    补充说明
>    firewall-cmd 是 firewalld的字符界面管理工具，firewalld是centos7的一大特性，最大的好处有两个：支持动态更新，不用重启服务；第二个就是加入了防火墙的“zone”概念。
>    
>    firewalld的配置文件以xml格式为主（主配置文件firewalld.conf例外），他们有两个存储位置
>    1、/etc/firewalld/ 用户配置文件 -- zone目录下public.xml可参考编辑。
>    
>    2、/usr/lib/firewalld/ 系统配置文件，预置文件
>    ```
>
> 5. `cat /etc/os-release`查看linux版本信息

> 1. `./nginx -s reload` /usr/local/nginx/sbin/nginx :修改配置后重写加载配置
>    * `./nginx -s stop`