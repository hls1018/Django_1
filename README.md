# Django

一，什么是web框架？

框架，即framework，特指为解决一个开放性问题而设计的具有一定约束性的支撑结构，使用框架可以帮你快速开发特定系统，简单的说，就是你用别人搭建好的舞台来表演。

对于所有的web应用，本质上其实就是socket服务端，用户的浏览器其实就是一个socket客户端。

VIEW:https://github.com/hls1018/Django_1/blob/master/socket_demo1.py

  最简单的web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接受用户请求，从文件中读取HTML，返回。

如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接收HTTP请求，解析HTTP请求，发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读取HTTP规范。

  正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接，HTTP原始请求和响应格式，所以，需要一个统计的接口，这个接口就是wsgi:web server gateway interface.
  
VIEW:https://github.com/hls1018/Django_1/blob/master/wsgi_demo.py

注意：

整个application（）函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，我们只负责在更高层次上面考虑如何响应请求就可以了。

application（）函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。

Python内置一个wsgi服务器，这个模块叫wsgiref

application（）函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

    //environ:一个包含所有HTTP请求信息的dict对象；
    
    //start_response:一个发送HTTP响应的函数。
    
在application（）函数中，调用：

start_response('200 OK',[('Content-Type','text/htnl')])

就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。start_response（）函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。

通常情况下，都应该把Content-Type 头发送给浏览器。其他很多常用的HTTP Header也应该发送。

然后，函数的返回值返回b'<h1> HELLO ,WEB!</h1>'将作为HTTP响应的body发送给浏览器。

有了wsgi,我们关心的就是如何从environ这个dict对象中拿到HTTP请求信息，然后构造HTML,通过start_response()发送header，最后返回Body.



