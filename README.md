# Django

一，什么是web框架？

框架，即framework，特指为解决一个开放性问题而设计的具有一定约束性的支撑结构，使用框架可以帮你快速开发特定系统，简单的说，就是你用别人搭建好的舞台来表演。

对于所有的web应用，本质上其实就是socket服务端，用户的浏览器其实就是一个socket客户端。

VIEW:https://github.com/hls1018/Django_1/blob/master/socket_demo1.py

  最简单的web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接受用户请求，从文件中读取HTML，返回。

如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接收HTTP请求，解析HTTP请求，发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读取HTTP规范。

  正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接，HTTP原始请求和响应格式，所以，需要一个统计的接口，这个接口就是wsgi:web server gateway interface.
  
VIEW:

