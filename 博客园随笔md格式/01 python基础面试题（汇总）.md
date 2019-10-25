##### 1、入门
##### 1.为什么学习 Python?
##### 2.通过什么途径学习的 Python?
##### 3 公司线上和开发环境使用的什么系统?
##### 4 Python 和 Java、PHP、C、C#、C++等其他语言的对比?
```python
1.C语言，它既有高级语言的特点，又具有汇编语言的特点，它是结构式语言。C语言应用指针：可以直接进行靠近硬件的操作，但是C的指针操作不做保护，也给它带来了很多不安全的因素。C++在这方面做了改进，在保留了指针操作的同时又增强了安全性，受到了一些用户的支持，但是，由于这些改进增加语言的复杂度，也为另一部分所诟病。Java则吸取了C++的教训，取消了指针操作，也取消了C++改进中一些备受争议的地方，在安全性和适合性方面均取得良好的效果，但其本身解释在虚拟机中运行，运行效率低于C++/C。一般而言，C，C++，java被视为同一系的语言，它们长期占据着程序使用榜的前三名。
      C语言的优点：简洁紧凑、灵活方便；运算符丰富；数据类型丰富；表达方式灵活实用；允许直接访问物理地址，对硬件进行操作；生成目标代码质量高，程序执行效率高；可移植性好；表达力强；
      C语言的缺点：C语言的缺点主要表现在数据的封装性上，这一点使得C在数据的安全性上有很大缺陷，这也是C和C++的一大区别。 C语言的语法限制不太严格，对变量的类型约束不严格，影响程序的安全性，对数组下标越界不作检查等。从应用的角度，C语言比其他高级语言较难掌握。也就是说，对用C语言的人，要求对程序设计更熟练一些。

 

2.C++是C语言的继承，它既可以进行C语言的过程化程序设计，又可以进行以抽象数据类型为特点的基于对象的程序设计，还可以进行以继承和多态为特点的面向对象的程序设计。C++擅长面向对象程序设计的同时，还可以进行基于过程的程序设计，因而C++就适应的问题规模而论，大小由之。 
C++不仅拥有计算机高效运行的实用性特征，同时还致力于提高大规模程序的编程质量与程序设计语言的问题描述能力。
C++语言的程序因为要体现高性能，所以都是编译型的。但其开发环境，为了方便测试，将调试环境做成解释型的。即开发过程中，以解释型的逐条语句执行方式来进行调试，以编译型的脱离开发环境而启动运行的方式来生成程序最终的执行代码。
生成程序是指将源码（C++语句）转换成一个可以运行的应用程序的过程。如果程序的编写是正确的，那么通常只需按一个功能键，即可搞定这个过程。该过程实际上分成两个步骤。
第一步是对程序进行编译，这需要用到编译器（compiler）。编译器将C++语句转换成机器码(也称为目标码)；如果这个步骤成功，下一步就是对程序进行链接，这需要用到链接器（linker）。链接器将编译获得机器码与C++库中的代码进行合并。C++库包含了执行某些常见任务的函数（“函数”是子程序的另一种称呼）。例如，一个C++库中包含标准的平方根函数sqrt，所以不必亲自计算平方根。C++库中还包含一些子程序，它们把数据发送到显示器，并知道如何读写硬盘上的数据文件。 
 
 3. C#语言，C#是微软公司发布的一种面向对象的、运行于.NET Framework之上的高级程序设计语言。C#看起来与Java有着惊人的相似；它包括了诸如单一继承、接口、与Java几乎同样的语法和编译成中间代码再运行的过程。但是C#与Java有着明显的不同，它借鉴了Delphi的一个特点，与COM（组件对象模型）是直接集成的，而且它是微软公司 .NET windows网络框架的主角。首先，C# 和JAVA一样，简直就是照搬了C++的部分语法，因此，对于数量众多的C++程序员学习起来很容易上手，另外，对于新手来说，比C++要简单一些。其次，Windows是占垄断地位的平台，而开发Windows应用，当然微软的声音是不能忽略的。最重要的是，相对于C++，用C# 开发应用软件可以大大缩短开发周期，同时可以利用原来除用户界面代码之外的C++代码。


4. Java语言，Java是一种可以撰写跨平台应用软件的面向对象的程序设计语言，是由Sun Microsystems公司于1995年5月推出的Java程序设计语言和Java平台（即JavaSE, JavaEE, JavaME）的总称。Java 技术具有卓越的通用性、高效性、平台移植性和安全性，广泛应用于个人PC、数据中心、游戏控制台、科学超级计算机、移动电话和互联网，同时拥有全球最大的开发者专业社群。在全球云计算和移动互联网的产业环境下，Java更具备了显著优势和广阔前景。
Java的优势，与传统程序不同，Sun 公司在推出 Java 之际就将其作为一种开放的技术。全球数以万计的 Java 开发公司被要求所设计的 Java软件必须相互兼容。“Java 语言靠群体的力量而非公司的力量”是Sun公司的口号之一，并获得了广大软件开发商的认同。这与微软公司所倡导的注重精英和封闭式的模式完全不同。Sun 公司对 Java 编程语言的解释是：Java 编程语言是个简单、面向对象、分布式、解释性、健壮、安全与系统无关、可移植、高性能、多线程和动态的语言。


5.php语言，PHP（PHP: Hypertext Preprocessor的缩写，中文名：“PHP：超文本预处理器”）是一种通用开源脚本语言。语法吸收了C语言、Java和Perl的特点，入门门槛较低，易于学习，使用广泛，主要适用于Web开发领域。
     特性：PHP 独特的语法混合了 C、Java、Perl 以及 PHP 自创新的语法；PHP可以比CGI或者Perl更快速的执行动态网页——动态页面方面，与其他的编程语言相比，PHP是将程序嵌入到HTML文档中去执行，执行效率比完全生成htmL标记的CGI要高许多，PHP具有非常强大的功能，所有的CGI的功能PHP都能实现； PHP支持几乎所有流行的数据库以及操作系统；最重要的是PHP可以用C、C++进行程序的扩展。


6.python语言，是一种面向对象、直译式计算机程序设计语言，Python语法简洁而清晰，具有丰富和强大的类库。它常被昵称为胶水语言，它能够很轻松的把用其他语言制作的各种模块（尤其是C/C++）轻松地联结在一起。常见的一种应用情形是，使用python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中有特别要求的部分，用更合适的语言改写。
Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符和动态类型。相对于Lisp这种传统的函数式编程语言，Python对函数式设计只提供了有限的支持。有两个标准库(functools, itertools)提供了Haskell和Standard ML中久经考验的函数式程序设计工具。Python本身被设计为可扩充的。并非所有的特性和功能都集成到语言核心。Python提供了丰富的API和工具，以便程序员能够轻松地使用C语言、C++、Cython来编写扩充模块。Python编译器本身也可以被集成到其它需要脚本语言的程序内。因此，很多人还把Python作为一种“胶水语言”（glue language）使用。使用Python将其他语言编写的程序进行集成和封装。
```
##### 5 简述解释型和编译型编程语言?
```python
编译型（需要编译器，相当于用谷歌翻译）：编译型语言执行速度快，不依赖语言环境运行，跨平台差，如C，C++执行速度快，调试麻烦

解释型（需要解释器，相当于同声传译）：解释型跨平台好，一份代码，到处使用，缺点是执行速度慢，依赖解释器运行，如python，JAVA执行速度慢，调试方便 
```
##### 6 Python 解释器种类以及特点?
```python
## CPython

CPython是使用最广且被的Python解释器。本教程以CPython为准。当我们从Python官方网站下载并安装好Python 2.7后，我们就直接获得了一个官方版本的解释器：CPython。这个解释器是用C语言开发的，所以叫CPython。在命令行下运行python就是启动CPython解释器。

## IPython

IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的。好比很多国产浏览器虽然外观不同，但内核其实都是调用了IE。CPython用>>>作为提示符，而IPython用In [序号]:作为提示符。

## PyPy

PyPy是另一个Python解释器，它的目标是执行速度。PyPy采用JIT技术，对Python代码进行动态编译（注意不是解释），所以可以显著提高Python代码的执行速度。

绝大部分Python代码都可以在PyPy下运行，但是PyPy和CPython有一些是不同的，这就导致相同的Python代码在两种解释器下执行可能会有不同的结果。如果你的代码要放到PyPy下执行，就需要了解PyPy和CPython的不同点。

## Jython

Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。

## IronPython

IronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。
```
##### 7 位和字节的关系?
```python
8 bit = 1bytes
```
##### 8 b、B、KB、MB、GB 的关系?
```python
8bit = 1B
1024B = 1KB
1024KB = 1MB
1024MB = 1GB
```
##### 9 请至少列举 5 个 PEP8 规范(越多越好)
```python
- 使用space（空格）来表示缩进，而不要用tab（制表符）
- 和语法相关的每一层缩进都要用4个空格来表示
- 每行的字符数不应超过79
- 对于占据多行的长表达式来说，除了首行之外的其余各行都应该在通常的缩进级别之上再加上4个空格
- 文件中函数与类之间应该用两个空行隔开
- 在同一个类中，各方法之间应该用一个空行隔开
- 函数、变量及属性应该用小写字母来拼写，各单词之间以下划线相连，例如：`lowercase_underscore`
- 类中的实例方法（instance method），应该把首个参数命名为self，以表示该对象自身
- 类方法（class method）的首个参数，应该命名为cls，以表示该类自身
- 不要通过检测长度的方法（如if len(somelist) == 0）来判断somelist是否为[]或“”等空值，而是应该采用if not somelist,它会假定：空值会自动评估为False     
```
##### 10 求结果:or and
```python
v1 = 1 or 3
v2 = 1 and 3
v3 = 0 and 2 and 1
v4 = 0 and 2 or 1
v5 = 0 and 2 or 1 or 4
v6 = 0 or Flase and 1
---------------------------------
v1 = 1 or 3
v2 = 1 and 3
v3 = 0 and 2 and 1
v4 = 0 and 2 or 1
v5 = 0 and 2 or 1 or 4
v6 = 0 or False and 1
>>>1 3 0 1 1 False
```
##### 11.ascii、unicode、utf-8、gbk 区别?
```python
ascii：
在计算机内部，所有信息最终都是一个二进制值。每一个二进制位（bit），有0和1两种状态，因此，8个二进制位可以组合出256种状态，这被称为字节（byte)。上个世纪60年代，美国制定了一套字符编码，对英文字符与二进制之间做了联系，这被称为ASCII码，一直沿用至今。
ASCII码一共规定了128个字符，比如SPACE是32，A是65，这128个符号只咱用了一个字节的后面七位，最前面的一位统一规定为0。

unicode：
世界上有多种编码方法，同一个二进制数字可以被解释称不同的符号。因此，在打开一个文本文件时候，就必须知道它的编码方式，用错误的编码方式打开，就会出现乱码。
Unicode编码，这是一种所有符号的编码。
Unicode显然是一个巨大的集合，现在的规模可以容纳100多万个符号。每个符号的编码都不一样，比如U+0041表示英语的大写字母A，U+4e25表示汉字严。
在Unicode庞大的字符集的优势下，还存在一个问题，比如一个汉字，“严”的Unicode是十六进制4e25，转成二进制足足有15位，也就是，这个符号需要2个字节，表示其他字符还存在3个字节或者更多。计算机怎么区别三个字节表示的是同一个符号而不是分开表示三个呢？如果Unicode统一规定，每个符号用3个字节表示，但是某些字母显然不需要3个，那么就浪费了空间，文本文件大小超出了很多，这显然是不合理的。直到UTF8字符编码出现了。

utf-8：
UTF8的最大特点是，它是一种变长编码，可以使用1-4个字节表示一个符号，根据不同的符号来变化字节长度。
UTF8编码规则只有两条：
1）对于单字节的符号，字节的第一位设为0，后面的7位为这个符号的Unicode码。因此，对于英文字母，UTF8编码和ASCII编码是相同的。
2）对于非单字节（假设字节长度为N）的符号，第一个字节的前N位都设为1，第N+1设为0，后面字节的前两位一律设为10，剩下的没有提及的二进制，全部为这个符号的Unicode码。

gbk：
GBK编码是对GB2312的扩展，完全兼容GB2312。采用双字节编码方案，剔出xx7F码位，共23940个码位，共收录汉字和图形符号21886个，GBK编码方案于1995年12月15日发布。它几乎完美支持汉字，因此经常会遇见GBK与Unicode的转换。

1，各个编码之间的二进制，是不能互相识别的，会产生乱码。

2，文件的存储，传输，不能是unicode （只能是utf-8 utf-16 gbk gbk2312 ascii等）
```
##### 12.字节码和机器码的区别?
```python
字节码是一种中间状态（中间码）的二进制代码（文件）。需要直译器转译后才能成为机器码。

```
##### 13.三元运算编写格式。
```python
条件成立 if 条件 else 条件不成立

```
##### 14.列举你了解的所有Python2和Python3的区别?
```python
# py2
>>> print("hello", "world")
('hello', 'world')
# py3
>>> print("hello", "world")
hello world

py2：input_raw()
py3：input()

1/2的结果
py2：返回0
py3：返回0.5

py2：默认编码ascii
py3：默认编码utf-8

字符串
py2：unicode类型表示字符串序列，str类型表示字节序列
py3:：str类型表示字符串序列，byte类型表示字节序列

py2中函数用关键字global声明某个变量为全局变量，但是在嵌套函数中，想要给一个变量声明为非局部变量是没法实现的。
py3中，新增了关键字nonlocal,使得非局部变量成为可能

```
##### 15.Py2 项目如何迁移成 py3?
##### 16.用一行代码实现数值交换:
```python
a = 1
b = 2
------------------
a,b = b,a

```
##### 17.Python3 和 Python2 中 int 和 long 的区别?
```python
python2:
  int() # 整型
  long() # 长整型
python3中没有long类型，只有int类型

```
##### 18.xrange 和 range 的区别?
```python
xrange 用法与 range 完全相同，所不同的是生成的不是一个list对象，而是一个生成器。
注意：现在的python3中将以前的range取消了，而将xrange重新命名成了range！所以我们现在看到的range其实本质还是xrange~。

```
##### 19.如何实现字符串的反转?如:name="wupeiqi"请反转为name= "iqiepuw" 。
```python
name="wupeiqi"
name[::-1]
> 'iqiepuw'

```
##### 20.文件操作时:xreadlines和readlines的区别?
```python
readlines()是把文件的全部内容读到内存，并解析成一个list，当文件的体积很大的时候，需要占用很多内存

xreadlines()则直接返回一个iter(file)迭代器，在Python 2.3之后已经不推荐这种表示方法了.直接使用for循环迭代文件对象

```
##### 21.列举布尔值为False的常见值?
```python
0, [] , () , {} , '' , False , None

```
##### 22.is 和==的区别?
```python
is比较的是id
== 比较的是值

```
##### 23.哪些情况下，y! = x - (x-y)会成立？
x,y是两个不相等的非空集合
##### 2、数据类型：
##### 字典:
##### 1.1 现有字典 dict={‘a’:24，‘g’:52，‘i’:12，‘k’:33}请按字典中的 value 值进行排序？
```python
1. sorted(dict.items()，key = lambda x:x[1])

```
##### 1.2 说一下字典和json的区别？
字典是一种数据结构，json是一种数据的表现形式，字典的key值只要是能hash的就行，json的必须是字符串
##### 1.3 什么是可变、不可变类型？
可变不可变指的是内存中的值是否可以被改变，不可变类型指的是对象所在内存块里面的值不可以改变，有数值、字符串、元组；可变类型则是可以改变，主要有列表、字典。
##### 1.4 存入字典里的数据有没有先后排序？
存入的数据不会自动排序，可以使用sort函数对字典进行排序。
##### 1.5 字典推导式？
```python
1. dict = {key: value for (key, value) in iterable}

```
##### 1.6 现有字典 d={‘a’:24，’g’:52，’l’:12，’k’:33}请按字 典中的 value 值进行排序？
```python
1. sorted(d.items()，key = lambda x:x[1])

```
##### 1.7 描述下dict的item()方法与iteritems()的不同
```python
字典的items方法作用：是可以将字典中的所有项，以列表方式返回。因为字典是无序的，所以用items方法返回字典的所有项，也是没有顺序的。

字典的iteritems方法作用：与items方法相比作用大致相同，只是它的返回值不是列表，而是一个迭代器。

"""
在Python2.x中，iteritems() 用于返回本身字典列表操作后的迭代器【Returns an iterator on all items(key/value pairs) 】，不占用额外的内存。

在Python 3.x 里面，iteritems()方法已经废除了。在3.x里用 items()替换iteritems() ，可以用于 for 来循环遍历。
"""

```
##### 字符串
##### 2.1 请反转字符串“aStr”?
```python
1. print("aStr"[::-1])

```
##### 2.2 将字符串"k:1|k1:2|k2:3|k3:4"，处理成Python字典：{k:1， k1:2， ... } # 字 典里的K作为字符串处理
```python
1. str1 = "k:1|k1:2|k2:3|k3:4"
2. def str2dict(str1):
3.   dict1 = {}
4.   for iterms in str1.split('|'):
5.      key，value = iterms.split(':')
6.      dict1[key] = value
7.   return dict1

```
##### 2.3 请按alist中元素的age由大到小排序
alist [{'name':'a'，'age':20}，{'name':'b'，'age':30}，{'name':'c'，'age':25}]
```python
sorted(alist，key=lambda x:x['age']，reverse=True)

```
##### 2.4 常用的字符串格式化哪几种？
```python
name = '张三'
1）、占位符
s1 = "%s DSB 你好"%name
2）、format
s2 = '{} DSB 你好'.format(name)
3）、f-string（python3.6之后才有的特性）
s3 = f'{name} DSB 你好'

```
##### 2.5 简述字符串驻留机制
```python
对于短字符串，将其赋值给多个不同的对象时，内存中只有一个副本，多个对象共享该副 
本。长字符串不遵守驻留机制。

驻留适用范围: 由数字，字符和下划线（_）组成的python标识符以及整数[-5,256]。 

```
##### 列表
##### 3.1 下面代码的输出结果将是什么？
```python
list = ['a'， 'b'， 'c'， 'd'， 'e']
print(list[10:])

```
下面的代码将输出[]，不会产生IndexError错误。就像所期望的那样，尝试用超出成员的个数的index
来获取某个列表的成员。例如，尝试获取list[10]和之后的成员，会导致IndexError。
##### 3.2 写一个列表生成式，产生一个公差为11的等差数列
```python
1.print([x*11 for x in range(10)])

```
##### 3.3 给定两个列表，怎么找出他们相同的元素和不同的元素?
```python
1. list1 = [1，2，3]
2. list2 = [3，4，5]
3. set1 = set(list1)
4. set2 = set(list2)
5. print(set1&amp;set2)
6. print(set1^set2)

```
##### 3.4 请写出一段Python代码实现删除一个list里面的重复元素?
比较容易记忆的是用内置的set：
```python
1. l1 = ['b'，'c'，'d'，'b'，'c'，'a'，'a']
2. l2 = list(set(l1))

```
如果想要保持他们原来的排序：<br />
用list类的sort方法：
```python
1. l1 = ['b'，'c'，'d'，'b'，'c'，'a'，'a']
2. l2 = list(set(l1))
3. l2.sort(key=l1.index)
4. print(l2)

```
也可以这样写：
```python
1. l1 = ['b'，'c'，'d'，'b'，'c'，'a'，'a']
2. l2 = sorted(set(l1)，key=l1.index)
3. print(l2)

```
也可以用遍历：
```python
1. l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
2. l2 = []
3. for i in l1:
4.  if not i in l2:
5.      l2.append(i)
6. print(l2)
```
##### 3.5 下面这段代码的输出结果是什么？请解释？
```python
1. def extendlist(val, list=[]):
2.  list.append(val)
3.  return list
4. list1 = extendlist(10)
5. list2 = extendlist(123, []
6. list3 = extendlist('a')
7. print("list1 = %s" %list1)
8. print("list2 = %s" %list2)
9. print("list3 = %s" %list3)
10. 输出结果：
11. list1 = [10, 'a']
12. list2 = [123]
13. list3 = [10, 'a']
```
新的默认列表只在函数被定义的那一刻创建一次。当extendList被没有指定特定参数list调用时，这组list的值<br />
随后将被使用。这是因为带有默认参数的表达式在函数被定义的时候被计算，不是在调用的时候被计算。
##### 3.6 将以下3 个函数按照执行效率高低排序
```python
1. def f1(lIn):
2.      l1 = sorted(lIn)
3.      l2 = [i for i in l1 if i<0.5]
4.      return [i*i for i in l2]
5. def f2(lIn):
6.      l1 = [i for i in l1 if i<0.5]
7.      l2 = sorted(l1)
8.      return [i*i for i in l2]
9. def f3(lIn):
10.     l1 = [i*i for i in lIn]
11.     l2 = sorted(l1)
12.     return [i for i in l1 if i<(0.5*0.5)]
```
按执行效率从高到低排列：f2、f1和f3。<br />
要证明这个答案是正确的，你应该知道如何分析自己代码的性能。<br />
Python中有一个很好的程序分析包，可以满足这个需求。
```python
1. import random
2. import cProfile
3. lIn = [random.random() for i in range(100000)]
4. cProfile.run('f1(lIn)')
5. cProfile.run('f2(lIn)')
6. cProfile.run('f3(lIn)')

```
##### 3. 7 有一个list["This","is","a","Boy","!"],所有元素都是字符串,对他进行大小写 无关的排序
```python
l1 = ['This','is','a','Boy','!']
print(sorted(l1))

```
##### 元组
<ol>
- tuple:元组，元组将多样的对象集合到一起，不能修改，通过索引进行查找，使用括号”()”;
- 应用场景：把一些数据当做一个整体去使用，不能修改；
</ol>
##### 集合
set:set集合，在Python中的书写方式为{}，集合与之前列表、元组类似，可以存储多个数据，但
是这些数据是不重复的。集合对象还支持union(联合), intersection(交), difference(差)和
sysmmetric_difference(对称差集)等数学运算.
快速去除列表中的重复元素
```python
1. a = [11,22,33,33,44,22,55]
2. set(a)
3. {11, 22, 33, 44, 55}

```
交集：共有的部分
```python
1.  a = {71,72,73,74,75}
2.  b = {72,74,75,76,77}
3.  a&amp;b
4.  {72, 74, 75}

```
并集：总共的部分
```python
1.  a = {21,22,23,24,25}
2.  b = {22,24,25,26,27}
3.  a | b
4.  {21, 22, 23, 24, 25, 26, 27}

```
差集：另一个集合中没有的部分
```python
1.  a = {51,52,53,54,55}
2.  b = {52,54,55,56,57}
3.  b - a
4.  {66, 77}

```
对称差集(在a或b中，但不会同时出现在二者中)
```python
1.  a = {91,92,93,94,95}
2.  b = {92,94,95,96,97}
3.  a ^ b
4.  {11, 33, 66, 77}

```
##### 综合
##### 1.列举字符串、列表、元组、字典每个常用的5个方法?
```python
字符串：repleace,strip,split,reverse,upper,lower,join.....

列表：append,pop,insert,remove,sort,count,index.....

元组：index,count,len(),dir()

字典：get,keys,values,pop,popitems,clear,update,items.....

```
##### 2.is 和==的区别?
```python
is比较的是id
== 比较的是值

```
##### 3.什么是反射?以及应用场景?
```python
在绝大多数语言当中都有反射机制的存在， 可以用字符串的方式去访问对象的属性，调用对象的方法（但是不能去访问方法），Python中一切皆对象，都可以使用反射

1）、反射机制是很多框架的基石。
2）、

```
##### 4.简述Python的深浅拷贝?
```python
copy()：浅copy，浅拷贝指仅仅拷贝数据集合的第一层数据

deepcopy():深copy,深拷贝指拷贝数据集合的所有层

```
##### 5.Python 垃圾回收机制?
```python
垃圾回收机制是自动帮助我们管理内存，清理垃圾的一种工具

1）、引用计数
当一个对象的引用被创建或者复制时，对象的引用计数加1；
当一个对象的引用被销毁时，对象的引用计数减1；
当对象的引用计数减少为0时，就意味着对象已经没有被任何人使用了，可以将其所占用的内存释放了。

优点：

简单、直观
实时性，只要没有了引用就释放资源。
缺点：

维护引用计数需要消耗一定的资源
循环应用时，无法回收。也正是因为这个原因，才需要通过标记-清理和分代收集机制来辅助引用计数机制。

2）、标记-清除
“标记-清除”不改动真实的引用计数，而是将
集合中对象的引用计数复制一份副本，改动该对象引用的副本。对于副
本做任何的改动，都不会影响到对象生命走起的维护。

3）、分代回收
将系统中的所有内存块根据其存活时间划分为不同的集合，
每一个集合就成为一个“代”，垃圾收集的频率随着“代”的存活时间的增大而减小。
也就是说，活得越长的对象，就越不可能是垃圾，就应该减少对它的垃圾收集频率。
那么如何来衡量这个存活时间：通常是利用几次垃圾收集动作来衡量，
如果一个对象经过的垃圾收集次数越多，可以得出：该对象存活时间就越长。

```
##### 6.Python 的可变类型和不可变类型的区别?
```python
值变ID不变为可变类型
值变ID变为不可变类型

```
##### 7.填空题
1.获取 Python 解释器版本的方法是
```python
import sys
print(sys.version)

```
2.如果模块是被导入的,`__name__`的值是. 文件名 , 如果模块是被直接执行的`__name__`的值是 `__main__`
3.Python 的内存管理中, 为了追踪内存中的对象, 使用了 `id()` 这一简单技术
4.Python 的标准解释器是有 C 语言实现的, 称为__cpython__, 有 Java 实现的被称为 Jpython
5.Python 中, ___语句能直接显示的释放内存资源
```python
import gc

gc.collect()

```
6.Python 的乘方运算符是. `**`
##### 8. lambda表达式格式以及应用场景？
```
匿名就是没有名字
def func(x,y,z=1):
    return x+y+z

匿名
lambda x,y,z=1:x+y+z #与函数有相同的作用域，但是匿名意味着引用计数为0，使用一次就释放，除非让其有名字
func=lambda x,y,z=1:x+y+z 
func(1,2,3)
#让其有名字就没有意义

与内置函数配合一起使用

```
##### 9. *arg和**kwarg作用
*args用来接收溢出的位置参数，将接收的参数组织成元祖<br />
**kwargs用来接收溢出的关键字参数，将接受的参数组织成字典
##### 10.求结果
```python
v = dict.fromkeys(['k1','k2'],[])
v['k1'].append(666)
print(v) #{'k1': [666], 'k2': [666]}
v['k1'] = 777
print(v)#{'k1': 777, 'k2': [666]}
#第一次字典的两个k指向的是同一块内存地址，所以k1的内存地址追加666，
k2的值也同样会是666，
而当给k1赋值时，改变了k1指向的内存地址，所以这个时候，k2不会随之发生变化

```
##### 11.一行代码实现9*9乘法表
```python
print("\n".join("\t".join(["%s*%s=%s" %(x,y,x*y) for y in range(1, x+1)]) 
                
# 递归
def f(i):
     if i>=1:
        f(i-1)
        print(['%dx%d=%d'%(j,i,i*j) for j in range(1,i+1)])
        
if __name__=='__main__':
    f(9)

```
##### 12.比较 a = [1,2,3] 和 b = [(1),(2),(3) ] 以及 c = [(1,),(2,),(3,) ] 的区别？
a与b两者值相等，而c中列表的每个元素是一个个的元祖形式<br />
a,b元素均为数字，b中括号内没加逗号，所以仍然是数字
##### 13.1 <(2==2)和 1 <2==2 的结果分别是什么, 为什么
```python
print(1 < (2 == 2))  --> False
print(1 < 2 == 2)  --> True

```
##### 14.如何打乱一个排好序的 list 对象 alist
```python
import random
random.shuffle(alist)

```
##### 15.如何查找一个字符串中特定的字符?find 和 index 的差异?
```python
1）、find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回-1
2）、index()方法：在字符串里查找子串第一次出现的位置，类似字符串的find方法，不过比find方法更好的是，如果查找不到子串，会抛出异常，而不是返回-1
3）、rfind和rindex方法用法和上面一样，只是从字符串的末尾开始查找

```
##### 16.把 aaabbcccd 这种形式的字符串压缩成 a3b2c3d1 这种形式。
```python
b={}
c=""
a="aaabbcccd"
for i in a:
    b[i]=b.get(i,0)+1
for i,t in b.items():
    c+=str(i)
    c+=str(t)
print(c)

```
##### 17.Python 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1+2+3.编程找出 1000 以内的所有完数。
```python
from functools import reduce


def sum(a, b):
    return a + b


for i in range(2, 1001):
    l = [1]
    for j in range(2, int(i / 2 + 1)):
        if i % j == 0:
            l.append(j)
    if i == reduce(sum, l):
        print(i)
        print(l)

```
##### 18.给你一个字符串，比如‘abc’，请打印出该字符串的所有排列组合：
以‘abc’为例，输出的结果应该是：'abc', 'acb', 'bac', 'bca', 'cab', 'cba'
```python
def perm(s=''):
    if len(s) <= 1:
        return [s]
    sl = []  
    for i in range(len(s)):  
        for j in perm(s[0:i] + s[i + 1:]):  
            sl.append(s[i] + j)  
    return sl


def main():
    perm_nums = perm('abb')  
    no_repeat_nums = list(set(perm_nums))  # 去重
    print('perm_nums', len(perm_nums), perm_nums)
    print('no_repeat_nums', len(no_repeat_nums), no_repeat_nums)
    pass


if __name__ == '__main__':
    main()

```
##### 19.执行以下代码段后,x 的值为
```python
x = 10
x += x
x -= x - x
print(x)

"""
20
"""

```
##### 20.对于一个非空字符串,判断其是否可以有一个子字符串重复多次组成,字符串 只包含小写字母且长度不超过 10000
示例 1:
\1. 输入"abab"<br />
\2. 输出True<br />
\3. 样例解释: 输入可由"ab"重复两次组成
示例 2:
\1. 输入"abcabcabc"<br />
\2. 输出True<br />
\3. 样例解释: 输入可由"abc"重复三次组成
示例 3:<br />
\1. 输入"aba"
\2. 输出False
```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                a = s[:i]
                j = i
                while j < n and s[j:j + i] == a:
                    j += i
                if j == n: return True

        return False

```
##### 21.从0-99这100个数中随机取出10个，要求不能重复，可以自己设计数据结构
```python
print([x * x for x in range(1, 11)])

```
##### 介绍一下try except的用法和作用?
```python
Python的except用来捕获所有异常， 因为Python里面的每次错误都会抛出 一个异常，所以每个程序的错误都被当作一个运行时错误。
 
try:
    pass
except BaseException as e:
 
    print(e)
 
finally:
 
    pass

```
##### 在python中如何抛出，捕获，处理异常？
```python
raise Exception 触发抛出异常
用try和except语句来捕获异常
处理异常的方法有：
try ... except...else语句
finally子句，
with语句

```
# 二 函数面试题
### enumerate 的作用是什么?
```python
# 答案
'''
enumerate函数是将一个可迭代对象中元素，按元素顺序每个增加一个索引值，将其组成一个索引序列，利用它可以同时获得索引和值，这样做的目的是为了将一个可迭代对象中元素组成一个“索引,值”对便于后续操作。
'''

```
### lambda 表达式格式以及应用场景?
```python
# 答案

# 匿名就是没有名字
def func(x,y,z=1): return x+y+z
# 匿名
lambda x,y,z=1:x+y+z # 与函数有相同的作用域，但是匿名意味着引用计数为0，使用一次就释放，除非让其有名字 func=lambda x,y,z=1:x+y+z

func(1,2,3)
# 让其有名字就没有意义,与内置函数配合一起使用

```
### Python 递归的最大层数?
```python
# 答案
'''
    最大数为998
'''

```
### 列表推导式和生成器表达式 [i % 2 for i in range(10)] 和 (i % 2 for i inrange(10)) 输出结果分别是什么?
```python
print([i % 2 for i in range(10)])
print((i % 2 for i in range(10)))

```
### 列举常见的内置函数?
```python
# 答案
'''
数学类型
abs(a) : 求取绝对值。abs(-1)
max(list) : 求取list最大值。max([1,2,3])
min(list) : 求取list最小值。min([1,2,3])
sum(list) : 求取list元素的和。 sum([1,2,3]) >>> 6
sorted(list) : 排序，返回排序后的list。
len(list) : list长度,len([1,2,3])
divmod(a,b): 获取商和余数。 divmod(5,2) >>> (2,1)
pow(a,b) : 获取乘方数。pow(2,3) >>> 8
round(a,b) : 获取指定位数的小数。a代表浮点数，b代表要保留的位数。round(3.1415926,2) >>> 3.14
range(a[,b]) : 生成一个a到b的数组,左闭右开。 range(1,10) >>> [1,2,3,4,5,6,7,8,9]

类型转换
int(str) : 转换为int型。int('1') >>> 1
float(int/str) : 将int型或字符型转换为浮点型。float('1') >>> 1.0
str(int) : 转换为字符型。str(1) >>> '1'
bool(int) : 转换为布尔类型。 str(0) >>> False str(None) >>> False
bytes(str,code) : 接收一个字符串，与所要编码的格式，返回一个字节流类型。bytes('abc', 'utf-8') >>> b'abc' bytes(u'爬虫', 'utf-8') >>> b'\xe7\x88\xac\xe8\x99\xab'
list(iterable) : 转换为list。 list((1,2,3)) >>> [1,2,3]
iter(iterable)： 返回一个可迭代的对象。 iter([1,2,3]) >>> <list_iterator object at 0x0000000003813B00>
dict(iterable) : 转换为dict。 dict([('a', 1), ('b', 2), ('c', 3)]) >>> {'a':1, 'b':2, 'c':3}
enumerate(iterable) : 返回一个枚举对象。
tuple(iterable) : 转换为tuple。 tuple([1,2,3]) >>>(1,2,3)
set(iterable) : 转换为set。 set([1,4,2,4,3,5]) >>> {1,2,3,4,5} set({1:'a',2:'b',3:'c'}) >>> {1,2,3}
hex(int) : 转换为16进制。hex(1024) >>> '0x400'
oct(int) : 转换为8进制。 oct(1024) >>> '0o2000'
bin(int) : 转换为2进制。 bin(1024) >>> '0b10000000000'
chr(int) : 转换数字为相应ASCI码字符。 chr(65) >>> 'A'
ord(str) : 转换ASCI字符
为相应的数字。 ord('A') >>> 65

相关操作
eval() : 执行一个表达式，或字符串作为运算。 eval('1+1') >>> 2
exec() : 执行python语句。 exec('print("Python")') >>> Python
filter(func, iterable) : 通过判断函数fun，筛选符合条件的元素。 filter(lambda x: x>3, [1,2,3,4,5,6]) >>> <filter object at 0x0000000003813828>
map(func, *iterable) : 将func用于每个iterable对象。 map(lambda a,b: a+b, [1,2,3,4], [5,6,7]) >>> [6,8,10]
zip(*iterable) : 将iterable分组合并。返回一个zip对象。 list(zip([1,2,3],[4,5,6])) >>> [(1, 4), (2, 5), (3, 6)]
type()：返回一个对象的类型。
id()： 返回一个对象的唯一标识值。
hash(object)：返回一个对象的hash值，具有相同值的object具有相同的hash值。 hash('python') >>> 7070808359261009780
help()：调用系统内置的帮助系统。
isinstance()：判断一个对象是否为该类的一个实例。
issubclass()：判断一个类是否为另一个类的子类。
globals() : 返回当前全局变量的字典。
next(iterator[, default]) : 接收一个迭代器，返回迭代器中的数值，如果设置了default，则当迭代器中的元素遍历后，输出default内容。
reversed(sequence) ： 生成一个反转序列的迭代器。 reversed('abc') >>> ['c','b','a']
'''

```
### filter、map、reduce 的作用?
```python
# 答案
filter(func, iterable) : 通过判断函数fun，筛选符合条件的元素。 
filter(lambda x: x>3, [1,2,3,4,5,6]) 
>>> <filter object at 0x0000000003813828>

map(func, *iterable) : 将func用于每个iterable对象。 map(lambda a,b: a+b, 
map(lambda a,b: a+b, [1,2,3,4], [5,6,7])
>>> [6,8,10]
                       
reduce(): 函数会对参数序列中元素进行累积。
reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数                                                
>>> 15
```
### 一行代码实现 9*9 乘法表
```python
# 答案
'''
print('\n'.join(['\t'.join(["%2s*%2s=%2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
'''


```
### 什么是闭包?
```python
闭包函数（closure function）指的是定义在一个函数内部的函数，被外层函数包裹着，其特点是可以访问到外层函数中的名字，如下inner函数就是一个闭包函数。

def outer():
    num = 1
    def inner():
        print(num) # 内层函数中不存在num 但可以访问到外层的num
    return inner # 基于函数对象的概念我们可以将内层函数返回到外界使用，从而打破函数调用的层级限制，但无论在何处调用，作用域的嵌套关系都是以定义阶段为准的，所以外界得到的不仅仅是一个函数对象（inner），在该函数外还包裹了一层作用域，这使得该函数无论在何处调用，都是访问自己外层包裹的作用域中的名字num

func = outer() # func == inner  func指向的是inner的内存地址，但是func本身确实一个全局变量，可以在任意位置调用func，但无论在何处调用func，都需要按照定义阶段作用域的嵌套关系去查找名字

num=1000
func() #输出结果：1 

```
### 使用生成器编写 fib 函数, 函数声明为 fib(max), 输入一个参数 max 值, 使得 该函数可以这样调用。
```python
for i in range(0,100):
    print fib(1000)

# 并产生如下结果(斐波那契数列),1,1,2,3,5,8,13,21...

# 答案
def fib():
    i,k=1,0
    while 1:
        j=i+k
        yield j
        i=k
        k=j
for fn in fib():
    if fn>1000:
        break
    else:
        print(fn)

```
### 一行代码, 通过 filter 和 lambda 函数输出以下列表索引为基数对应的元素。
```python
list_a=[12,213,22,2,2,2,22,2,2,32]

# 答案
l = filter(lambda x:x in list_a,[i for i in range(len(list_a))])
print(list(l))


```
### 写一个base62encode函数,62进制。
```python
# 即:0123456789AB..Zab..z(10 个数字+26 个大写字母+26 个小写字母)。 

# 答案
def base62Encode(n):
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    lst = []
    while n > 0:
        lst.append(n % 62) # 58
        n = n // 62

    lst = lst[::-1]
    result = ""
    for item in lst: # 58
        result += s[item]

    return result
  
print(base62Encode(58))

# 结果
w

```
### 请实现一个装饰器,限制该函数被调用的频率,如10秒一次
```python
# 答案
import time
def time_pay(func):

    def inner(*args, **kwargs):
        for line in range(10):
            print(line + 1)
            time.sleep(1)

        res = func(*args, **kwargs)

        return res

    return inner

@time_pay
def func1():
    print('from func1...')
    
func1()

```
### 请实现一个装饰器,通过一次调用使函数重复执行5次。
```python
# 答案
def again_func(func):

    def inner(*args, **kwargs):

        for line in range(5):

            func(*args, **kwargs)

    return inner

@again_func
def func1():
    print('from func1...')

func1()

```
### python 一行 print 出 1~100 偶数的列表, (列表推导式, filter 均可)
```python
# 答案
print([i for i in range(1, 101) if i % 2 == 0])

print(list(filter(lambda x: x % 2 == 0, range(1, 101))))

```
### 解释生成器与函数的不同,并实现和简单使用generator
```python
# 答案
'''
生成器和函数的主要区别在于函数return avalue，生成器yield  a  value，同事标记或记忆point of the yield 以便在下次调用时从标记点恢复执行，yield使用函数转换成生成器，而生成器反过来有返回迭代器。
'''

```
### *arg 和**kwarg 作用?
```python
*args用来接收溢出的位置参数，将接收的参数组织成元祖 
**kwargs用来接收溢出的关键字参数，将接受的参数组织成字典

```
### 请写出打印结果:
```python
# 例 1
def func(a,b=[]):
    b.append(a)
    print(b)
func(1)
func(1)
func(1)
func(1)

# 例 2
def func(a,b={}):
    b[a] = 'v'
    print(b)
    
func(1)
func(2)

# 答案:
'''
例1:
[1]
[1, 1]
[1, 1, 1]
[1, 1, 1, 1]

例2:
{1: 'v'}
{1: 'v', 2: 'v'}

'''

```
### 简述yield和yieldfrom关键字。
```python
# 答案:
'''
yield:
    当一个函数中出现yield关键字的时候，那么这个函数就是一个生成器。可以用for循环或者next()函数来迭代。

yield from:
    简单地说，yield from  generator 。实际上就是返回另外一个生成器
''

```
### 以下代码输出结果为:
```python
# 调用上下文如下
collapse = True
processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
print(processFunc("i\tam\ntest\tobject !"))

collapse = False
processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
print(processFunc("i\tam\ntest\tobject !"))
# 以上代码会在控制台输出什么?

# 答案：
'''
i am test object !
i   am
test    object !
'''

```
### 请给出下面代码的输出结果
```python
a = 1
def fun(a):
    a=2

fun(a)
print(a)

a = []
def fun(a):
    a.append(1)
fun(a)
print(a)

# 答案
1
[1]

```
### 什么是lambda函数,下面这段代码的输出是什么
```python
nums = range(2,20)
for i in nums:
    nums = filter(lambda x:x==i or x % i, nums)
print(list(nums))

# 答案:
'''
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
'''

```
### 指出下面程序存在的问题
```python
def Lastllindextem(src, index):
    '''请返回传入 src 使用空格或者"\"切分后的倒数第 index 个子串'''
    return src.split('\')[-index]

# 答案
\会是转义符的，会有问题，需要\\


```
### 有一个列表[3,4,1,2,5,6,6,5,4,3,3]请写一个函数,找出该列表中没有重复的数的总和。
```python
def func(l):
    res = []
    sum_s = 0
    for i in l:
        if i not in res:
            res.append(i)
            sum_s += i

    return sum_s


list1 = [3, 4, 1, 2, 5, 6, 6, 5, 4, 3, 3]

print(func(list1))  # 21

```
### 求打印结果
```python
arr = [1,2,3]
def bar():
     arr+=[5]

     bar()
print(arr)
'''
A.  error
B.  [5]
C. [1,2,3]
D. [1,2,3,5]
'''
# 答案
A

```
### 请给出下面代码片段的输出
```python
def say_hi(func):
    def wrapper(*args, **kwargs):
        print("HI")
        ret = func(*args, **kwargs)
        print("BYE")
        return re
    return wrapper

def say_yo(func):
    def wrapper(*args, **kwargs):
        print("YO")
        return func(*args, **kwargs)
    return wrapper

@say_hi
@say_yo
def func():
    print("ROCK &amp; ROLL")
func()

# 答案
'''
HI
YO
ROCK &amp; ROLL
BYE
'''

```
### map(str,[1,2,3,4,5,6,7,8,9]) 输出是什么?
```python
print(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # <map object at 0x101f59748>

```
### 请简述标准库中functools.wraps的作用
```python
# 答案
'''
Python装饰器（decorator）在实现的时候，有一些细节需要被注意。例如，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）。这样有时候会对程序造成一些不便，例如笔者想对flask框架中的一些函数添加自定义的decorator，添加后由于函数名和函数的doc发生了改变，对测试结果有一些影响。

所以，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring。
'''

```
### 请给出下面代码片段的输出
```python
def test():
     try:
            raise ValueError("something wrong")
     except ValueError as e:
            print("Error occurred")
            return
     finally:
            print("Done")
            
test()

# 答案
Error occurred
Done

```
### 下面的函数,哪些会输出1,2,3三个数字
```python
def func1():
    for i in range(3):
        print(i)
        a_list = [0, 1, 2]

    for i in a_list:
        print(i + 1)

def func2():
    i = 1

    while i < 3:
        print(i)

        i += 1

def func3():
    for i in range(3):
        print(i + 1)

# 答案
func3()

```
### 以下函数需要在其中引用一个全局变量k,请填写语句
```python
def fun():
   ________
     k=k+1
     
# 答案:
global k

```
### 请把以下函数转化为python lambda匿名函数
```python
def add(x,y):
     return x+y

# 答案
print(lambda x, y: x + y)

```
### 阅读以下代码,并写出程序的输出结果
```python
my_dict = {"a":0,"b":1} 2.
def func(d): 
     d["a"]=1 
     return d
     
func(my_dict) 
my_dict["c"]=2 
print(my_dict)

# 答案
{'a': 1, 'b': 1, 'c': 2}

```
### 填空题
```python
 # 有函数定义如下
def calc(a,b,c,d=1,e=2):
     return (a+b)*(c-d)+e

# 请分别写出以下标号代码的输出结果, 如果出错请写出 Error
print(calc(1,2,3,4,5)) # ____2
print(calc(1,2,3)) # ____8
print(calc(1,2)) # ____报错 missing 1 required positional argument: 'c'
print(calc(1,2,3,e=4)) # ____10
print(calc(e=4, c=5, a=2,b=3)) # ____24 
print(calc(1,2,3, d=5, 4)) # ____SyntaxError

```
### 下列函数的输出结果
```python
def add_end(l=[]):
    l.append("end")
    return l


print(add_end())  # 输出什么
print(add_end())  # 再次调用输出什么? 为什么

# 答案
'''
['end']
['end', 'end']  # 函数在定义阶段参数l就指向了[]的内存地址
'''

```
### 可变参数定义*args,**kwargs的区别是什么？并且写出下边代码的输入内容
```python
def foo(*args, **kwargs):
    print("args=", args)
    print("kwargs=", kwargs)
    print("-----------------")

if __name__ == '__main__':
    foo(1, 2, 3, 4)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, 4, a=1, b=2, c=3)
    foo("a", 1, None, a=1, b='2', c=3)
    
# 答案:
'''
args= (1, 2, 3, 4)
kwargs= {}
-----------------
args= ()
kwargs= {'a': 1, 'b': 2, 'c': 3}
-----------------
args= (1, 2, 3, 4)
kwargs= {'a': 1, 'b': 2, 'c': 3}
-----------------
args= ('a', 1, None)
kwargs= {'a': 1, 'b': '2', 'c': 3}
'''
```
### 请写出log实现(主要功能时打印函数名)
```python
@log
def now():
     print("2019-07-25")
     
now()

# 输出
'''
call now()
2019-07-25
'''
```
### Python 如何定义一个函数
```python
A. class <name>(<Type> arg1, <type> arg2, ...) 
B. function <name>(arg1,arg2,...)
C. def <name>(arg1, arg2,...)
D. def <name>(<type> arg1, <type> arg2...)

# 答案:
C
```
### 选择代码运行结果
```python
country_counter = {}
def addone(country):
        if country in country_counter:
                country_counter[country] += 1
        else:
                country_counter[country] = 1
                
addone("Japan")
addone("china")
print len(country_counter)

'''
A.  0
B.  1
C.  2
D.  3
E.  4
'''

# 答案
C
```
### 选择输出结果
```python
def doff(arg1, *args):
        print(type(args))
        
doff("applea", "bananas", "cherry")

A.str
B.int
C.tuple
D.list
E.dict

# 答案:
C
```
### 下面程序的输出结果是
```python
d = lambda p:p*2 
t = lambda p:p*3

x = 2
x = d(x)
x = t(x)
x = d(x)
print(x)

# 答案
24
```
### 以下代码输出是什么,请给出答案并解释
```python
def multipliers():
        return [lambda x:x*i for i in range(4)] 
        
print([m(2) for m in multipliers()])

# 答案:
    [6，6，6，6]
    闭包函数延迟绑定问题。
# 请修改 multipliers 的定义来产生期望的结果
def multipliers():
        return [lambda x, i=i:x*i for i in range(4)] 
print([m(2) for m in multipliers()])
```
### 写函数
```python
'''
有一个数据结构如下所示，请编写⼀个函数从该结构数据中返回由指定的字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。
'''
data:{
    "time":"2016-08-05T13:13:05",
    "some_id":"ID1234",
    "grp1":{"fld1":1, "fld2":2,},
    "xxx2":{"fld3":0, "fld4":0.4,},
        "fld6":11,
        "fld7": 7,
        "fld46":8
}

# fields:由"|"连接的以 fld 开头的字符串, 如 fld2|fld7|fld29

# 答案一:
def select(data, fields):
    result = {}
    field_lst = fields.split('|')
    for key in data:
        if key in field_lst:
            result[key] = data[key]
        elif type(data[key]) == dict:
            res = select(data[key], fields)
            result.update(res)
    return result


data = {"time": "2016-08-05T13:13:05",
        "some_id": "ID1234",
        "grp1": {"fld1": 1, "fld2": 2},
        "xxx2": {"fld3": 0, "fld5": 0.4},
        "fld6": 11,
        "fld7": 7,
        "fld46": 8}
fields = 'fld2|fld3|fld7|fld19'
print(select(data, fields))

# 答案二:
def select(data,fields,result = {}):
    field_lst = fields.split('|')
    for key in data:
        if key in field_lst:
            result[key] = data[key]
        elif type(data[key]) == dict:
            select(data[key], fields)
    return result
data={"time":"2016-08-05T13:13:05",
    "some_id":"ID1234",
    "grp1":{ "fld1":1,"fld2":2},
    "xxx2":{ "fld3":0,"fld5":0.4},
    "fld6":11,
    "fld7":7,
    "fld46":8}
fields = 'fld2|fld3|fld7|fld19'
select(data,fields)
print(select(data,fields))
```
### 谈谈你对闭包的理解？
闭包(closure)是函数式编程的重要的语法结构。闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。<br />
当一个内嵌函数引用其外部作作用域的变量,我们就会得到一个闭包. 总结一下,创建一个闭包必须满足以下几点:

- 必须有一个内嵌函数
- 内嵌函数必须引用外部函数中的变量
- 外部函数的返回值必须是内嵌函数

### Python函数调用的时候参数的传递方式是值传递还是引用传递？
```python
Python的参数传递有：位置参数、默认参数、可变参数、关键字参数。
函数的传值到底是值传递还是引用传递，要分情况：
```
不可变参数用值传递：
```
像整数和字符串这样的不可变对象，是通过拷贝进行传递的，因为你无论如何都不可能在原处改变
```
不可变对象
```
可变参数是引用传递的：
比如像列表，字典这样的对象是通过引用传递、和C语言里面的用指针传递数组很相似，可变对象
能在函数内部改变。
```
### 对缺省参数的理解 ？
缺省参数指在调用函数的时候没有传入参数的情况下，调用默认的参数，在调用函数的同时赋值时，<br />
所传入的参数会替代默认参数。<br />
*args 是不定长参数，他可以表示输入参数是不确定的，可以是任意多个。<br />
**kwargs 是关键字参数，赋值的时候是以键 = 值的方式，参数是可以任意多对在定义函数的时候<br />
不确定会有多少参数会传入时，就可以使用两个参数。
### 为什么函数名字可以当做参数用?
Python中一切皆对象，函数名是函数在内存中的空间，也是一个对象。
### Python中pass语句的作用是什么？
在编写代码时只写框架思路，具体实现还未编写就可以用 pass 进行占位，使程序不报错，不会进<br />
行任何操作。
### 有这样一段代码，print c会输出什么，为什么？
```python
a = 10
b = 20
c = [a]
a = 15
答：10对于字符串、数字，传递是相应的值。
```
### map函数和reduce函数？
①从参数方面来讲：<br />
map()包含两个参数，第一个参数是一个函数，第二个是序列（列表 或元组）。其中，函数（即 map<br />
的第一个参数位置的函数）可以接收一个或多个参数。<br />
reduce()第一个参数是函数，第二个是序列（列表或元组）。但是，其函数必须接收两个参数。<br />
②从对传进去的数值作用来讲：<br />
map()是将传入的函数依次作用到序列的每个元素，每个元素都是独自被函数“作用”一次 。<br />
reduce()是将传人的函数作用在序列的第一个元素得到结果后，把这个结果继续与下一个元素作用<br />
（累积计算）。
### 递归函数停止的条件？
```
递归的终止条件一般定义在递归函数内部，在递归调用前要做一个条件判断，根据判断的结果选择
是继续调用自身，还是 return;返回终止递归。
终止的条件：
1.判断递归的次数是否达到某一限定值
2.判断运算的结果是否达到某个范围等，根据设计的目的来选择
```
### 回调函数，如何通信的?
```
回调函数是把函数的地址作为参数传递给另一个函数，将整个函数当作一个对象，赋值给调用的函
数。
```
### Python主要的内置数据类型都有哪些？ print dir( ‘a ’) 的输出？
```
内建类型：布尔类型、数字、字符串、列表、元组、字典、集合；
输出字符串‘a’的内建方法；
```
### print(list(map(lambda x: x * x, [y for y in range(3)])))的输出？
```
1. [0， 1， 4]
```
### hasattr() getattr() setattr() 函数使用详解？
### hasattr(object, name)函数：
判断一个对象里面是否有name属性或者name方法，返回bool值，有name属性(方法)返回True，<br />
否则返回False。<br />
注意：name要使用引号括起来。
```python
1. class function_demo(object):
2.     name = 'demo'
3.     def run(self):
4.         return "hello function"
5. functiondemo = function_demo()
6. res = hasattr(functiondemo, 'name')  #判断对象是否有name 属性，True
7. res = hasattr(functiondemo, "run") #判断对象是否有run方法，True
8. res = hasattr(functiondemo, "age") #判断对象是否有age属性，Falsw
9. print(res)
```
### getattr(object, name[,default]) 函数：
获取对象object的属性或者方法，如果存在则打印出来，如果不存在，打印默认值，默认值可选。<br />
注意：如果返回的是对象的方法，则打印结果是：方法的内存地址，如果需要运行这个方法，可以在后<br />
面添加括号()。
```python
1. functiondemo = function_demo()
2. getattr(functiondemo, 'name') #获取name属性，存在就打印出来--- demo
3. getattr(functiondemo, "run") #获取run方法，存在打印出 方法的内存地址---<bound method function_demo.run of <__main__.function_demo object at 0x10244f320>>
4. getattr(functiondemo, "age") #获取不存在的属性，报错如下：
5. Traceback (most recent call last):
6.   File "/Users/liuhuiling/Desktop/MT_code/OpAPIDemo/conf/OPCommUtil.py", line 39, in <module>
7.     res = getattr(functiondemo, "age")
8. AttributeError: 'function_demo' object has no attribute 'age'
9. getattr(functiondemo, "age", 18)  #获取不存在的属性，返回一个默认值
```
### setattr(object,name,values)函数：
给对象的属性赋值，若属性不存在，先创建再赋值
```python
1．class function_demo(object):
2．    name = 'demo'
3．    def run(self):
4．        return "hello function"
5．functiondemo = function_demo()
6．res = hasattr(functiondemo, 'age')  # 判断age属性是否存在，False
7．print(res)
8．setattr(functiondemo, 'age', 18 )  #对age属性进行赋值，无返回值
9．res1 = hasattr(functiondemo, 'age') #再次判断属性是否存在，True
```
### 综合使用：
```python
1．class function_demo(object):
2．    name = 'demo'
3．    def run(self):
4．        return "hello function"
5．functiondemo = function_demo()
6．res = hasattr(functiondemo, 'addr') # 先判断是否存在if res:
7．    addr = getattr(functiondemo, 'addr')
8．    print(addr)else:
9．    addr = getattr(functiondemo, 'addr', setattr(functiondemo, 'addr', '北京首都'))
10．    #addr = getattr(functiondemo, 'addr', '美国纽约')
11．    print(addr)
```
reduce(lambda x,y: x*y, range(1,n+1)) 注意：Python3中取消了该函数。
### 什么是lambda函数？ 有什么好处？
lambda 函数是一个可以接收任意多个参数(包括可选参数)并且返回单个表达式值的函数<br />
1、lambda 函数比较轻便，即用即仍，很适合需要完成一项功能，但是此功能只在此一处使用，<br />
连名字都很随意的情况下；<br />
2、匿名函数，一般用来给 filter， map 这样的函数式编程服务;<br />
3、作为回调函数，传递给某些应用，比如消息处理
### 下面这段代码的输出结果将是什么？请解释。
```python
def multipliers():
    return [lambda x : i * x for i in range(4)]
    print [m(2) for m in multipliers()]
```
上面代码输出的结果是[6， 6， 6， 6] (不是我们想的[0， 2， 4， 6])。<br />
上述问题产生的原因是Python闭包的延迟绑定。这意味着内部函数被调用时，参数的值在闭包内<br />
进行查找。因此，当任何由multipliers()返回的函数被调用时， i的值将在附近的范围进行查找。那时，<br />
不管返回的函数是否被调用，for循环已经完成，i被赋予了最终的值3。<br />
因此，每次返回的函数乘以传递过来的值3，因为上段代码传过来的值是2，它们最终返回的都是6。下面是解决这一问题的一些方法。<br />
一种解决方法就是用Python生成器。
```python
def multipliers():
for i in range(4): yield lambda x :
i * x
```
另外一个解决方案就是创造一个闭包，利用默认函数立即绑定。
```python
def  multipliers():
    return [lambda x， i=i : i * x for i in range(4)]
```
### 什么是lambda函数？它有什么好处？写一个匿名函数求两个数的和？
```python
"""
lambda 函数是匿名函数；使用 lambda 函数能创建小型匿名函数。这种函数得名于省略了用 def
声明函数的标准步骤；
"""

# 答案
f = lambda x，y:x+y
print(f(2017，2018))
```
### 说说python中装饰器、迭代器的用法；描述下dict的items()方法与iteritems()方法的不同；
```python
# 答案
'''
装饰器是指对函数执行过程，做一些扩展，甚至可以更改本身函数的执行迭代器是指遵循迭代器协议的对象，这类对象在被for循环时，每次迭代生成下一个项，不用一开始就生成整个列表在python3中不存在iteritems，items方法返回可迭代对象在python2中items()返回[(key,value)]的列表对象，iteritems()返回迭代器对象，iteritems()循环时不可以增删dict的内容
'''
```
### def(a, b=[])这种写法有什么陷阱?
```python
# 答案
'''
函数的第二个默认参数是一个list，当第一次执行的时候实例化了一个list，第二次执行还是用第一次执行的时候实例化的地址存储，所以三次执行的结果就是 [1, 1, 1] ，想每次执行只输出[1] ，默认参数应该设置为None。
'''
```
### 如何判断一个值是函数还是方法?
```python
from types import MethodType,FunctionType

print(isinstance('1', FunctionType))  # False
print(isinstance(lambda x:x, FunctionType))  # True
```
### 请编写一个函数实现将IP地址转换成一个整数。
```python
'''
如 10.3.9.12 转换规则为:
   10 00001010
   3 00000011
   9 00001001 12 00001100
再将以上二进制拼接起来计算十进制结果:00001010 00000011 00001001 000 01100 = ?
'''
def text(b):

    list_str=b.split(" ")
    new_str=[]
    for i in list_str:
        new_str.append(str(int(i,2)))
    return ".".join(new_str)

print(text("00001010 00000011 00001001 00001100"))
```
### 填空题: 补全代码
```python
'''
若要将 N 个 task 分配给 N 个 worker 同时去完成, 每个 worker 分别都可以承 担这 N 个 task,但费用不同. 下面的程序用回溯法计算总费用最小的一种工作分 配方案, 在该方案中, 为每个 worker 分配 1 个 task.程序中,N 个 task 从 0 开 始顺序编号, N 个 worker 也从 0 开始顺序编号, 主要的变量说明如下:

    - ci:将任务 i 分配给 worker j 的费用
    - task[i]: 值为 0 表示 task i 未分配, 值为 j 表示 task,i 分配给 worker j
    - worker[k] 值为 0 表示未分配 task, 值为 1 表示 worker k 已分配 task;
    - mincost: 最小总费用

'''

# 写个函数接收一个文件夹名称作为参数, 显示文件夹中文件的路径, 以及 其中包含文件夹中文件的路径。
N=8
mincosr = 65535 
worker = []
task = []
temp = []
c=[]

def plan(k, cost):
        global mincosr
        if __(1)__ and cost<mincosr:
        mincosr = cost
        for i in range(N):
                temp[i] = task[i]
   else:
            for i in range(N):
                    if worker[i] ==0 and __(2)__:
                    worker[i] = 1
                    task[k] = __(3)__
                        plan(__(4)__,cost+c[k][i]) 
                        __(5)__
                        task[k] = 0

def main():
        for i in range(N):
                worker.append(0)
        task.append(0)
        temp.append(0)
        c.append(0)
    for j in range(N):
        print("请输入 worker"+str(i)+"完成 task" + str(j)+"的花费")
        input_value = input()
                c[i].append(int(input_value))

plan(0,0)
 
print('\n 最小费用: '+str(mincosr)) 

for i in range(N):
        print("Task"+str(i)+"is assigned to Worker" + str(temp[i]) )

if __name__ == "__main__":
        main()
```