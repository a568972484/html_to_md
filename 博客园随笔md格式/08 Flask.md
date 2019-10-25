#### 1. Flask 中正则 URL 的实现？
app.route('<URL>')中 URL 显式支持 string、int、float、path uuid any 6种类型，隐式支持正则。<br />
**第一步：**写正则类，继承 BaseConverter，将匹配到的值设置为 regex 的值。
```python
1. class RegexUrl(BaseConverter): 
2.      def __init__(self， url_map， *args): 
3.          super(RegexUrl， self).__init__(url_map) 
4.          self.regex = args[0] 
```
**第二步：**把正则类赋值给我们定义的正则规则。
```python
5. app.url_map.converters['re'] = RegexUrl 
```
**第三步：**在 URL 中使用正则。
```python
6. @app.route('/regex/<re("[a-z]{3}"):id>') 
7. def regex111(id): 
8.    return 'id:%s'%id 
```
#### 2. Flask 中请求上下文和应用上下文的区别和作用？
current_app、g 是应用上下文。<br />
request、session 是请求上下文。<br />
手动创建上下文的两种方法：
```python
1. with app.app_context() 
2. app = current_app._get_current_object() 
```
**两者区别：**<br />
请求上下文：保存了客户端和服务器交互的数据。<br />
应用上下文：flask 应用程序运行过程中，保存的一些配置信息，比如程序名、数据库连接、应用信息等。<br />
两者作用：<br />
请求上下文(request context)：<br />
Flask从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。请求对象是一个很好的例子，它封装了客户端发送的HTTP请求。<br />
要想让视图函数能够访问请求对象，一个显而易见的方式是将其作为参数传入视图函数，不过这会导致程序中的每个视图函数都增加一个参数，除了访问请求对象,如果视图函数在处理请求时还要访问其他对象，情况会变得更糟。为了避免大量可有可无的参数把视图函数弄得一团糟，<br />
Flask使用上下文临时把某些对象变为全局可访问。<br />
应用上下文(application context)：<br />
它的字面意思是 应用上下文，但它不是一直存在的，它只是request context 中的一个对 app 的代理(人)，所谓local proxy。它的作用主要是帮助 request 获取当前的应用，它是伴 request 而生，随 request 而灭的。
#### 3. Flask中数据库设置？
```python
 app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test' 
```
动态追踪修改设置，如未设置只会提示警告
```python
 app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
```
查询时会显示原始SQL语句
```python
 app.config['SQLALCHEMY_ECHO'] = True 
```
<img src="https://img-blog.csdnimg.cn/2018110811320155.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RvbWluaWNKaQ==,size_16,color_FFFFFF,t_70" />
#### 4. 常用的SQLAlchemy查询过滤器？
<img src="https://img-blog.csdnimg.cn/20181108115551636.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RvbWluaWNKaQ==,size_16,color_FFFFFF,t_70" />
#### 5. 对Flask蓝图(Blueprint)的理解？
**1) 蓝图的定义**<br />
蓝图 /Blueprint 是Flask应用程序组件化的方法，可以在一个应用内或跨越多个项目共用蓝图。<br />
使用蓝图可以极大地简化大型应用的开发难度，也为 Flask扩展 提供了一种在应用中注册服务的集中式机制。<br />
**2) 蓝图的应用场景**<br />
1. 把一个应用分解为一个蓝图的集合。这对大型应用是理想的。一个项目可以实例化一个应用对象，初始化几个扩展，并注册一集合的蓝图。<br />
2. 以 URL 前缀和/或子域名，在应用上注册一个蓝图。 URL 前缀/子域名中的参数即成为这个蓝图下的所有视图函数的共同的视图参数（默认情况下）。<br />
3. 在一个应用中用不同的 URL 规则多次注册一个蓝图。<br />
4. 通过蓝图提供模板过滤器、静态文件、模板和其它功能。一个蓝图不一定要实现应用或者视图函数。<br />
5. 初始化一个 Flask 扩展时，在这些情况中注册一个蓝图。<br />
**3) 蓝图的缺点**<br />
不能在应用创建后撤销注册一个蓝图而不销毁整个应用对象。<br />
**4) 使用蓝图的三个步骤**<br />
**1.创建 一个蓝图对象**
```python
 blue = Blueprint("blue"，__name__) 
```
**2.在这个蓝图对象上进行操作 ，例如注册路由、指定静态文件夹、注册模板过滤器**
```python
 @blue.route('/') 
     def blue_index(): 
        return 'Welcome to my blueprint' 
```
**3.在应用对象上注册这个蓝图对象**
```python
 app.register_blueprint(blue，url_prefix='/blue') 
```
字段对象 说明<br />
FieldList 一组指定类型的字段<br />
WTForms常用验证函数<br />
InputRequired 确保字段中有数据<br />
DataRequired 确保字段中有数据并且数据为真<br />
EqualTo 比较两个字段的值，常用于比较两次密码输入<br />
Length 验证输入的字符串长度<br />
NumberRange 验证输入的值在数字范围内<br />
URL 验证URL<br />
AnyOf 验证输入值在可选列表中<br />
NoneOf 验证输入值不在可选列表中<br />
**使用Flask-WTF需要配置参数SECRET_KEY。**<br />
CSRF_ENABLED是为了CSRF（跨站请求伪造）保护。 SECRET_KEY用来生成加密令牌，当CSRF激活的时候，该设置会根据设置的密匙生成加密令牌。
#### 6. Flask项目中如何实现 session 信息的写入？
Flask中有三个 session：<br />
第一个：数据库中的 session，例如:db.session.add()<br />
第二个：在 flask_session 扩展中的 session，使用：from flask_session importSession，使用第三方扩展的 session 可以把信息存储在服务器中，客户端浏览器中只存储 sessionid。<br />
第三个：flask 自带的 session，是一个请求上下文， 使用：from flask import session。自带的session 把信息加密后都存储在客户端的浏览器 cookie 中。
#### 7. 项目接口实现后路由访问不到怎么办？
1.可以通过 postman 测试工具测试，或者看 log 日志信息找到错误信息的大概位置。<br />
2.断点调试
#### 8. Flask中url_for函数？
**1.URL反转：**根据视图函数名称得到当前所指向的url。<br />
**2.url_for()** 函数最简单的用法是以视图函数名作为参数，返回对应的url，还可以用作加载静态文件。
```html
 <link rel="stylesheet" href="{{url_for('static',filename='css/index.css')}}">  
```
该条语句就是在模版中加载css静态文件。<br />
**3.url_for 和 redirect 区别**<br />
url_for是用来拼接 URL 的，可以使用程序 URL 映射中保存的信息生成 URL。url_for() 函数最简单的用法是以视图函数名作为参数， 返回对应的 URL。例如，在示例程序中 hello.py 中调用<br />
url_for('index') 得到的结果是 /。<br />
redirect 是重定向函数，输入一个URL后，自动跳转到另一个URL所在的地址，例如，你在函数<br />
中写 return redirect('https://www.baidu.com') 页面就会跳转向百度页面。
```python
1. from flask import Flask,redirect,url_for   
2. app = Flask(__name__)   
3. @app.route('/')   
4. def index():   
5.     login_url = url_for('login')   
6.     return redirect(login_url)   
7.     return u'这是首页'   
8.   
9. @app.route('/login/')   
10. def login():   
11.     return  u'这是登陆页面'   
12.   
13. @app.route('/question/<is_login>/')   
14. def question(is_login):   
15.     if is_login == '1':   
16.         return  u'这是发布问答的页面'   
17.     else:   
18.         return  redirect(url_for('login'))   
19.    
20. if __name__ == '__main__':   
21.     app.run(debug=True)  
```
#### 9. Flask中请求钩子的理解和应用？
请求钩子是通过装饰器的形式实现的，支持以下四种：<br />
1，before_first_request 在处理第一个请求前运行<br />
2，before_request:在每次请求前运行<br />
3，after_request:如果没有未处理的异常抛出，在每次请求后运行<br />
4，teardown_request:即使有未处理的异常抛出，在每次请求后运行<br />
应用：<br />
请求钩子
```python
1. @api.after_request  
2. def after_request(response): 
3.    """设置默认的响应报文格式为 application/json""" 
4.    # 如果响应报文 response 的 Content-Type 是以 text 开头，则将其改为 
5.    # 默认的 json 类型 
6.    if response.headers.get("Content-Type").startswith("text"): 
7.     response.headers["Content-Type"] = "application/json" 
8.    return respon 
```
#### 10. 一个变量后写多个过滤器是如何执行的？
{{ expression | filter1 | filter2 | ... }} 即表达式(expression)使用filter1 过滤后再将filter1的结果去使用 filter2 过滤。
#### 11. 如何把整个数据库导出来，再导入指定数据库中？
导出：<br />
mysqldump [-h 主机] -u 用户名 -p 数据库名 > 导出的数据库名.sql<br />
导入指定的数据库中:<br />
**第一种方法：**<br />
mysqldump [-h 主机] -u 用户名 -p 数据库名 < 导出的数据库名.sql<br />
**第二种方法：**<br />
先创建好数据库，因为导出的文件里没有创建数据库的语句，如果数据库已经建好，则不用再创建。<br />
create database example charset=utf8;（数据库名可以不一样）<br />
切换数据库：<br />
use example;<br />
导入指定 sql 文件：<br />
mysql>source /path/example.sql;
#### 12. Flask和Django路由映射的区别？
在django中，路由是浏览器访问服务器时，先访问的项目中的url，再由项目中的url找到应用中url，这些url是放在一个列表里，遵从从前往后匹配的规则。在flask中，路由是通过装饰器给每个视图函数提供的，而且根据请求方式的不同可以一个url用于不同的作用。
#### 13. 跨站请求伪造和跨站请求保护的实现？
<img src="https://img-blog.csdnimg.cn/20181108115517483.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RvbWluaWNKaQ==,size_16,color_FFFFFF,t_70" /><br />
图中Browse是浏览器，WebServerA是受信任网站/被攻击网站A，WebServerB是恶意网站/点<br />
击网站B。<br />
（1）一开始用户打开浏览器，访问受信任网站A，输入用户名和密码登陆请求登陆网站A。<br />
（2）网站A验证用户信息，用户信息通过验证后，网站A产生Cookie信息并返回给浏览器。<br />
（3）用户登陆网站A成功后，可以正常请求网站A。<br />
（4）用户未退出网站A之前，在同一浏览器中，打开一个TAB访问网站B。<br />
（5）网站B看到有人方式后，他会返回一些攻击性代码。<br />
（6）浏览器在接受到这些攻击性代码后，促使用户不知情的情况下浏览器携带Cookie（包括sessionId）信息，请求网站A。这种请求有可能更新密码，添加用户什么的操作。 从上面CSRF攻击原理可以看出，要完成一次CSRF攻击，需要被攻击者完成两个步骤：<br />
1.登陆受信任网站A，并在本地生成COOKIE。<br />
2.在不登出A的情况下，访问危险网站B。<br />
如果不满足以上两个条件中的一个，就不会受到CSRF的攻击，以下情况可能会导致CSRF：<br />
1.登录了一个网站后，打开一个tab页面并访问另外的网站。<br />
2.关闭浏览器了后，本地的Cookie尚未过期，你上次的会话还没有已经结束。（事实上，关闭浏览器不能结束一个会话，但大多数人都会错误的认为关闭浏览器就等于退出登录/结束会话了……）<br />
解决办法：就是在表单中添加from.csrf_token。
#### 14. Flask(_ name_ )中的__name__可以传入哪些值？
可以传入的参数：<br />
1，字符串：‘hello’,<br />
但是‘abc’,不行，因为abc是python内置的模块<br />
2，__name__，约定俗成<br />
不可以插入的参数<br />
1，python内置的模块，re,urllib,abc等<br />
2，数字
#### 15. 请手写一个 flask 的 Hello World。
```python
from flask import Flask;------->引入Flask插件，pip install Flask;

app=Flask(__name__) #变量app是Flask的一个实例并且必须传入一个参数，__name__对应的值是__main，即当前的py文件的文件名作为Flask的程序名称，这个也可以自定义，比如，取，'MY_ZHH_APP'
                          #__name__是固定写法，主要是方便flask框架去寻找资源 ，也方便flask插件出现错误时，去定位问题

@app.route('/')      #相当于一个装饰器，视图映射，路由系统生成 视图对应url，这边没有指定method .默认使用get
def first_flask():    #视图函数
    return 'Hello World'  #response，最终给浏览器返回的内容


if __name__ == '__main__':
    app.run(debug=True)              #启动这个应用服务器，并开启debug,才能定位问题
```
#### 16. Flask 框架的优势?
```python
1.轻巧
2.简洁
3.扩展性强（个人认为最重要的特点）
4.核心（werkzeug和jinja2）jinja2就是指模板引擎。

Flask确实很“轻”，不愧是Micro Framework，从Django转向Flask的开发者一定会如此感慨，除非二者均为深入使用过
Flask自由、灵活，可扩展性强，第三方库的选择面广，开发时可以结合自己最喜欢用的轮子，也能结合最流行最强大的Python库。
入门简单，即便没有多少web开发经验，也能很快做出网站
非常适用于小型网站
非常适用于开发web服务的API
开发大型网站无压力，但代码架构需要自己设计，开发成本取决于开发者的能力和经验
各方面性能均等于或优于Django
Django自带的或第三方的好评如潮的功能，Flask上总会找到与之类似第三方库
Flask灵活开发，Python高手基本都会喜欢Flask，但对Django却可能褒贬不一
Flask与关系型数据库的配合使用不弱于Django，而其与NoSQL数据库的配合远远优于Django
Flask比Django更加Pythonic，与Python的philosophy更加吻合
```
#### 17. Flask 框架依赖组件?
```python
# 依赖jinja2模板引擎
# 依赖werkzurg协议
```
#### 18. Flask 蓝图的作用?
```python
# blueprint把实现不同功能的module分开.也就是把一个大的App分割成各自实现不同功能的module.
# 在一个blueprint中可以调用另一个blueprint的视图函数, 但要加相应的blueprint名.

```
#### 19. 列举使用过的 Flask 第三方组件?
```python
# Flask组件
    flask-session  session放在redis
    flask-SQLAlchemy 如django里的ORM操作
    flask-migrate  数据库迁移
    flask-script  自定义命令
    blinker  信号-触发信号
# 第三方组件
    Wtforms 快速创建前端标签、文本校验
    dbutile     创建数据库连接池
    gevnet-websocket 实现websocket
# 自定义Flask组件
    自定义auth认证 
    参考flask-login组件

```
#### 20. 简述 Flask 上下文管理流程?
```python
# a、简单来说，falsk上下文管理可以分为三个阶段：
　　1、'请求进来时'：将请求相关的数据放入上下问管理中
　　2、'在视图函数中'：要去上下文管理中取值
　　3、'请求响应'：要将上下文管理中的数据清除
# b、详细点来说：
　　1、'请求刚进来'：
        将request，session封装在RequestContext类中
        app，g封装在AppContext类中
        并通过LocalStack将requestcontext和appcontext放入Local类中
　　2、'视图函数中'：
        通过localproxy--->偏函数--->localstack--->local取值
　　3、'请求响应时'：
        先执行save.session()再各自执行pop(),将local中的数据清除

```
#### 21. Flask 中的 g 的作用?
```python
# g是贯穿于一次请求的全局变量，当请求进来将g和current_app封装为一个APPContext类，
# 再通过LocalStack将Appcontext放入Local中，取值时通过偏函数在LocalStack、local中取值；
# 响应时将local中的g数据删除

```
#### 22. 如何编写 flask 的离线脚本?
```python
#新建create_tablepy
from chun import db,create_app
 
app = create_app()
app_ctx = app.app_context() # app_ctx = app/g
with app_ctx: # __enter__,通过LocalStack放入Local中
    db.create_all() # 调用LocalStack放入Local中获取app，再去app中获取配置

```
#### 23. Flask 中上下文管理主要涉及到了那些相关的类?并􏰁述类主要作用?
```python
RequestContext  #封装进来的请求（赋值给ctx）
AppContext      #封装app_ctx
LocalStack      #将local对象中的数据维护成一个栈（先进后出）
Local           #保存请求上下文对象和app上下文对象

```
#### 24. 为什么要Flask把Local对象中的的值stack维护成一个列表?
```python
# 因为通过维护成列表，可以实现一个栈的数据结构，进栈出栈时只取一个数据，巧妙的简化了问题。
# 还有，在多app应用时，可以实现数据隔离；列表里不会加数据，而是会生成一个新的列表
# local是一个字典，字典里key（stack）是唯一标识，value是一个列表

```
#### 25. Flask 中多 app 应用如何编写?
```python
请求进来时，可以根据URL的不同，交给不同的APP处理。蓝图也可以实现。
    #app1 = Flask('app01')
    #app2 = Flask('app02')
    #@app1.route('/index')
    #@app2.route('/index2')
源码中在DispatcherMiddleware类里调用app2.__call__，
  原理其实就是URL分割，然后将请求分发给指定的app。
之后app也按单app的流程走。就是从app.__call__走。

```
#### 26. 在Flask中实现WebSocket需要什么组件?
```python
# gevent-websocket

```
#### 27. wtforms 组件的作用?
```python
# WTForms是一个支持多个web框架的form组件，主要用于对用户请求数据进行验证。
# WTforms作用：当网站中需要用到表单时，WTForms变得很有效。应该把表单定义为类，作为单独的一个模块。

```
#### 28. Flask 框架默认 session 处理机制?
```python
# 前提:
    不熟的话:记不太清了,应该是……分两个阶段吧   
# 创建:
    当请求刚进来的时候,会将request和session封装成一个RequestContext()对象,
    接下来把这个对象通过LocalStack()放入内部的一个Local()对象中;
　　 因为刚开始 Local 的ctx中session是空的;
　　 所以,接着执行open_session,将cookie 里面的值拿过来,重新赋值到ctx中
    (Local实现对数据隔离,类似threading.local) 
# 销毁:
    最后返回时执行 save_session() 将ctx 中的session读出来进行序列化,写到cookie
    然后给用户,接着把 ctx pop掉

```
#### 29. 解释Flask框架中的Local对象和threadinglocal对象的区别?
```python
# a.threading.local
作用：为每个线程开辟一块空间进行数据存储(数据隔离)。

问题：自己通过字典创建一个类似于threading.local的东西。
storage = {
   4740: {val: 0},
   4732: {val: 1},
   4731: {val: 3},
   }

# b.自定义Local对象
作用：为每个线程(协程)开辟一块空间进行数据存储(数据隔离)。
class Local(object):
   def __init__(self):
      object.__setattr__(self, 'storage', {})
   def __setattr__(self, k, v):
      ident = get_ident()
      if ident in self.storage:
         self.storage[ident][k] = v
      else:
         self.storage[ident] = {k: v}
   def __getattr__(self, k):
      ident = get_ident()
      return self.storage[ident][k]
obj = Local()
def task(arg):
   obj.val = arg
   obj.xxx = arg
   print(obj.val)
for i in range(10):
   t = Thread(target=task, args=(i,))
   t.start()

```
#### 30. SQLAlchemy 中的 session 和 scoped_session 的区别?
```python
# Session：
由于无法提供线程共享功能，开发时要给每个线程都创建自己的session
打印sesion可知他是sqlalchemy.orm.session.Session的对象
# scoped_session：
为每个线程都创建一个session，实现支持线程安全
在整个程序运行的过程当中，只存在唯一的一个session对象。
创建方式:
   通过本地线程Threading.Local()
   # session=scoped_session(Session)
   创建唯一标识的方法(参考flask请求源码)

```
#### 31. SQLAlchemy 如何执行原生 SQL?
```python
# 使用execute方法直接操作SQL语句(导入create_engin、sessionmaker)
engine=create_engine('mysql://root:*****@127.0.0.1/database?charset=utf8')
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
session.execute('alter table mytablename drop column mycolumn ;')

```
#### 32. ORM 的实现原理?
```python
# ORM的实现基于一下三点
映射类：描述数据库表结构，
映射文件：指定数据库表和映射类之间的关系
数据库配置文件：指定与数据库连接时需要的连接信息(数据库、登录用户名、密码or连接字符串)

```
#### 33. DBUtils 模块的作用?
```python
# 数据库连接池
使用模式：
1、为每个线程创建一个连接，连接不可控，需要控制线程数
2、创建指定数量的连接在连接池，当线程访问的时候去取，不够了线程排队，直到有人释放(推荐)
---------------------------------------------------------------------------
两种写法：
1、用静态方法装饰器，通过直接执行类的方法来连接使用数据库
2、通过实例化对象，通过对象来调用方法执行语句
https://www.cnblogs.com/ArmoredTitan/p/Flask.html

```
#### 34. 以下SQLAlchemy的字段是否正确?如果不正确请更正.
```python
fromdatetime importdatetime
fromsqlalchemy.ext.declarative
importdeclarative_base
fromsqlalchemy importColumn, Integer, String, DateTime
Base =declarative_base()


classUserInfo(Base):
   
__tablename__ ='userinfo'
id=Column(Integer, primary_key=True, autoincrement=True)

name =Column(String(64), unique=True)

ctime =Column(DateTime, default=datetime.now())
from datetime import datetime
from sqlalchemy.ext.declarative
import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()
class UserInfo(Base):
    __tablename__ = 'userinfo'   
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True)
ctime = Column(DateTime, default=datetime.now())
-----------------------------------------------------------------------
不正确：
    Ctime字段中参数应为’default=datetime.now’
    now 后面不应该加括号，加了的话，字段不会实时更新。

```
#### 35. SQLAchemy 中如何为表设置引擎和字符编码?
```python
sqlalchemy设置编码字符集，一定要在数据库访问的URL上增加'charset=utf8'
否则数据库的连接就不是'utf8'的编码格式

eng=create_engine('mysql://root:root@localhost:3306/test2?charset=utf8',echo=True)
1. 设置引擎编码方式为utf8。

    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/sqldb01?charset=utf8")
2. 设置数据库表编码方式为utf8

class UserType(Base):
    __tablename__ = 'usertype'
    id = Column(Integer, primary_key=True)
    caption = Column(String(50), default='管理员')
    # 添加配置设置编码
    __table_args__ = {
        'mysql_charset':'utf8'
    }

这样生成的SQL语句就自动设置数据表编码为utf8了,__table_args__还可设置存储引擎、外键约束等等信息。

```
#### 36. SQLAchemy 中如何设置联合唯一索引?
```python
通过'UniqueConstraint'字段来设置联合唯一索引
__table_args=(UniqueConstraint('h_id','username',name='_h_username_uc'))
# h_id和username组成联合唯一约束

```