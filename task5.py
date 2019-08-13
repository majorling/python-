#1.类和对象
类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。而对象是类的实例。
对：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

#2.正则表达式
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
re 模块使 Python 语言拥有全部的正则表达式功能。
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

#3.re模块
re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
函数语法：re.match(pattern, string, flags=0)
pattern指匹的正则表达式，string是指要匹配的字符串，flags是指标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

#4.datetime模块学习
datetime库定义了2个常量和5个类。
2个常量分别是MINYEAR=1和MAXYEAR=9999。

5个类分别是：
date类：表示日期的类
time类：表示时间的类
datetime类：表示时间日期的类
timedelta类：表示两个datetime对象的差值；
tzinfo类：表示时区的相关信息

#5.http请求
python中实现HTTP 请求有三种方式，分别为urllib2/urllib、httplib/urllib 和 Requests。
urllib2/urllib
1.基本请求和响应模型
urllib2和urllib是Python中的两个内置模块，实现 HTTP 请求时，以urllib2为主，urllib为辅。urllib2模块提供了urliopen() 方法，可以向指定的 URL 发出请求来获取数据。
2.请求头headers处理
请求头信息可以直接与URL一起放到Requset()方法里也可以使用add_header()方法添加请求头信息。
3.Cookie处理
urllib2对Cookie的处理是自动的，使用CookieJar函数进行Cookie的管理。我们也可以通过设置请求头中的Cookie域来自定义添加Cookie的内容。
4.设置超时处理的三种方法
在 python2.6之前的版本，urllib2的API并没有Timeout的设置，要设置Timeout值，只能通过设置Socket的全局Timeout值实现。而在python2.6及新的版本中，urlopen() 函数提供了对 Timeout 的设置。
5.获取 HTTP 响应码
对于 200 OK 来说，urlopen()方法返回的response对象的 getcode()方法可以得到该HTTP响应码，但是对于其他类型的响应码，urlopen() 方法会抛出异常，这样需要通过异常对象来获取响应码。

