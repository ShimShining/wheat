- 涵盖测试的全技能
- 面试中常见的问题
- 网络上收集的一些面试经验
# 测试理论
## 如何理解工程效能的
- 由Google举办的GTAC大会在2016年提出的工程效能的概念，可以简单的理解成为了更好的做自动化测试以及测试产出而衍生出的工程效能上的工具平台或方法论，
- 而我的理解是提升加快研发效能，和提升工程师团队效率和质量
- 测试谁来做，工程效能模式下没有专职的测试人员，而开发做测试肯定会提升效率
- 开发转型做测试后，从人员的角度上看，unit test依旧还是开发来做，而apitest，guitest在转型后指向了转型过来的开发
- 原来的业务测试人员可以更专注与探索性测试
## 如何理解敏捷开发
- 敏捷开发属于增量式开发
- 对于需求范围不明确、需求变更较多的项目而言可以很大程度上响应和拥抱变
- 主张简单、拥抱变化、可持续性、递增的变化、高质量的工作、快速反馈
- 软件是你的主要目标
## 什么是CI/CD,什么是DevOps
- ci 持续集成
- cd持续交付，持续部署
- DevOps促进软件开发部门,qa和运维部门，三个部门的之间沟通，协调，合作的工作模式
## 什么是 BDD,什么是 TDD
- bdd 行为驱动开发
- tdd测试驱动开发
## 用例设计方法
### 判定表
#### 判定表知识点
- 判定表的定义
    - 分析和表述若干条件下,被测对象针对这些输入做出的响应的一种工具
    - 在遇到复杂业务逻辑时,可以利用该表理清逻辑关系
- 概念
    - 条件
        - 条件桩: 需求规格说明书定义的被测对象的所有输入
        - 条件项: 针对条件桩所有可能输入数据的真假值
    - 动作
        - 动作桩: 针对条件,被测对象可能采取的所有操作
        - 动作项: 针对动作桩,被测对象响应的可能取值
    - 规则: 条件项和动作项组合在一起,形成的业务逻辑处理规则
- 判定表应用步骤
    - 1.理解需求,确定条件桩和动作桩
    - 2.设计及优化判定表
    - 3.填写动作项
    - 4.根据判定表中输出结果的表现,进行判定表的合并(非必须),简化判定表;如果输出相同,在对应的输入中,有且只有一个条件的取值对动作不产生任何影响则可合并
### 因果图
- 定义: 因果图是一种形式语言,用自然语言描述的规格说明可以转换为因果图
- 因果图实际上是一种数字逻辑电路(一个组合的逻辑网络),没有标准的电子学符号,而是使用了稍微简单点的符号
- 输入与输出的关系
    - 恒等: 当输入条件发生时,结果一定出现,否则一定不出现
    - 非: 当输入条件发生时,结果一定不出现,否则,一定出现
    - 或: 当多个输入条件时,只要有一个发生,结果就会发生
    - 与: 当多个输入条件时,只有所有输入条件都发生,结果才会发生
- 输入与输入的关系
    - 异: 所有输入条件中最多有一个产生,也可以一个没有
    - 或: 所有输入条件中,最少有一个产生,或者多个,或者所有
    - 唯一: 所有输入条件中,有且只有一个条件产生
    - 要求: 所有输入条件中,只要有一个产生,其他条件也会跟着出现
- 步骤
    - 1.按规格说明分解为可执行的片段
    - 2.确定规格说明中的因果关系
    - 3.分析规格说明的语义内容,并将其转换为连接因果关系的布尔图
    - 4.给图加上注解符号,说明由于语法或环境限制而不能联系起来的因和果
    - 5.通过仔细地跟踪图中的状态变化情况,将因果图转换成一个有限项的判定表
    - 6.将判定表的列转换成测试用例

### 正交
- 因子: 所有参与实验的且影响实验结果的条件称为因子
- 水平: 影响实验因子的取值或输入称为水平
- 整齐可比: 在同一张正交表中每个因子的每个水平出现的次数完全相同,实验中每个因子的每个水平与其他因子的水平参与实验的几率完全相同
- 均匀分散: 同一张正交表中,任意两列的水平搭配时完全相同的
- 设计流程
    - 分析需求获取因子及水平
    - 根据因子水平选择合适的正交表
    - 替换因子水平,获取实验次数
    - 根据经验或其他因素补充实验次数
    - 细化输出获取测试用例
- 注意点
    - 选择正交表示,因子和水平敲好与正交表相同时,直接使用正交表
    - 被测对象因子与正交表中的因子数不同,选择正交表中因子项大于被测对象因子数,且试验次数最少的,多余的因子弃用
    - 因子水平都不相同,则可选择因子,水平稍大于被测对象的,且试验次数最少的
### 状态迁移
- 关注被测对象的状态变化,在需求规格说明书中是否有不可达到的状态和非法的状态,是否产生非法的状态转移
- 状态: 被测对象在特定输入条件下所保持的响应形式
- 方法流程
    - 根据需求明确状态节点
    - 绘制状态迁移图
    - 绘制状态迁移树
    - 抽取测试用例
---
# 基础技能
## 系统
### 操作系统的中断是如何处理
- 中断是指CPU对系统发生的某个时间做出的一种反应,CPU暂停正在执行的程序,保存现场后自动去执行相应的处理程序,处理万该事件后再返回中断处继续执行原来的程序
- 中断一般分为三类
    - CPU外部引起的中断: I/O中断,时钟中断
    - CPU内部事件或程序执行中引起的中断: 程序非法操作,地址越界,浮点溢出
    - 在程序中使用了系统调用引起的
- 中断处理一般分为两个步骤
    - 中断响应: 由硬件实施
    - 中断处理: 由软件实施
## Linux
### 命令
#### 查看某个端口是否被占用
- netstat -anp | grep 8080
- ls -of | grep 8080
#### 将1个服务器的文件拷贝到另一个服务器上
将本地文件拷贝到远程
- scp 文件名 用户名@计算机IP或者计算机名称:远程路径
- scp /root/install.* root@192.168.1.12:/usr/local/src  
从远程将文件拷回本地
- scp 用户名@计算机IP或者计算机名称:文件名  本地路径
- scp root@192.168.1.12:/usr/local/src/*.log /root/
- 复制目录加-r参数
- scp -r /home/test1 zhidao@192.168.0.1:/home/test2 
## Android
### Android手机卡顿的原因
- 碎片化的系统因素
    - Android整个平台的差异越来越大
    - 流通版本较多(官方发行的版本有20多个)
    - Android设备形态各异,设备形态的差异,导致必须接受各种各样的适配和定制
    - 第三方ROM厂商改造
- 内存回收机制(DVM)
    - DVM继承了JAVA的GC内存回收机制
    - 当系统执行内存回收的时候其他程序(进程)都将处于暂停状态
    - 一般情况下GC并不会导致卡顿,用户感知性不强
    - 但是连续的GC会导致进程暂停状态时间累积加长
    - 屏幕刷新率60帧的标准,暂停时间超过16毫秒,就会导致帧率异常,连续的异常丢帧,用户感知到了,就形成了卡顿
- 硬件性能与软件不匹配
    - 手机性能的主要指标有CPU,内存,GPU,EMMC 
- 应用优化自身问题,导致的卡顿
    -  不好的大图片资源处理机制,大图意味着大内存,也就是最容易造成内存泄漏,抖动等问题,小则频繁触发GC,引起卡顿,大则引发OOM,应用崩溃
    -  内存泄漏,体现在静态变量引用了本需要回收的对象,导致该对象不能回收;可用内存越来越少,可能引发其他应用卡顿
    -  界面UI线程处理不当,UI线程中处理了过多的耗时操作,导致UI线程来不及处理画面帧的生成,绘制,导致帧率过低,从而用户感知卡顿
    -  不好的缓存机制
- 运行时所需要的资源存在强烈的竞争
## 容器
### 什么是容器技术
- 将运行的应用，和所使用的环境，依赖，配置等东西用沙盒技术包装起来，形成的一个容器
- 容器的特点就是，不管到那个机器下都里面的应用都可以运行
### docker
应用容器引擎，可以使用docker来打包容器镜像，然后发布到任何一台机器上，实现虚拟化技术
#### docker的优缺点
- 优点：可以快速部署，资源占用低，快速移植，扩展，高效虚拟化
- 缺点：各应用之间不是完全隔离，没有虚拟机那么彻底，使用的是宿主机的内核，没有虚拟化自己的内核
#### 运行docker run命令的时候–link参数的原理，如果两个容器分布在不同的机器上无法使用–link,那么我们应该怎么处理
- –link的原理是将目标容器的网络信息已环境变量的形式注入到容器中
- 所以如果两个容器不在同一台机器上无法使用link参数,
- 那么可以在启动容器的时候直接使用-e参数设置环境变量来给容器传递网络的IP地址和端口号等信息
#### 在docker selenium的开源项目中，为什么不支持IE镜像
- 因为容器并不虚拟化自己的内核，而是在一台机器上的所有容器都使用宿主机的内核。
- 而docker只能安装在linux系统上（因为容器的底层逻辑需要linux内核的能力)
- 而IE浏览器是使用windows内核驱动的，所以无法制作IE浏览器的镜像
#### 如果我们有一个软件要进行部署测试。要测试软件可以兼容各种操作系统，那么可以使用docker启动centos或者redhat镜像来完成测试么
- 不可以，因为容器并不虚拟化自己的内核，而是在一台机器上的所有容器都使用宿主机的内核。
- 所以如果宿主机的内核是3.1.0的版本,即便我们启动了名字为centos 6或者centos 7或者其他镜像，那么在容器里仍然使用的是3.1.0的内核。
- 所以总结下来任何对内核有要求的场景尽量不要使用容器
#### 如果我们现在需要排查一个容器中的网络问题，但是容器的镜像并没有安装任何的网络排查工具，也无法通过网络下载工具，这个时候要怎么做
- 可以启动一个带有网络排查工具的容器，然后通过 container 网络模式将新创建的容器挂载到要排查的容器上。
- 这样两个容器的网络就是互通的，就可以抓取到目标容器的网络流量
### k8s
是一款google开源的容器集群的管理系统，可以实现容器集群的自动化部署，自动扩缩容，维护等功能
#### k8s特点
1、负载均衡
2、水平扩展（对使用资源可以进行扩大和裁剪）
3、服务自愈（故障迁移）（高可用）
4、储存卷挂载
5、版本回退
6、安全（安全认证机制）


## 网络
#### 1.HTTP和HTTPS的区别,以及HTTPS有什么缺点
- http协议和https协议区别如下
    - http是以明文的方式在网络中传输数据,而https协议传世的数据则是经过TLS加密后的,HTTPS具有更高的安全性
    - HTTPS在TCP三次握手阶段之后,还需要进行ssl的handshake,协商加密使用的对称加密密钥
    - https协议需要服务端申请证书,浏览器端安装对应的根证书
    - http协议端口是80,https协议端口是443
- https优点
    -  https传输数据过程中使用密钥进行加密,因此安全性更高
    -  https协议可以认证用户和服务器,确保数据发送到正确的用户和服务器
- https缺点
    - https握手阶段延时较高: 由于进行http会话之前还需要进行ssl握手,因此https协议握手阶段延时增加
    - https部署成本高: 一方面https协议需要证书来验证自身的安全性,所以需要购买CA证书;另一方面由于采用https协议需要进行加解密计算,占用CPU资源较多,需要的服务器配置或数目高
#### 2. HTTP返回码
- HTTP协议的响应报文由状态行,响应头部和响应包体三部分组成,其响应状态码描述如下
    - 1xx: 指示信息,表示请求已接收,继续处理;
    - 2xx: 成功,表示请求已被成功接收,理解,接受(返回);
    - 3xx: 重定向,要完成的请求必须进行更进一步的操作;
    - 4xx: 客服端错误,表示请求有语法错误或请求无法实现;
    - 5xx: 服务端错误,服务器未能实现合法的请求;
- 常见状态码,状态描述的详细说明如下
    - 200 OK: 客户端请求成功
    - 206 partial content服务器一整正确处理部分GET请求,实现断点续传或同时分片下载,该请求必须包含Range请求来指示客户端期望得到的范围
    - 300 nultiple choice(可选重定向): 被请求的资源有一系列可供选择的反馈信息,由浏览器/用户自行选择其中一个
    - 301 moved permanently(永久重定向): 该资源已被永久移动到新位置,将来任何对该资源的访问都要使用本响应返回的若干个URI之一
    - 302 move temporarily(临时重定向): 请求的资源现在临时从不同的URI中获得
    - 304 not modified: 如果客户端发送一个带条件的GET请求,并且该请求已经被允许,而文档内容未被改变,则返回304,该响应不包含包体(即可直接使用缓存)
    - 403 Forbidden: 服务器收到请求,但是拒绝提供服务(权限)
    - 404 NOT Found: 请求资源不存在(输入了错误的URL)
#### IP地址,MAC地址的作用
- MAC地址是一个硬件地址,用来定义网络设备的位置,主要由数据链路层负责;
- IP地址是IP协议提供的一种统一地址格式,为互联网上的每一个网络和每一台主机分配一个逻辑地址,以此来屏蔽物理地址的差异
#### OSI七层模型和TCP/IP四层模型,每层的协议
- OSI 七层模型及其包含的协议如下:
    - 物理层: 通过媒介传输比特,确定机械及电气范围,传输单位为bit,主要包括的协议为->IEE502.3 CLOCK RJ45
    - 数据链路层: 将比特组装成帧和点到点的传递,传输单位为帧,主要包括协议为->MAC VLAN PPP
    - 网络层: 负责数据包从源到宿的传递和网际互联,传输单位为包,主要包括的协议为IP,ARP,ICPM
    - 传输层: 提供端到端的可靠报文传递和错误恢复,传输单位为报文,主要包括协议为TCP,UDP
    - 会话层: 建立,管理和终止会话,传输单位为SPDU,主要包括的协议为->RPC,NFS
    - 表示层: 对数据进行翻译,加密和压缩,传输单位为PPDU,主要包括的协议为JPEG ASII
    - 应用层: 允许访问OSI环境的手段,传输单位为APDU, 主要包括的协议为->FTP HTTP DNS
- TCP/IP 四层模型
    - 网络接口层 MAC VLAN
    - 网络层: IP ARP ICMP
    - 传输层: TCP UDP
    - 应用层: HTTP DNS SMTP
#### TCP的三次握手和四次挥手的过程
- 三次握手的过程如下
    - C -> SYN -> S
    - S -> SYN/ACK -> C
    - C -> ACK -> S
    - 三次握手的原因
        - 可以防止已经失效的连接请求报文突然又传输到服务器导致服务器资源浪费;
        - 例如: 客户端先发送了一个SYN,但是由于网络阻塞,该SYN数据包在某个节点长期滞留
        - 然后客户端又重传SYN数据包并正确建立TCP连接,然后传输数据后关闭连接;该连接释放后失效的SYN数据包才到达服务器
        - 如果是两次握手,服务器会认为这是客户端发起的又一次请求,然后发送SYN/ACK,并在服务器创建SOCKET套接字,等待客户端发送数据
        - 由于客户端并没有发起新的请求,所以会丢弃服务端的SYN/ACK,此时服务端会一直等待客户端发送数据从而造成资源浪费
- TCP四次挥手
    - C -> FIN -> S
    - S -> ACK -> C
    - S -> FIN -> C
    - C -> ACK -> S
    - 四次挥手的原因
        - 连接的关闭控制权在应用层,所以被动关闭的一方在收到FIN包时,TCP协议栈会直接发送一个ACK确认包
        - 优先关闭一端的通信
        - 然后通知应用层,由应用层决定什么时候发送FIN包
        - 应用层可以使用系统调用函数read==0来判断对端是否关闭连接.
#### 搜索百度,整个网络的链路
- 浏览器输入URL
    - 浏览器将URL解析为IP地址,解析域名需要用到DNS协议
    - 首先主机会查询DNS的缓存,如果没有就给本地的DNS发送查询请求
    - DNS查询分为两种查询,一种 是递归查询,一种是迭代查询
        - 迭代查询: 本地DNS服务器,向根域名服务器发送查询请求,根域名服务器告知该域名的一级域名服务器,然后本地服务器给该一级域名服务器发送查询请求,然后依次类推知道查询到该域名的IP地址
    - DNS服务器是基于UDP,会用到UDP协议
    - 得到IP地址后,浏览器就要与服务器建立一个http连接,要用到http协议
    - http生成一个get请求报文,将该报文传给TCP层处理,用到TCP协议
        - 如果采用https,会使用https协议先对http数据进行加密
    - TCP层如果有需要,先将HTTP数据包分片,分片依据路径MTU和MSS
    - TCP数据包会发送给IP层,用到IP协议
    - IP层通过路由选路,然后发送到目的地址
        - 在一个网段内寻址是通过以太网协议实现(也可以是其他物理层,比如PPP)
        - 以太网协议需要知道目的IP地址的物理地址,需要ARP协议
    - 解释
        - 1. DNS,http, https协议属于应用层
            - 应用层是体系结构中的最高层
            - 应用层确定进程之间的通信性质以满足用户的需要,进程是指正在运行的程序
            - 应用层不仅要提供应用进程所需要的信息交换和原地操作,而且还要作为互相作用的应用进程的用户代理,来完成一些为进行语义上有意义的信息交换所必须的功能
            - 应用层直接为用户的应用进程提供服务
        - 2. TCP/UDP属于传输层
            - 传输层的任务就是负责主机中两个进程之间的通信
            - 因特网的传输层可使用两种不同协议
                - 面向连接的传输控制协议TCP,面向连接的服务能够提供可靠的交付
                - 无连接的用户数据报协议,无连接服务则不保证提供可靠的交付,只是尽最大努力交付
            - 在分组交换网络内的各个交换结点机都没有传输层
        - 3. IP,ARP协议输入网络层
            - 网络层负责为分组交换网上的不同主机提供通信
            - 发送数据时,网络层将运输层产生的报文段或用户数据报封装成分组或包进行传送
            - 在TCP/IP体系中,分组也叫做IP数据报,或简称数据报
            - 网络层的另一个任务就是要选择合适的路由,使源主机运输层所传下来的分组能够交付到目的主机
        - 4. 数据链路层
            - 当发送数据时,数据链路层的任务是将在网络层交下来的IP数据报组装成帧,在两个相邻节点间的链路上传送以帧为单位的数据
            - 每一帧包含数据和必要的控制信息(同步信息,地址信息,差错控制,以及流量控制信息等)
            - 控制信息使接收端能够知道一个帧从哪个比特开始到哪个比特结束
            - 控制信息还使接收端能检测到所收到的帧中有无差错
        - 5. 物理层
            - 物理层就是透明的传输比特流
            - 物理层上所传输数据的单位是比特
            - 传递信息所利用的是一些物理媒体
            - 双绞线,同轴电缆,光缆等并不在物理层之内而是在物理层的下面,因此也有人把物理媒体当做第0层
- 简略版
    - 1、输入url
    - 2、解析dns
    - 3、建立tcp连接
    - 4、客户端发送http请求
    - 5、服务器处理请求
    - 6、服务器响应请求
    - 7、浏览器加载渲染html
    - 8、浏览器请求其他在html的资源
#### HTTP的报文结构
- 1、HTTP请求报文：一个HTTP请求报文由请求行、请求头部、空行和请求数据4个部分组成
- 2、HTTP响应报文：HTTP响应也由三个部分组成，分别是：状态行、消息报头、响应正文


#### TCP/IP数据链路层的交互过程
- 网络层等到数据链路层用mac地址作为通信目标,数据包到达网络层准备往数据链路层发送的时候
- 首先会去自己的ARP缓存表(存储ip-mac对应关系)去查找该目标ip的mac地址
- 如果查到了,就将目标ip的mac地址封装到链路层数据包的包头
- 如果没有查到,会发起一个广播:who is xxx tell ip xxx,所有收到的广播机器看这个ip是不是自己的
- 如果是自己的,则以单拨的形式将自己的mac地址回复给请求的机器
#### IP层怎么知道包围应该给哪个应用程序,怎么区分是UDP报文还是TCP报文
- 根据端口区分
- 看ip头中的协议标识字段: 17是udp,16是tcp

## 编程
### 标准数据类型
Python3 中有六个标准的数据类型：

- Number（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Set（集合）
- Dictionary（字典）
Python3 的六个标准数据类型中：

- 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
- 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
### 多态
- 多态：就是可以接收多种类型的参数，返回一种类型的参数
- 同一个行为具有多个不同表现形式或形态的能力
- 多态是指一类事物有多种形态，比如动物类，可以有猫，狗，猪等等。（一个抽象类有多个子类，因而多态的概念依赖于继承)
- 调用不同的子类将会产生不同的行为，而无须明确知道这个子类实际上是什么，这是多态的重要应用场景
- 多态性是 : 一个接口,多种实现
- 多态与多态性是两种概念
    - 多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
    - 在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）。
    - 也就是说，每个对象可以用自己的方式去响应共同的消息。
    - 所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。
- 鸭子类型
### GC
- 引用计数为主，分代回收为辅
- 引用计数：python中一切皆为对象，核心是一个结构体PyObject其中维护了一个int型变量ob_refcnt
- 在python程序内部每创建一个对象，就会将对象分到一代中，每个代就是一个链表，代进行标记-清除的时间  与  代内对象存活时间成正比例关系。
- 当Python运行时，会记录其中分配对象(object allocation)和取消分配对象(object deallocation)的次数，当两者的差值高于某个阈值时就触发GC回收机制
### 装饰器
- 装饰器的定义: 修改其他函数的功能的函数
- 装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
- 它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
- 装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用
- 为已经存在的函数或对象添加额外的功能
- 装饰器接口定义可以更加明确一些，装饰器必须接受一个callable对象，其实它并不关心你返回什么，可以是另外一个callable对象（大部分情况），也可以是其他类对象，比如property
```python
from functools import wraps

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """print log before a function."""
        print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logging
def say(something):
    """say something"""
    print "say {}!".format(something)

print say.__name__  # say
print say.__doc__ # say something````
```
- 不能装饰@staticmethod 或者 @classmethod
    - 只要把你的装饰器放在@staticmethod之前就好了，因为你的装饰器返回的还是一个正常的函数，然后再加上一个@staticmethod是不会出问题的 
- 优化装饰器代码
```python
# decorator.py是一个非常简单的装饰器加强包。你可以很直观的先定义包装函数wrapper()，
# 再使用decorate(func, wrapper)方法就可以完成一个装饰器
from decorator import decorate

def wrapper(func, *args, **kwargs):
    """print log before a function."""
    print("[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__))
    return func(*args, **kwargs)

def logging(func):
    return decorate(func, wrapper)  # 用wrapper装饰func
```
```python
# @decorator装饰器来完成你的装饰器
from decorator import decorator

@decorator
def logging(func, *args, **kwargs):
    print("[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__))
    return func(*args, **kwargs)
```
```python
# wrapt是一个功能非常完善的包，用于实现各种你想到或者你没想到的装饰器。
# 使用wrapt实现的装饰器你不需要担心之前inspect中遇到的所有问题，因为它都帮你处理了，甚至inspect.getsource(func)也准确无误
import wrapt

# without argument in decorator
@wrapt.decorator
def logging(wrapped, instance, args, kwargs):  # instance is must
    print "[DEBUG]: enter {}()".format(wrapped.__name__)
    return wrapped(*args, **kwargs)

@logging
def say(something): pass
# 带参数的warpt
def logging(level):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print "[{}]: enter {}()".format(level, wrapped.__name__)
        return wrapped(*args, **kwargs)
    return wrapper

@logging(level="INFO")
def do(work): pass
```
#### 闭包
- 在一些语言中，在函数中可以（嵌套）定义另一个函数时，如果内部的函数引用了外部的函数的变量，则可能产生闭包。
- 闭包可以用来在一个函数与一组“私有”变量之间创建关联关系。在给定函数被多次调用的过程中，这些私有变量能够保持其持久性。
- 闭包理解成轻量级的接口封装
- ### 进程和线程的定义,使用场景
- 进程是分配资源的基本单位;线程是系统调度和分派的基本单位
- 属于同一进程的线程,堆是共享的,栈是私有的
- 属于同一进程的所有线程都具有相同的地址空间
- 计算密集型任务用多进程
- IO密集型用多线程
- Python有GIL,同一时刻一个进程只能有一个线程获取CPU的执行,所以对于计算密集型并无实际作用
- 多进程的优点
    - 编程相对容易,通常不需要考虑锁和同步资源的问题
    - 更强的容错性,比起多线程,一个进程崩溃了不会影响其他进程
    - 有内核保证的隔离: 数据和错误的隔离
- 多线程的优点
    - 创建速度快,方便高效的数据共享;多线程间可以共享同一虚拟地址空间;多进程间数据共享需要用到共享内存,信号量等IPC技术
    - 较轻的上下文切换开销,不用切换地址空间,不用更改寄存器,不用刷新TLB
    - 提供非均质的服务
---
## 数据库
### 聚簇索引与非聚簇索引
- 聚簇索引: 将数据存储与索引放到了一起,找到索引也就找到了数据
- 非聚簇索引: 将数据存储与索引分开的结果,索引结构的叶子节点指向了数据的对应行
- myisam通过key_buffer把索引先缓存到内存中，当需要访问数据时（通过索引访问数据），在内存中直接搜索索引，然后通过索引找到磁盘相应数据，这也就是为什么索引不在key buffer命中时，速度慢的原因
- 澄清一个概念：innodb中，在聚簇索引之上创建的索引称之为辅助索引，辅助索引访问数据总是需要二次查找，非聚簇索引都是辅助索引，像复合索引、前缀索引、唯一索引，辅助索引叶子节点存储的不再是行的物理位置，而是主键值
- 聚簇索引默认是主键，如果表中没有定义主键，InnoDB 会选择一个唯一的非空索引代替。如果没有这样的索引，InnoDB 会隐式定义一个主键来作为聚簇索引。InnoDB 只聚集在同一个页面中的记录。包含相邻健值的页面可能相距甚远
### 数据库设计的三大范式
- 第一范式: 确保每列保持原子性(所有字段值都是不可分解的原子值)
- 第二范式: 确保表中的每列都和主键相关(在一个数据库表中,一个表中只能保存一种数据,不可以把多种数据保存在同一张数据库表中)
- 第三范式: 确保每列都和主键直接相关,而不是间接相关
---
# 功能
---
# 接口
### 接口测试常用测试点
- 接口测试是测试系统组件间接口的一种测试
- 接口测试主要用于检测外部系统与系统之间以及内部各个子系统之间的交互点
- 测试的重点是要检查数据的交换,传递和控制管理的过程,以及系统间的相互逻辑依赖关系等
#### 测试策略
- 接口测试也是属于功能测试,因此跟以往的功能测试流程并没有太大区别,测试流程依旧是
    - 评审测试接口文档(需求文档)
    - 根据接口文档编写测试用例(等价类,边界值)
    - 执行测试,查看不同的参数请求,接口的返回的数据是否达到预期
#### 测试用例考虑的维度
##### 功能测试
- 接口的功能是否正确实现
- 接口是否安装设计文档中来实现
    - username参数写成了user,就不符合需求,接口文档在整个开发中都需要使用,所以接口的实际的设计要与接口设计文档中保持一致
- 逻辑业务
    - 是否有依赖业务,比如查看订单,需要用户先登录
    - 业务逻辑测试: 传递正确的参数,返回的结果是否正确,与数据库或者redis一致;增删改的操作,需要看数据库是否同步了这些操作
- 错误码测试
    - 通用的错误码与业务错误码是否能够清晰的说明调用问题,错误码能否尽可能全的覆盖所有的情况
    - 返回值测试: 返回值除了内容需要时正确的,还需要保证类型也是正确的,保证调用方拿到这些参数能够正确的解析(参数边界值,等价类)
- json格式测试
    - 接口的入参数是传递json串,需要去测试传递非json串,程序是否正确处理,返回相应的error code
- 默认值测试
    - 非必填参数会有一些默认值,比如说一个查询接口,参数page_size为返回的查询结果,默认为10,那么久需要有一个case来覆盖这个场景
- 异常测试
    - 参数异常
        - 关键字参数: 将参数写为开发语言中的关键字
        - 参数为空
        - 多或少参数
        - 错误参数: 参数名写错,看是否能返回相应的error code
    - 数据异常
        - 关键字数据: 将参数的值填为开发语言中的关键字
        - 数据为空
        - 长度不一致,数据库中每个字段都设置有字段长度,填写不符合的长度进行验证
        - 错误数据: 将参数的值任意填写,填写不存在的数值
        - 异常类型测试: int类型,传入string
##### 兼容性测试
- 接口进行了调整,前端没有进行变更,这个时候就需要验证新的接口是否满足旧的调用方式
##### 性能测试
- 响应时间
- 吞吐量
- 并发用户数
- 占用内存,CPU
##### 安全测试
- 敏感信息是否加密
- 必要参数是否后端也进行校验
- 接口是否防止恶意请求(SQL注入,请求频率)
- cookie: 将header中的cookie修改或者删除后,看是否能返回相应的error code
- header: 删除或修改header中的部分参数值,是否能返回相应的error code
- 鉴权信息(不带或者鉴权信息错误)
---
# 性能
## 性能指标
### QPS
- Queries per Secone(每秒处理请求数)
- QPS = fetchs / 处理时间
### RPS
- Requests Per Second: 指客户端每秒发出的请求数
- 吞吐率 = 总请求数 / 处理这些请求的总完成时间
- Requests per second = Complete requests / Time taken for tests
### TPS
- Transactions Per Second: 即服务器每秒处理的事务数
- 业务TPS = CAPS × 每个呼叫平均TPS
- CAPS:  Call Attempts Per Second （每秒建立呼叫数量）
### RT
- Reponse Time（响应时间），从发起请求到完全接收到应答的时间消耗
## 其他概念
### 并发数
- 同时访问服务器站点的连接数
### 并发连接数
- 并发连接数就是服务器某个时刻所接受的请求数目，也就是某个时刻所接受的会话数目
### 并发用户数
- 一个用户可能产生多个会话，所以并发用户数和并发连接数并不重复。并发用户数是指服务器某个时刻所能接受的用户数
### 线程数
- 程序运行中消耗cpu的线程数，在正常消耗范围内线程数越大越好
### 吞吐量
- 吞吐量，是指在一次性能测试过程中网络上传输的数据量的总和
# 常见用例设计场景
## 排队打车
## 微信聊天界面
## 电商秒杀系统(限时限量)
# 自动化
## 如何度量你的自动化测试方案/工程效能工具的成本,收益
- 自动化的收益 = 迭代次数 * (全手动执行成本 - 维护成本) - 首次自动化成本
- 自动化的收益与迭代次数成正比
- 自动化收益可能为负数：即当自动化成本和维护成本比手动执行成本还高时
- 很多时候自动化成本并不比手动成本高，但是维护成本很高
- 自动化优点
    - 1、减少测试工作量 
    - 2、提高产品质量
    - 3、迭代周期的缩短，是可以缩短项目周期
- 片面追求自动化的资源节省，或者要求精确量化自动化的收益，都不可取
- 什么项目适合自动化
    -  1、回归测试为主，（需要长期维护的项目）
    -  2、接口比较稳定的产品，同上
    -  3、手动测试特别费时费力，甚至无法达到测试目的的项目。比如压力测试，大数据或者大量重复数据测试，必须有自动化工具的支持
- 自动化的介入时间点
    - 1、项目的初期可能不太适合自动化，（项目修改频繁，维护成本高）
---
# 算法
## 排序
- 排序算法可以分为内部排序和外部排序,内部排序是数据记录在内存中进行的排序
### 冒泡排序

--- 
# 问题定位
### 从程序设计角度来说，群发微信红包的时候，每个人领取到的金额跟红包金额对不上的话，有可能代码哪里出现了问题
#### 问题刨析
- 这是一个范围比较广的问题，但提供的信息比较少，不知道有没有深入了解问题，比如将问题展开讨论，会有 n 种结果，我猜想面试官想考察你思考问题是否全面(主动询问相关细节)
#### 所有人红包领取的总额是红包金额吗？
- 是
    - 转账系统和红包分发系统出现交互问题。
        - 每个人收到的红包金额与红包分发的金额对应，即张三的红包发到了王五，王五的红包发到了张三：分发系统没问题，转账系统没问题，红包分发系统计算好金额和对象后，在传递给转账系统时，发生了顺序错乱。

        - 每个人收到的红包金额与红包分发的金额不对应，即红包分发金额 4 + 5 + 6 = 15 ，收到的金额 5 + 5 + 5 = 15：分发系统没问题，转账系统出现转账错误问题。
- 否
    - 转账系统出现转账错误问题
### 外网线上反馈一个问题,复现不了,如何定位
- [外网问题定位](https://blog.csdn.net/QcloudCommunity/article/details/88659155)
- 常见的外网问题成因
    - 后台数据返回异常,或部分数据为空
    - 针对边界情况,页面未做相应的容错措施,导致页面报错
    - 用户的网络环境
    - APP版本问题
    - 通过上一级入口进入页面时,漏传部分参数
    - 与用户特定的操作步骤相关所引发
- 解决措施
    - JS报错,使用sentry监控上报
    - 用户的行为轨迹,使用打点的方式(IndexedDB(500MB),本地缓存,需要排查时使用白名单去捞)
















# 测开
``# 用例设计
- 排队打车进行用例设计