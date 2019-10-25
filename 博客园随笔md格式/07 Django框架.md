##### 1. Django ORM查询中select_related和prefetch_related的区别？？
```python
def select_related(self, *fields)
    性能相关：表之间进行join连表操作，一次性获取关联的数据。

    总结：
    1. select_related主要针一对一和多对一关系进行优化。
    2. select_related使用SQL的JOIN语句进行优化，通过减少SQL查询的次数来进行优化、提高性能。

def prefetch_related(self, *lookups)
    性能相关：多表连表操作时速度会慢，使用其执行多次SQL查询在Python代码中实现连表操作。

    总结：
    1. 对于多对多字段（ManyToManyField）和一对多字段，可以使用prefetch_related()来进行优化。
    2. prefetch_related()的优化方式是分别查询每个表，然后用Python处理他们之间的关系。
```
##### 2. Django ORM是什么？
```python
对象关系映射，通过models中的类来对应数据库中的一个表，一个对象对应一个数据行，一个属性对应数据库中的一个字段
```
<img src="https://images2018.cnblogs.com/blog/1353865/201806/1353865-20180620150003416-1374537457.png" alt="对象关系映射" />
##### 3. Django创建项目的命令？
django-admin startproject 项目名称<br />
python manage.py startapp 应用 app 名
##### 4. Django 创建项目后，项目文件夹下的组成部分（对mvt 的理解）？
项目文件夹下的组成部分：<br />
manage.py 是项目运行的入口，指定配置文件路径。<br />
与项目同名的目录，包含项目的配置文件。<br />
`__init__`.py 是一个空文件，作用是这个目录可以被当作包使用,也可以做一些初始化操作。<br />
settings.py 是项目的整体配置文件。<br />
urls.py 是项目的 URL 配置文件。<br />
wsgi.py 是项目与 WSGI 兼容的 Web 服务器。
##### 5. 对 MVC,MVT解读的理解？
M：Model，模型，和数据库进行交互<br />
V：View，视图，负责产生Html页面<br />
C：Controller，控制器，接收请求，进行处理，与M和V进行交互，返回应答。<br />
<img src="https://img-blog.csdnimg.cn/20181108115444362.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RvbWluaWNKaQ==,size_16,color_FFFFFF,t_70" /><br />
1、 用户点击注按钮，将要注册的信息发送给网站服务器。<br />
2、 Controller控制器接收到用户的注册信息，Controller会告诉Model层将用户的注册信息保存到数据库<br />
3、 Model层将用户的注册信息保存到数据库<br />
4、 数据保存之后将保存的结果返回给Model模型，<br />
5、 Model层将保存的结果返回给Controller控制器。<br />
6、 Controller控制器收到保存的结果之后，或告诉View视图，view视图产生一个html页面。<br />
7、 View将产生的Html页面的内容给了Controller控制器。<br />
8、 Controller将Html页面的内容返回给浏览器。<br />
9、 浏览器接受到服务器Controller返回的Html页面进行解析展示。<br />
M：Model，模型，和MVC中的M功能相同，和数据库进行交互。<br />
V：view，视图，和MVC中的C功能相同，接收请求，进行处理，与M和T进行交互，返回应答。<br />
T：Template，模板，和MVC中的V功能相同，产生Html页面<br />
<img src="https://img-blog.csdnimg.cn/20181108115416852.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RvbWluaWNKaQ==,size_16,color_FFFFFF,t_70" /><br />
1、 用户点击注册按钮，将要注册的内容发送给网站的服务器。<br />
2、 View视图，接收到用户发来的注册数据，View告诉Model将用户的注册信息保存进数据库。<br />
3、 Model层将用户的注册信息保存到数据库中。<br />
4、 数据库将保存的结果返回给Model<br />
5、 Model将保存的结果给View视图。<br />
6、 View视图告诉Template模板去产生一个Html页面。<br />
7、 Template生成html内容返回给View视图。<br />
8、 View将html页面内容返回给浏览器。<br />
9、 浏览器拿到view返回的html页面内容进行解析，展示。
##### 6. Django中models利用ORM对Mysql进行查表的语句（多个语句）？
字段查询<br />
all():返回模型类对应表格中的所有数据。<br />
get():返回表格中满足条件的一条数据，如果查到多条数据，则抛异常：MultipleObjectsReturned，<br />
查询不到数据，则抛异常：DoesNotExist。<br />
filter():参数写查询条件，返回满足条件 QuerySet 集合数据。<br />
条件格式：<br />
**模型类属性名**__条件名=值<br />
注意：此处是模型类属性名，不是表中的字段名<br />
关于 filter 具体案例如下：<br />
判等 exact。
```python
 BookInfo.object.filter(id=1) 
 BookInfo.object.filter(id__exact=1)此处的__exact 可以省略 
```
模糊查询 like<br />
例：查询书名包含'传'的图书。contains
```python
1. contains BookInfo.objects.filter(btitle__contains=’传’) 
```
空查询 where 字段名 isnull
```python
1. BookInfo.objects.filter(btitle__isnull=False) 
```
范围查询 where id in (1，3，5)
```python
1. BookInfo.objects.filter(id__in=[1，3，5]) 
```
比较查询 gt lt(less than) gte(equal) lte
```python
1. BookInfo.objects.filter(id__gte=3) 
```
日期查询
```python
1. BookInfo.objects.filter(bpub_date__year = 1980)  
2. BookInfo.objects.filter(bpub_date__gt = date(1980，1，1)) 
```
exclude:返回不满足条件的数据。
```python
3. BookInfo.objects.exclude(id=3) 
```
**F 对象**<br />
作用：用于类属性之间的比较条件。
```python
1. from django.db.models import F 
2. 例：where bread > bcomment BookInfo.objects.filter(bread__gt =F(‘bcomment’)) 
3. 例：BookInfo.objects.filter(bread__gt=F(‘bcomment’)*2) 
```
**Q 对象**<br />
作用：用于查询时的逻辑条件。可以对 Q 对象进行&amp;|~操作。
```python
1. from django.db.models import Q  
2. BookInfo.objects.filter(id__gt=3， bread__gt=30) 
3. BooInfo.objects.filter(Q(id__gt=3) &amp; Q(bread__gt=3)) 
4. 例：BookInfo.objects.filter(Q(id__gt=3) | Q(bread__gt=30)) 
5. 例：BookInfo.objects.filter(~Q(id=3)) 
```
order_by 返回 QuerySet<br />
作用：对查询结果进行排序。
```python
1. 例： BookInfo.objects.all().order_by('id') 
2. 例： BookInfo.objects.all().order_by('-id') 
3. 例：BookInfo.objects.filter(id__gt=3).order_by('-bread') 
```
**聚合函数**<br />
作用：对查询结果进行聚合操作。
```python
1. sum count max min avg 
```
aggregate：调用这个函数来使用聚合。
```python
1. from django.db.models import Sum，Count，Max，Min，Avg 
2. 例：BookInfo.objects.aggregate(Count('id')) 
```
{'id__count': 5} 注意返回值类型及键名
```python
1. 例：BookInfo.objects.aggregate(Sum(‘bread’)) 
```
{‘bread__sum’:120} 注意返回值类型及键名<br />
count 函数<br />
作用：统计满足条件数据的数目。<br />
例：统计所有图书的数目。
```python
1. BookInfo.objects.all().count() 
```
例：统计 id 大于 3 的所有图书的数目。
```python
1. BookInfo.objects.filter(id__gt = 3).count() 

```
##### 模型类关系
**一对多关系**<br />
例：图书类-英雄类<br />
models.ForeignKey() 定义在多的类中。<br />
**2）多对多关系**<br />
例：新闻类-新闻类型类<br />
models.ManyToManyField() 定义在哪个类中都可以。<br />
**3）一对一关系**<br />
例：员工基本信息类-员工详细信息类<br />
models.OneToOneField() 定义在哪个类中都可以。
##### 7. django中间件的使用？
面试官问你Django中间件的时候，我们不应该只是局限于面试官的问题，而应做到举一反三。<br />
面试之前准备一些白纸，在问到一些问题的时候应该用画图的形式展示出来<br />
比如这里问到Django的中间件，我们应该给面试官画出Django的生命周期整体流程图，把中间件作为一部分的回答内容，<br />
这样的好处在于，即展示了你对Django从前到后的流程都很熟悉又回答了面试官的问题，还顺带秀了一把其他技能，一举两得。<br />
中间件介绍:作为Django的门户，一切请求都会先经过中间件才会到达Django后端，所以中间件可以用来做全局方面的一些功能<br />
详细:给我们定义了五个方法
```python
1.def process_request(request):
    pass
2.def process_view(request):
    pass
3.def process_template_response(request):
    pass
4.def process_exception(request):
    pass
5.def process_response(request):
    pass

```
这些内容应该做到快速回答，不要"慢条斯理"的，搞IT的都很忙好吧，知识点一定要掌握牢固，脱口而出<br />
一定要记住你是需要在有限的时间内将自己的看家本领不遗余力的倾囊而出
<img src="F:\QQPCmgr\Temp\1543066336530.png" alt="1543066336530" />
##### 8. 谈一下你对uWSGI和 nginx的理解？
1.uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。WSGI是一种Web服务器网关接口。它是一个Web服务器（如nginx，uWSGI等服务器）与web应用（如用Flask框架写的程序）通信的一种规范。<br />
要注意 WSGI / uwsgi / uWSGI 这三个概念的区分。<br />
WSGI是一种通信协议。<br />
uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。<br />
uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。<br />
**2. nginx是一个开源的高性能的HTTP服务器和反向代理：**<br />
1.作为web服务器，它处理静态文件和索引文件效果非常高；<br />
2.它的设计非常注重效率，最大支持5万个并发连接，但只占用很少的内存空间；<br />
3.稳定性高，配置简洁；<br />
4.强大的反向代理和负载均衡功能，平衡集群中各个服务器的负载压力应用。
##### 9. 说说nginx和uWISG 服务器之间如何配合工作的？
首先浏览器发起http请求到nginx服务器，Nginx根据接收到请求包，进行url分析，判断访问的资源类型，如果是静态资源，直接读取静态资源返回给浏览器，如果请求的是动态资源就转交给uwsgi服务器，uwsgi服务器根据自身的uwsgi和WSGI协议，找到对应的Django框架，Django框架下的应用进行逻辑处理后，将返回值发送到uwsgi服务器，然后uwsgi服务器再返回给nginx，最后nginx将返回值返回给浏览器进行渲染显示给用户。 如果可以，画图讲解效果更佳，可以 将下面的图画给面试官。<br />
<img src="https://img-blog.csdnimg.cn/20181108115344784.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RvbWluaWNKaQ==,size_16,color_FFFFFF,t_70" />
##### 10. django开发中数据库做过什么优化?
1.设计表时，尽量少使用外键，因为外键约束会影响插入和删除性能；<br />
2.使用缓存，减少对数据库的访问；<br />
3.在orm框架下设置表时，能用varchar确定字段长度时，就别用text；<br />
4.可以给搜索频率高的字段属性，在定义时创建索引；<br />
5.Django orm框架下的Querysets 本来就有缓存的；<br />
6.如果一个页面需要多次连接数据库，最好一次性取出所有需要的数据，减少对数据库的查询次数；<br />
7.若页面只需要数据库里某一个两个字段时，可以用QuerySet.values()；<br />
8.在模板标签里使用with标签可以缓存Qset的查询结果。
##### 11. 验证码过期时间怎么设置？
将验证码保存到数据库或session，设置过期时间为1分钟，然后页面设置一个倒计时(一般是前端js实现 这个计时)的展示，一分钟过后再次点击获取新的信息。
##### 12. Python中三大框架各自的应用场景？
django：主要是用来搞快速开发的，他的亮点就是快速开发，节约成本，正常的并发量不过10000，如果要实现高并发的话，就要对django进行二次开发，比如把整个笨重的框架给拆掉，自己写socket实现http的通信，底层用纯c，c++写提升效率，ORM框架给干掉，自己编写封装与数据库交互的框<br />
架，因为啥呢，ORM虽然面向对象来操作数据库，但是它的效率很低，使用外键来联系表与表之间的查询；<br />
flask：轻量级，主要是用来写接口的一个框架，实现前后端分离，提升开发效率，Flask本身相当于一个内核，其他几乎所有的功能都要用到扩展（邮件扩展Flask-Mail，用户认证Flask-Login），都需要用第三方的扩展来实现。比如可以用Flask-extension加入ORM、窗体验证工具，文件上传、身份验<br />
证等。Flask没有默认使用的数据库，你可以选择MySQL，也可以NoSQL。<br />
其 WSGI 工具箱采用 Werkzeug（路由模块），模板引擎则使用 Jinja2。这两个也是Flask框架的核心。Python最出名的框架要数Django，此外还有Flask、Tornado等框架。虽然Flask不是最出名的框架，但是Flask应该算是最灵活的框架之一，这也是Flask受到广大开发者喜爱的原因。<br />
Tornado： Tornado是一种 Web 服务器软件的开源版本。Tornado 和现在的主流 Web 服务器框架（包括大多数 Python 的框架）有着明显的区别：它是非阻塞式服务器，而且速度相当快。 得利于其非阻塞的方式和对epoll的运用，Tornado 每秒可以处理数以千计的连接，因此 Tornado 是实时 Web 服务的一个 理想框架。
##### 13. django如何提升性能（高并发）？
对一个后端开发程序员来说，提升性能指标主要有两个一个是并发数，另一个是响应时间网站性能的优化一般包括web前端性能优化，应用服务器性能优化，存储服务器优化。<br />
对前端的优化主要有：<br />
1.减少http请求，减少数据库的访问量，比如使用雪碧图。<br />
2.使用浏览器缓存，将一些常用的css，js，logo图标，这些静态资源缓存到本地浏览器，通过设置http头中的cache-control和expires的属性，可设定浏览器缓存，缓存时间可以自定义。<br />
3.对html，css，javascript文件进行压缩，减少网络的通信量。<br />
对我个人而言，我做的优化主要是以下三个方面：<br />
1.合理的使用缓存技术，对一些常用到的动态数据，比如首页做一个缓存，或者某些常用的数据做<br />
个缓存，设置一定得过期时间，这样减少了对数据库的压力，提升网站性能。<br />
2.使用celery消息队列，将耗时的操作扔到队列里，让worker去监听队列里的任务，实现异步操<br />
作，比如发邮件，发短信。<br />
3.就是代码上的一些优化，补充：nginx部署项目也是项目优化，可以配置合适的配置参数，提升效率，增加并发量。<br />
4.如果太多考虑安全因素，服务器磁盘用固态硬盘读写，远远大于机械硬盘，这个技术现在没有普及，主要是固态硬盘技术上还不是完全成熟， 相信以后会大量普及。<br />
5.另外还可以搭建服务器集群，将并发访问请求，分散到多台服务器上处理。<br />
6.最后就是运维工作人员的一些性能优化技术了。
##### 14. 什么是restful api，谈谈你的理解?
上来先给面试官扔出一手Django的restgramework源码(这一块知识课下一定要自己看着源码走三遍做到烂熟于心，看着面试官的眼睛快速自信的说出。这一手源码扔出来之后，面试已经成功一半)<br />
REST:Representational State Transfer的缩写，翻译：“具象状态传输”。一般解释为“表现层状态转换”。<br />
REST是设计风格而不是标准。是指客户端和服务器的交互形式。我们需要关注的重点是如何设计REST风格的网络接口。<br />
REST的特点：<br />
1.具象的。一般指表现层，要表现的对象就是资源。比如，客户端访问服务器，获取的数据就是资源。比如文字、图片、音视频等。<br />
2.表现：资源的表现形式。txt格式、html格式、json格式、jpg格式等。浏览器通过URL确定资源的位置，但是需要在HTTP请求头中，用AcceptContent-Type字段指定，这两个字段是对资源表现的描述。<br />
3.状态转换：客户端和服务器交互的过程。在这个过程中，一定会有数据和状态的转化，这种转化叫做状态转换。其中，GET表示获取资源，POST表示新建资源，PUT表示更新资源，DELETE表示删除资源。HTTP协议中最常用的就是这四种操作方式。<br />
RESTful架构：<br />
1.每个URL代表一种资源；<br />
2.客户端和服务器之间，传递这种资源的某种表现层；<br />
3.客户端通过四个http动词，对服务器资源进行操作，实现表现层状态转换。
##### 14.1 如何设计符合 RESTful 风格的 API
**一、域名：**<br />
将api部署在专用域名下：<br />
http://api.example.com<br />
或者将api放在主域名下：<br />
http://www.example.com/api/<br />
**二、版本：**<br />
将API的版本号放在url中。<br />
http://www.example.com/app/1.0/info<br />
http://www.example.com/app/1.2/info<br />
**三、路径：**<br />
路径表示API的具体网址。每个网址代表一种资源。 资源作为网址，网址中不能有动词只能有名词，一般名词要与数据库的表名对应。而且名词要使用复数。<br />
错误示例：<br />
http://www.example.com/getGoods<br />
http://www.example.com/listOrders<br />
正确示例：<br />
获取单个商品<br />
http://www.example.com/app/goods/1<br />
获取所有商品<br />
http://www.example.com/app/goods<br />
**四、使用标准的HTTP方法：**<br />
对于资源的具体操作类型，由HTTP动词表示。 常用的HTTP动词有四个。<br />
GET SELECT ：从服务器获取资源。<br />
POST CREATE ：在服务器新建资源。<br />
PUT UPDATE ：在服务器更新资源。<br />
DELETE DELETE ：从服务器删除资源。<br />
示例：<br />
获取指定商品的信息<br />
GET http://www.example.com/goods/ID<br />
新建商品的信息<br />
POST http://www.example.com/goods<br />
更新指定商品的信息<br />
PUT http://www.example.com/goods/ID<br />
删除指定商品的信息<br />
DELETE http://www.example.com/goods/ID<br />
**五、过滤信息：**<br />
如果资源数据较多，服务器不能将所有数据一次全部返回给客户端。API应该提供参数，过滤返回结果。 实例：<br />
指定返回数据的数量<br />
http://www.example.com/goods?limit=10<br />
指定返回数据的开始位置<br />
http://www.example.com/goods?offset=10<br />
指定第几页，以及每页数据的数量<br />
http://www.example.com/goods?page=2&amp;per_page=20<br />
**六、状态码：**<br />
服务器向用户返回的状态码和提示信息，常用的有：<br />
200 OK ：服务器成功返回用户请求的数据<br />
201 CREATED ：用户新建或修改数据成功。<br />
202 Accepted：表示请求已进入后台排队。<br />
400 INVALID REQUEST ：用户发出的请求有错误。<br />
401 Unauthorized ：用户没有权限。<br />
403 Forbidden ：访问被禁止。<br />
404 NOT FOUND ：请求针对的是不存在的记录。<br />
406 Not Acceptable ：用户请求的的格式不正确。<br />
500 INTERNAL SERVER ERROR ：服务器发生错误。<br />
**七、错误信息：**<br />
一般来说，服务器返回的错误信息，以键值对的形式返回。<br />
{<br />
error: 'Invalid API KEY'<br />
}<br />
**八、响应结果：**<br />
针对不同结果，服务器向客户端返回的结果应符合以下规范。<br />
返回商品列表<br />
GET http://www.example.com/goods<br />
返回单个商品<br />
GET http://www.example.com/goods/cup<br />
返回新生成的商品<br />
POST http://www.example.com/goods<br />
返回一个空文档<br />
DELETE http://www.example.com/goods<br />
**九、使用链接关联相关的资源：**<br />
在返回响应结果时提供链接其他API的方法，使客户端很方便的获取相关联的信息。<br />
**十、其他：**<br />
服务器返回的数据格式，应该尽量使用JSON，避免使用XML。
##### 13. 什么csrf攻击原理？如何解决？
<img src="https://img-blog.csdnimg.cn/20181108115146482.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RvbWluaWNKaQ==,size_16,color_FFFFFF,t_70" /><br />
简单来说就是: 你访问了信任网站A，然后A会用保存你的个人信息并返回给你的浏览器一个cookie，然后呢，在cookie的过期时间之内，你去访问了恶意网站B，它给你返回一些恶意请求代码，要求你去访问网站A，而你的浏览器在收到这个恶意请求之后，在你不知情的情况下，会带上保存在本地浏览器的cookie信息去访问网站A，然后网站A误以为是用户本身的操作，导致来自恶意网站C的攻击代码会被执：发邮件，发消息，修改你的密码，购物，转账，偷窥你的个人信息，导致私人信息泄漏和账户财产安全收到威胁
##### 14. 启动Django服务的方法？
runserver 方法是调试 Django 时经常用到的运行方式，它使用 Django 自带的WSGI Server 运行，主要在测试和开发中使用，并且 runserver 开启的方式也是单进程 。
##### 15. 怎样测试django框架中的代码？
在单元测试方面，Django继承 python 的 unittest.TestCase 实现了自己的<br />
django.test.TestCase，编写测试用例通常从这里开始。测试代码通常位于app 的 tests.py 文件中(也可以在 models.py 中编写，一般不建议）。在Django 生成的 depotapp 中，已经包含了这个文件，并且其中包含了一个测试 用例的样例：
```python
1. python manage.py test：执行所有的测试用例 
2. python manage.py test app_name， 执行该 app 的所有测试用例 
3. python manage.py test app_name.case_name: 执行指定的测试用例 

```
一些测试工具：unittest 或者 pytest
##### 16. 有过部署经验？用的什么技术？可以满足多少压力？
1.有部署经验，在阿里云服务器上部署的<br />
2.技术有：nginx + uwsgi 的方式来部署 Django 项目<br />
3.无标准答案（例：压力测试一两千）
##### 17. Django中哪里用到了线程?哪里用到了协程?哪里用到了进程？
1.Django 中耗时的任务用一个进程或者线程来执行，比如发邮件，使用celery。<br />
2.部署 django项目的时候，配置文件中设置了进程和协程的相关配置。
##### 18. django关闭浏览器，怎样清除 cookies 和 session？
设置Cookie
```python
1. def cookie_set(request): 
2.     response = HttpResponse("<h1>设置Cookie，请查看响应报文头</h1>") 
3.     response.set_cookie('h1', 'hello django') 
4.     return response 

```
读取Cookie
```python
1. def cookie_get(request):  
2.     response = HttpResponse("读取Cookie，数据如下：<br>") 
3.     if request.COOKIES.has_key('h1'): 
4.         response.write('<h1>' + request.COOKIES['h1'] + '</h1>') 
5.     return response 

```
以键值对的格式写会话。
```python
1. request.session['键']=值 

```
根据键读取值。
```python
1. request.session.get('键',默认值) 

```
清除所有会话，在存储中删除值部分。
```python
1. request.session.clear() 

```
清除会话数据，在存储中删除会话的整条数据。
```python
1. request.session.flush() 

```
删除会话中的指定键及值，在存储中只删除某个键及对应的值。
```python
1. del request.session['键'] 

```
设置会话的超时时间，如果没有指定过期时间则两个星期后过期。<br />
如果value是一个整数，会话将在value秒没有活动后过期。<br />
如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。<br />
如果value为None，那么会话在两周后过期。
```python
1. request.session.set_expiry(value) 

```
Session 依赖于 Cookie，如果浏览器不能保存 cookie 那么 session 就失效了。因为它需要浏览器的 cookie 值去 session 里做对比。session就是用来在服务器端保存用户的会话状态。<br />
cookie 可以有过期时间，这样浏览器就知道什么时候可以删除 cookie了。 如果 cookie 没有设置过期时间，当用户关闭浏览器的时候，cookie 就自动过期了。你可以改变 SESSION_EXPIRE_AT_BROWSER_CLOSE 的设置来控制session 框架的这一行为。缺省情况下， SESSION_EXPIRE_AT_BROWSER_CLOSE设置为 False ，这样，会话 cookie 可以在用户浏览器中保持有效达SESSION_COOKIE_AGE 秒（缺省设置是两周，即 1，209，600 秒）如果你不想用户每次打开浏览器都必须重新登陆的话，用这个参数来帮你。如果SESSION_EXPIRE_AT_BROWSER_CLOSE<br />
设置为 True，当浏览器关闭时，Django 会使 cookie 失效。<br />
SESSION_COOKIE_AGE：设置 cookie 在浏览器中存活的时间。
##### 19. 有用过Django REST framework 吗？
面试就喜欢面试官问这种问题，前面就已经说过了，这种问题一提出来，我们内心是高兴的一笔的，正好将我们学的Django restframework源码带面试官走一波，之后可以再补充一点Django的其他源码，比如ORM源码，settings源码，<br />
admin源码...最后一定要记住，你要展示出你不仅阅读过源码还基于源码在自己的实际项目中参考借鉴过。如果把面试比作考试题满分100的话，这一题就是送分的30分大题！！！
##### 20. Celery分布式任务队列？
情景：用户发起request，并等待response返回。在本些views中，可能需要执行一段耗时的程序，那么用户就会等待很长时间，造成不好的用户体验，比如发送邮件、手机验证码等。 使用celery后，情况就不一样了。解决：将耗时的程序放到celery中执行。将多个耗时的任务添加到队列queue中，也就是用redis实现broker中间人，然后用多个worker去监听队列 里的任务去执行。<br />
<img src="https://img-blog.csdnimg.cn/20181108115107579.png" />

- 任务task：就是一个Python函数。
- 队列queue：将需要执行的任务加入到队列中。
- 工人worker：在一个新进程中，负责执行队列中的任务。
- 代理人broker：负责调度，在布置环境中使用redis。<br />
正向代理：请求经过代理服务器从局域网发出，然后到达互联网上的服务器。<br />
特点：服务端并不知道真正的客户端是谁。<br />
反向代理：请求从互联网发出，先进入代理服务器，再转发给局域网内的服务器。<br />
特点：客户端并不知道真正的服务端是谁。<br />
区别：正向代理的对象是客户端。反向代理的对象是服务端。

##### 21. 简述Django下的（内建的）缓存机制?
Django提供6种缓存方式:<br />
开发调试<br />
内存<br />
文件<br />
数据库<br />
Memcache缓存(python-memcached模块)<br />
Memcache缓存(pylibmc模块)<br />
除此之外还可使用redis缓存<br />
由于Django是动态网站，所有每次请求均会去数据进行相应的操作，当程序访问量大时，耗时必然会更加明显，<br />
最简单解决方式是使用：缓存，缓存将一个某个views的返回值保存至内存或者memcache中，5分钟内(默认配置)再有人来访问时，<br />
则不再去执行view中的操作，而是直接从内存或者Redis中之前缓存的内容拿到，并返回。<br />
这里可以向面试官介绍一下前面提到的Django中间件配合缓存协同工作的机制
##### 22. 对cookie与session的了解？他们能单独用吗？
首先需要搞清楚的是session是存储在服务器上的，cookie是存储在客户端浏览器上的两者是相辅相成的用户首次访问服务器，服务器会为每个用户单独创建一个session对象(HttpSession)，<br />
并为每个session分配唯一一个id(sessionId)，sessionId通过cookie保存到用户端，当用户再次访问服务器时，需将对应的sessionId携带给服务器，服务器通过这个唯一sessionId就可以找到用户对应的session对象，从而达到管理用户状态
##### 23. Django里QuerySet的get和filter方法的区别？
**1) 输入参数**<br />
get 的参数只能是model中定义的那些字段，只支持严格匹配。<br />
filter的参数可以是字段，也可以是扩展的 where查询关键字，如 in，like 等。<br />
**2) 返回值**<br />
get返回值是一个定义的 model 对象。<br />
filter返回值是一个新的 QuerySet 对象，然后可以对 QuerySet 在进行查询返回新的 QuerySet 对象，支持链式操作，QuerySet 一个集合对象，可使用迭代或者遍历，切片等，但是不等于 list 类型(使用一定要注意)。<br />
**3) 异常**<br />
get只有一条记录返回的时候才正常，也就说明 get 的查询字段必须是主键或者唯一约束的字段。当返回多条记录或者是没有找到记录的时候都会抛出异常。 filter 有没有匹配的记录都可以
##### 24. django 中当一个用户登录 A 应用服务器（进入登录状态），然后下次请求被 nginx 代理到 B 应用服务器会出现什么影响？
如果用户在A应用服务器登陆的session数据没有共享到B应用服务器，那么之前的登录状态就没有了。
**1.安装django-cors-headers，之后在settings.py中配置**
```python
pip install django-cors-headers

```
```python
INSTALLED_APPS = [
 ...
 'corsheaders'，
 ...
 ] 
 
MIDDLEWARE_CLASSES = (
 ...
 'corsheaders.middleware.CorsMiddleware',
 'django.middleware.common.CommonMiddleware', # 注意顺序
 ...
)
#跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
 '*'
)
 
CORS_ALLOW_METHODS = (
 'DELETE',
 'GET',
 'OPTIONS',
 'PATCH',
 'POST',
 'PUT',
 'VIEW',
)
 
CORS_ALLOW_HEADERS = (
 'XMLHttpRequest',
 'X_FILENAME',
 'accept-encoding',
 'authorization',
 'content-type',
 'dnt',
 'origin',
 'user-agent',
 'x-csrftoken',
 'x-requested-with',
 'Pragma',
)

```
**2.使用JSONP**<br />
使用Ajax获取json数据时，存在跨域的限制。不过，在Web页面上调用js的script脚本文件时却不受跨域的影响，JSONP就是利用这个来实现跨域的传输。因此，我们需要将Ajax调用中的dataType从JSON改为JSONP（相应的API也需要支持JSONP）格式。<br />
JSONP只能用于GET请求。<br />
**3.直接修改Django中的views.py文件**<br />
修改views.py中对应API的实现函数，允许其他域通过Ajax请求数据：
```python
def myview(_request):
    response = HttpResponse(json.dumps({“key”: “value”, “key2”: “value”}))
    response[“Access-Control-Allow-Origin”] = “*”
    response[“Access-Control-Allow-Methods”] = “POST, GET, OPTIONS”
    response[“Access-Control-Max-Age”] = “1000”
    response[“Access-Control-Allow-Headers”] = “*”
return response

```
##### 26. Django对数据查询结果排序怎么做，降序怎么做，查询大于某个字段怎么做?

- 排序使用order_by()
- 降序需要在排序字段名前加-
- 查询字段大于某个值：使用filter(字段名_gt=值)<br />
更多骚操作:

```python
models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
 
models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in
 
models.Tb1.objects.filter(name__contains="ven")  # 获取name字段包含"ven"的
models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
 
models.Tb1.objects.filter(id__range=[1, 3])      # id范围是1到3的，等价于SQL的bettwen and
 
类似的还有：startswith，istartswith, endswith, iendswith　

date字段还可以：
models.Class.objects.filter(first_day__year=2017)

```
##### 27. 生成迁移文件和执行迁移文件的命令是什么？
```python
python manage.py makemigrations 
python manage.py migrate 

```
##### 28.uWSGI与uwsgi区别
uWSGI是一个 Web 服务器，它实现了WSGI 协议、uwsgi、http 等协议。注意 uwsgi 是一种通信协议，而 uWSGI 是实现 uwsgi 协议和 WSGI 协议的Web 服务器。uWSGI 具有超快的性能、低内存占用和多app 管理等优点，并且搭配着 Nginx就是一个生产环境了，能够将用户访问请求与应用 app 隔离开，实现真正的部署。相比来讲，支持的并发量更高，方便管理多进程，发挥多核的优势，提升性能。
##### 29. apache和nginx的区别？(2018-4-16-lxy)
Nginx相对Apache的优点：<br />
轻量级，同样起web 服务，比apache 占用更少的内存及资源；<br />
抗并发，nginx 处理请求是异步非阻塞的，支持更多的并发连接，而apache 则是阻塞型的，在高并发下nginx 能保持低资源低消耗高性能； 配置简洁； 高度模块化的设计，编写模块相对简单；<br />
社区活跃。<br />
Apache相对Nginx的优点：<br />
rewrite ，比nginx 的rewrite 强大；<br />
模块超多，基本想到的都可以找到；<br />
少bug ，nginx 的bug 相对较多； 超稳定。
##### 30. git 常用命令? (2018-4-23-lxy)

- git clone 克隆指定仓库
- git status 查看当前仓库状态
- git diff 比较版本的区别
- git log 查看 git 操作日志
- git reset 回溯历史版本
- git add 将文件添加到暂存区
- git commit 将文件提交到服务器
- git checkout 切换到指定分支
- git rm 删除指定文件<br />
(命令好记，实际操作就相对较难，平时应有意识地去锻炼使用git管理我们的代码仓库)

##### 31. 什么是gitlab,github和gitlab的区别?
**参考博客:**https://blog.csdn.net/zhang_oracle/article/details/77317717
##### 32. git中 .gitignore文件的作用?
**参考博客:**https://www.cnblogs.com/kevingrace/p/5690241.html
##### 33. HttpRequest和HttpResponse是什么?干嘛用的？
HttpRequest是django接受用户发送多来的请求报文后，将报文封装到HttpRequest对象中去。<br />
HttpResponse 返回的是一个应答的数据报文。render内部已经封装好了HttpResponse类。<br />
视图的第一个参数必须是HttpRequest对象，两点原因：表面上说，他是处理web请求的，所以必须是请求对象，根本上说，他是基于请求的一种web框架，所以，必须是请求对象。 因为view处理的是一个request对象，请求的所有属性我们都可以根据对象属性的查看方法来获取具体的信息：格式：request.属性<br />
request.path 请求页面的路径，不包含域名<br />
request.get_full_path 获取带参数的路径<br />
request.method 页面的请求方式<br />
request.GET GET 请求方式的数据<br />
request.POST POST请求方式的数据<br />
request.COOKIES 获取cookie<br />
request.session 获取session<br />
request.FILES 上传图片（请求页面有enctype="multipart/form-data"属性时FILES才有数据)
##### 34. 什么是反向解析
使用场景：模板中的超链接，视图中的重定向<br />
使用：在定义url时为include定义namespace属性，为url定义name属性<br />
在模板中使用url标签：{% url 'namespace_value:name_value'%}<br />
在视图中使用reverse函数：redirect(reverse('namespce_value:name_value’))<br />
根据正则表达式动态生成地址，减轻后期维护成本。<br />
注意反向解析传参数，主要是在我们的反向解析的规则后面天界了两个参数，两个参数之间使用空格隔开：<a href="{% url 'booktest:fan2' 2 3 %}">位置参数</a>
##### 36.列举常见的请求方法。
```python
GET     请求指定的页面信息，并返回实体主体。
HEAD     类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
POST     向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
PUT     从客户端向服务器传送的数据取代指定的文档的内容。
DELETE      请求服务器删除指定的页面。
CONNECT     HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
OPTIONS     允许客户端查看服务器的性能。
TRACE     回显服务器收到的请求，主要用于测试或诊断。

```
##### 36.列举常见的状态码。
```python
状态代码有三位数字组成，第一个数字定义了响应的类别，共分五种类别:

1xx：指示信息--表示请求已接收，继续处理
2xx：成功--表示请求已被成功接收、理解、接受
3xx：重定向--要完成请求必须进行更进一步的操作
4xx：客户端错误--请求有语法错误或请求无法实现
5xx：服务器端错误--服务器未能实现合法的请求
常见状态码：

200 OK                        //客户端请求成功
400 Bad Request               //客户端请求有语法错误，不能被服务器所理解
401 Unauthorized              //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用 
403 Forbidden                 //服务器收到请求，但是拒绝提供服务
404 Not Found                 //请求资源不存在，eg：输入了错误的URL
500 Internal Server Error     //服务器发生不可预期的错误
503 Server Unavailable        //服务器当前不能处理客户端的请求，一段时间后可能恢复正常
更多状态码http://www.runoob.com/http/http-status-codes.html

```
##### 37.http 和 https 的区别?
```python
http的中文叫做超文本传输协议,它负责完成客户端到服务端的一系列操作,是专门用来传输注入HTML的超媒体文档等web内容的协议,它是基于传输层的TCP协议的应用层协议

https:https是基于安全套接字的http协议,也可以理解为是http+ssl/tls(数字证书)的组合

http和https的区别:

HTTP 的 URL 以 http:// 开头，而 HTTPS 的 URL 以 https:// 开头
HTTP 是不安全的，而 HTTPS 是安全的
HTTP 标准端口是 80 ，而 HTTPS 的标准端口是 443
在 OSI 网络模型中，HTTPS的加密是在传输层完成的,因为SSL是位于传输层的,TLS的前身是SSL,所以同理
HTTP无需认证证书,而https需要认证证书  

```
##### 38.简述 websocket 协议及实现原理。
```python
ebsocket是一种在单个TCP连接上进行全双工通讯的协议，双工（duplex）是指两台通讯设备之间，允许有双向的资料传输。全双工的是指，允许两台设备间同时进行双向资料传输。这是相对于半双工来说的，半双工不能同时进行双向传输，这期间的区别相当于手机和对讲机的区别，手机在讲话的同时也能听到对方说话，对讲机只能一个说完另一个才能说。


```
##### 39.django 中如何实现 websocket?
django实现websocket大致上有两种方式，一种channels，一种是dwebsocket。channels依赖于redis，twisted等，相比之下使用dwebsocket要更为方便一些。
```python
安装
# pip install dwebsocket

配置：

# setting.py
 
INSTALLED_APPS = [
    .....
    .....
    'dwebsocket',
]
 
MIDDLEWARE_CLASSES = [
    ......
    ......
    'dwebsocket.middleware.WebSocketMiddleware'  # 为所有的URL提供websocket，如果只是单独的视图需要可以不选
 
]
WEBSOCKET_ACCEPT_ALL=True   # 可以允许每一个单独的视图实用websockets


简单使用：
模拟文件下载的简单示例

from dwebsocket.decorators import accept_websocket
@accept_websocket
def test(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        return render(request, 'websocket.html')
    else:
        download = Haproxy()
        t = threading.Thread(target=download.run)
        t.start()
        sent = []
        while download.status:
            if len(download.res_dict) > len(sent):
                for i in download.res_dict.keys():
                    if i not in sent:
                        sent.append(i)
                request.websocket.send(str(sent[-1]+str(download.res_dict[sent[-1]])).encode('utf-8'))  # 发送消息到客户端
        if not download.status:
            request.websocket.send('下载完成'.encode('utf-8'))

```
dwebsocket有两种装饰器：require_websocket和accept_websocekt，使用require_websocket装饰器会导致视图函数无法接收导致正常的http请求，一般情况使用accept_websocket方式就可以了，
dwebsocket的一些内置方法：
request.is_websocket（）：判断请求是否是websocket方式，是返回true，否则返回false<br />
request.websocket： 当请求为websocket的时候，会在request中增加一个websocket属性，<br />
WebSocket.wait（） 返回客户端发送的一条消息，没有收到消息则会导致阻塞<br />
WebSocket.read（） 和wait一样可以接受返回的消息，只是这种是非阻塞的，没有消息返回None<br />
WebSocket.count_messages（）返回消息的数量<br />
WebSocket.has_messages（）返回是否有新的消息过来<br />
WebSocket.send（message）像客户端发送消息，message为byte类型
##### 40.Python web 开发中, 跨域问题的解决思路是?
```python
# 方案1.安装django-cors-headers
pip install django-cors-header

配置settings.py文件
 
INSTALLED_APPS = [
    ...
    'corsheaders'，
    ...
 ] 
MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', # 注意顺序
    ...
)
#跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

# 方案2.使用JSONP
使用Ajax获取json数据时，存在跨域的限制。不过，在Web页面上调用js的script脚本文件时却不受跨域的影响，JSONP就是利用这个来实现跨域的传输。因此，我们需要将Ajax调用中的dataType从JSON改为JSONP（相应的API也需要支持JSONP）格式。
JSONP只能用于GET请求。

# 方案3.直接修改Django中的views.py文件

修改views.py中对应API的实现函数，允许其他域通过Ajax请求数据：
def myview(_request):
  response = HttpResponse(json.dumps({“key”: “value”, “key2”: “value”}))
  response[“Access-Control-Allow-Origin”] = “*”
  response[“Access-Control-Allow-Methods”] = “POST, GET, OPTIONS”
  response[“Access-Control-Max-Age”] = “1000”
  response[“Access-Control-Allow-Headers”] = “*”
  return response

```
##### 45.什么是wsgi?
```python
WSGI的全称是Web Server Gateway Interface，翻译过来就是Web服务器网关接口。具体的来说，WSGI是一个规范，定义了Web服务器如何与Python应用程序进行交互，使得使用Python写的Web应用程序可以和Web服务器对接起来。


```
##### 46.列举django的内置组件?
```python
.Admin是对model中对应的数据表进行增删改查提供的组件
.model组件：负责操作数据库
.form组件：1.生成HTML代码2.数据有效性校验3校验信息返回并展示
.ModelForm组件即用于数据库操作,也可用于用户请求的验证  

```
##### 48.django 中 model 的 SlugField 类型字段有什么用途
SlugField 本质上相当于存放字符串，但是在意义上，主要用于把某些字段形成语义化的，可以访问的短网址（slug）字符串。
##### 49.django 中想要验证表单􏰀交是否格式正确需要用到 form 中的那个方法
```python
A.  form.save()
B.  form.save(commit=False)
C.  form.verify()
D.  form.is_valid()   *****

```
##### 50.django 常见的线上部署方式有哪几种?
##### 51.django 对数据查询结果排序怎么做, 降序怎么做?
```python
排序使用order_by()

降序需要在排序字段名前加-

查询字段大于某个值：使用filter(字段名_gt=值)

```
##### 52.下面关于http协议中的get和post方式的区别,那些是错误的?(多选)
```python
A. 他们都可以被收藏, 以及缓存
B. get请求参数放在url中
C. get只用于查询请求,不能用于数据请求
D. get不应该处理敏感数据的请求 

```
##### 53.django 中使用 memcached 作为缓存的具体方法? 优缺点说明?
```python
安装：
  首先要在django运行环境中安装：python-memcached（命令：pip install python-memcached）
1）在Django的settings中设置缓存

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ,'127.0.0.1:11211', # 可以为远程地址和端口，可以设置多个ip
        'TIMEOUT': 86400,  # 1 day,设置成0缓存将失效
        'OPTIONS': {
            'MAX_ENTRIES': 1000, # 高速缓存允许的最大条目数，超出这个数则旧值将被删除. 这个参数默认是300.
            'CULL_FREQUENCY': 3, # 当达到MAX_ENTRIES 的时候,被删除的条目比率。 实际比率是 1 / CULL_FREQUENCY，默认是3
        }
    }
}

2）业务逻辑
#coding=utf-8
def key_hash(value):
    """hash缓存key，防止过长"""
    import hashlib
    return '%s' % hashlib.md5(value).hexdigest()
 
 
def cache(num1, num2):
    """
    :param num1: 获取或者设置cache的标识
    :param num2：获取或者设置cache的标识
    :return: 缓存dict
    """
    from django.core.cache import cache
    import logging
    log = logging.getLogger(__name__)  # 日志
    # 去重并排序，增加缓存命中率
    cache_key = 'num1={num1}&amp;num2={num2}'.format(num1=num1, num2=num2)
    cache_key = key_hash(cache_key)
 
    # in cache, return cache
    if cache.get(cache_key):
        log.debug('cache %s hitting ' % cache_key)
        return cache.get(cache_key)
 
    # not in cache, get result and set cache
    ret = None
    # TODO do something get result
    ret = 'something'
    cache.set(cache_key, ret, 60 * 60 * 24)  # 一天过期
    return ret

```
##### 54.使用Django中modelfilter条件过滤方法,把下边sql语句转化成python 代码
```sql
select * from company where title like "%abc%" or mecount>999 order by createtime desc;

```
##### 55.从输入http://www.baidu.com/到页面返回,中间都是发生了什么?
```python
1、域名解析：
浏览器向DNS获取web服务器 www.baidu.com这个域名的 的ip地址
2、建立TCP连接
浏览器与对应ip地址的服务器进行TCP链接，端口为80
3、浏览器执行HTTP协议，发送GET请求，读取对应文件
4、服务器接收到请求后,返回网页信息 
5.客户端浏览器将这些信息组织成用户可以查看的网页形式

```
##### 56.django 请求的生命周期?
```python
. 当用户在浏览器中输入url时,浏览器会生成请求头和请求体发给服务端
请求头和请求体中会包含浏览器的动作(action),这个动作通常为get或者post,体现在url之中.
. url经过Django中的wsgi,再经过Django的中间件,最后url到过路由映射表,在路由中一条一条进行匹配,
一旦其中一条匹配成功就执行对应的视图函数,后面的路由就不再继续匹配了.
. 视图函数根据客户端的请求查询相应的数据.返回给Django,然后Django把客户端想要的数据做为一个字符串返回给客户端.
. 客户端浏览器接收到返回的数据,经过渲染后显示给用户.

```
##### 57.django 中如何在 model 保存前做一定的固定操作,比如写一句日志?
利用Django的Model的Signal Dispatcher,通过django.db.models.signals.pre_save()方法，在事件发生前，发射触发信号，这一切都被调度中的receiver方法深藏功与名的保存了。<br />
信号的处理一般都写在Model中，举个例子：
```python
import logging
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
class Order(models.Model):
logger = logging.getLogger(__name__)
@receiver(pre_save, sender=Order)
def pre_save_handler(sender, **kwargs):
 logger.debug("{},{}".format(sender, **kwargs))

```
##### django的request对象是在什么时候创建的？
```python
`class WSGIHandler(base.BaseHandler):`
`-------request = self.request_class(environ)`
请求走到WSGIHandler类的时候，执行**cell**方法，将environ封装成了request 

```
##### 58.简述django中间件及其应用场景?
```python
.process_request : 请求进来时,权限认证
.process_view : 路由匹配之后,能够得到视图函数
.process_exception : 异常时执行
.process_template_responseprocess : 模板渲染时执行
.process_response : 请求有响应时执行

```
##### 59.简述 django FBV 和 CBV?
FBV和CBV本质是一样的，基于函数的视图叫做FBV，基于类的视图叫做CBV<br />
在python中使用CBV的优点：

- .提高了代码的复用性，可以使用面向对象的技术，比如Mixin（多继承）
- .可以用不同的函数针对不同的HTTP方法处理，而不是通过很多if判断，提高代码可读性

##### 60.如何给 django CBV 的函数设置添加装饰器?
```python
from django.utils.decorators import method_decorator
        1、给方法加：
            @method_decorator(check_login)
            def post(self, request):
                ...
        2、给dispatch加：
            @method_decorator(check_login)
            def dispatch(self, request, *args, **kwargs):
                ...
        3、给类加：
            @method_decorator(check_login, name="get")
            @method_decorator(check_login, name="post")
            class HomeView(View):
                ... 

```
##### 61.django 如何连接多个数据库并实现读写分离?
在配置文件中增加slave数据库的配置
在Django的配置文件settings.py中,DATABASES中添加代码如下:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 主服务器的运行ip
        'PORT': 3306,   # 主服务器的运行port
        'USER': 'django',  # 主服务器的用户名
        'PASSWORD': 'django',  # 主服务器的密码
        'NAME': 'djangobase'   #  数据表名
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql', 
        'HOST': '127.0.0.1',
        'PORT': 8306,
        'USER': 'django_slave',
        'PASSWORD': 'django_slave',
        'NAME': 'djangobase_slave'
    }
}　　

```
创建数据库操作的路由分类
在项目的utils中创建db_router.py文件,并在该文件中定义一个db类,用来进行读写分离
```python
class MasterSlaveDBRouter(object):
    """数据库主从读写分离路由"""
 
    def db_for_read(self, model, **hints):
        """读数据库"""
        return "slave"
 
    def db_for_write(self, model, **hints):
        """写数据库"""
        return "default"
 
    def allow_relation(self, obj1, obj2, **hints):
        """是否运行关联操作"""
        return True　　

```
配置读写分离路由
在配置文件中增加:
```python
#配置读写分离
DATABASE_ROUTERS = ['项目名.utils.db_router."自定义的类名称"']

```
##### 62.列举 django orm 中你了解的所有方法?
```python
# QuerySet对象的所有方法
  <1> all():                  查询所有结果 
  <2> filter(**kwargs):       它包含了与所给筛选条件相匹配的对象。获取不到返回None
  <3> get(**kwargs):          返回与所给筛选条件相匹配的对象，返回结果有且只有一个。
                              如果符合筛选条件的对象超过一个或者没有都会抛出错误。
  <4> exclude(**kwargs):      它包含了与所给筛选条件不匹配的对象
  <5> order_by(*field):       对查询结果排序
  <6> reverse():              对查询结果反向排序 
  <8> count():                返回数据库中匹配查询(QuerySet)的对象数量。 
  <9> first():                返回第一条记录 
  <10> last():                返回最后一条记录 
  <11> exists():              如果QuerySet包含数据，就返回True，否则返回False
  <12> values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的
                              并不是一系 model的实例化对象，而是一个可迭代的字典序列
  <13> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
  <14> distinct():            从返回结果中剔除重复纪录

```
##### 63.django 中的 F 的作用?
```python
像之前我们所了解的一些过滤的例子和操作都是在针对字段值和某一个常量之间作比较，但是如果我们要针对两个字段值作比较的话就不行了，这就涉及到这个F查询了

```
##### 64.django 中的 Q 的作用?
```python
filter() 等方法中的关键字参数查询都是一起进行“AND” 的。 如果你需要执行更复杂的查询（例如OR语句），你可以使用Q对象。

```
##### 65.django 中如何执行原生 SQL?
```python
1.使用execute执行自定义的SQL
     直接执行SQL语句（类似于pymysql的用法）
        # 更高灵活度的方式执行原生SQL语句
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT DATE_FORMAT(create_time, '%Y-%m') FROM blog_article;")
        ret = cursor.fetchall()
        print(ret)
2.使用extra方法 ：queryset.extra(select={"key": "原生的SQL语句"})
3.使用raw方法
    1.执行原始sql并返回模型
    2.依赖model多用于查询

```
##### 67.only 和 defer 的区别?
```python
defer('id','name'):取出对象，字段除了id和name都有
only('id','name'):取的对象，只有id和name

```
##### 68.select_related 和 prefetch_related 的区别?
```python
前提：有外键存在时，可以很好的减少数据库请求的次数,提高性能
select_related通过多表join关联查询,一次性获得所有数据,只执行一次SQL查询
prefetch_related分别查询每个表,然后根据它们之间的关系进行处理,执行两次查询

```
##### 69.django 中 filter 和 exclude 的区别
两者取到的值都是QuerySet对象,filter选择满足条件的,exclude:排除满足条件的.
##### 70.django 中 values 和 values_list 的区别?

- values : queryset类型的列表中是字典
- values_list : queryset类型的列表中是元组

##### 71.如何使用 django orm 批量创建数据?
```python
objs=[models.Book(title="图书{}".format(i+15)) for i in range(100)]
models.Book.objects.bulk_create(objs)

```
##### 72.django 的 Form 和 ModeForm 的作用?
```python
Form组件的主要功能如下：
    生成页面可用的HTML标签       ——>只能生成获取用户信息的那些input标签等
    对用户提交的数据进行校验，返回错误提示信息
    保留页面上用户输入的内容
    
ModelForm组件，这个组件主要就是将model与Form组件的功能结合起来，可以更加便捷的对数据进行添加、编辑以及数据的验证操作。相对于单独的Form组价来说要方便很多。但是Form组件会比这个ModelForm组件更加灵活，如果在使用Django做web开发过程中验证的数据和数据库字段相关（可以对表进行增、删、改操，注意 Many to many字段，也可以级联操作第3张关系表；），建议优先使用ModelForm，用起来更方便些，但是在使用ModelForm的时候慎用fields='__all__'，获取数据库所有字段势必造成资源的浪费。

```
##### 73.django 的 Form 组件中，如果字段中包含 choices 参数，请使用两种方式 实现数据源实时更新。

- 1.重写构造函数

```python
def__init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)
     self.fields["city"].widget.choices = models.City.objects.all().values_list("id", "name")

```

- 2.利用ModelChoiceField字段,参数为queryset对象

```python
authors = form_model.ModelMultipleChoiceField(queryset=models.NNewType.objects.all())//多选

```
##### 74.django 的 Model 中的 ForeignKey 字段中的 on_delete 参数有什么作用?
```python
删除关联表中的数据时,当前表与其关联的field的操作
django2.0之后，表与表之间关联的时候,必须要写on_delete参数,否则会报异常

```
##### 77.基于django使用ajax发送post请求时，有哪种方法携带csrftoken?

- 1.后端将csrftoken传到前端，发送post请求时携带这个值发送

```python
data: {
        csrfmiddlewaretoken: '{{ csrf_token }}'
  },

```

- 2.获取form中隐藏标签的csrftoken值，加入到请求数据中传给后端

```python
data: {
          csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val()
     },

```

- 3.cookie中存在csrftoken,将csrftoken值放到请求头中

```python
headers:{ "X-CSRFtoken":$.cookie("csrftoken")} 

```
##### 79.django 的缓存能使用 redis 吗?如果可以的话，如何配置?
```python
# 设置django缓存存放位置为redis数据库,并设置一个默认(default)选项,在redis中(配置文件/etc/redis/redis.conf)开启了RDB持久化储存
# pip install django-redis, 然后在视图中可以通过 from django_redis import get_redis_connection 这个方法和redis数据库进行连接
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # redis服务器的ip地址及端口号,及数据库序号,redis一共有15个数据库 0~15
        "LOCATION": "redis://127.0.0.1:6379/6",
　　　　　# "LOCATION": "redis://:passwordpassword@47.193.146.xxx:6379/0", # 如果redis设置密码的话，需要以这种格式进行设置,host前面是密码
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

```
##### 80.django 路由系统中 name 的作用?

- name：对URL路由关系进行命名

##### 81.django 的模板中 filter、simple tag 、 inclusion tag 的区别?
```python
filter的用法：
    #先引入template
from django import template
#声明register，名字只能是register
register = template.Library()
 
#带名字的装饰器，调用的时候用起的名字 如dsb
@register.filter(name='dsb')
def add_sb(value, arg):
    return "{}_{}abc".format(value, arg)
 
@register.filter
def add_sb(value, arg):
    return "{}_{}_abc".format(value, arg)
  
自定义simpletag和自定义inclusion_tag
1. 在app下创建一个名叫templatetags的python包
2. 在templatetags里建一个py文件

simpletag的用法:

和自定义filter类似，只不过接收更灵活的参数。

```
##### 82.django-debug-toolbar 的作用?
django开发调试工具
django-debug-toolbar 是一组可配置的面板，可显示有关当前请求/响应的各种调试信息，并在单击时显示有关面板内容的更多详细信息。
##### 83.django 中如何实现单元测试?
```python
Django的单元测试使用python的unittest模块，这个模块使用基于类的方法来定义测试。类名为django.test.TestCase,继承于python的unittest.TestCase。

执行目录下所有的测试(所有的test*.py文件)：运行测试的时候，测试程序会在所有以test开头的文件中查找所有的test cases(inittest.TestCase的子类),自动建立测试集然后运行测试。

$ python manage.py test

执行animals项目下tests包里的测试：

$ python manage.py testanimals.tests

执行animals项目里的test测试：

$ python manage.py testanimals

单独执行某个test case：

$ python manage.py testanimals.tests.AnimalTestCase

单独执行某个测试方法：

$ python manage.py testanimals.tests.AnimalTestCase.test_animals_can_speak

为测试文件提供路径：

$ python manage.py testanimals/

通配测试文件名：

$ python manage.py test--pattern="tests_*.py"

启用warnings提醒：

$ python -Wall manage.py test

```
##### 84.解释orm中dbfirst和codefirst的含义?
```python
Code First From Database（DbFirst）数据库先行

Code First（代码先行）

```
##### 85.django 中如何根据数据库表生成 model 类?
创建一个项目，修改setting文件，在setting里面设置你要连接的数据库类型和连接名称，地址之类，和创建新项目的时候一致
1.运行下面代码可以自动生成models模型文件<br />
python manage.py inspectdb<br />
2.把模型文件导入到app中
创建app
django-admin.py startapp app
将模型导入创建的app中去
python manage.py inspectdb > app/models.py
##### 86.使用orm和原生sql的优缺点?
相对来说，ORM的缺点就是SQL的优势地方，而优点也是SQL的劣势地方
```python
优点
  方便的使用面向对象，语句清晰
  防注入『这个其实不算ORM的核心，因为比如Phalcon的SQL形式写法也可以防注入』
  方便动态构造语句，对于不同的表的相同操作采用多态实现更优雅
  一定程度方便重构数据层『比如改表名，字段名等』
  设置钩子函数
缺点
  不太容易处理复杂查询语句
  性能较直接用SQL差

```