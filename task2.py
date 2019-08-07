1.列表
标志[ ]:

#基本操作(创建，append( )，pop( ) ,del( ), 拷贝）
# 创建1
list = list( )
# 创建2
list = [ ]

a = [1,2,3,4,5]
a.append(6)#末尾增加一个元素
print(a)
[1, 2, 3, 4, 5, 6]

a = [1,2,3,4,5]
a.pop()#移除一个元素
a
[1, 2, 3, 4]

a = [1,2,3,4,5]
del a[0] #移除一个元素
a
[2, 3, 4, 5]

#拷贝
a = [1,2,3,4,5]
a1 = a.copy()
a1

a2 = a[:]
a2
[1, 2, 3, 4, 5]

#列表相关方法
list.append(obj) 在列表末尾添加新的对象(每次增加一个) list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（每次增加一个或多个） list.count(obj) 统计某个元素在列表中出现的次数 list.index(obj) 从列表中找出某个值第一个匹配项的索引位置 list.insert(index, obj) 将obj插入列表索引为index的位置 list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 list.remove(obj) 移除列表中某个值的第一个匹配项 list.reverse() 反转整个列表，就地修改，不返回值 list.sort(key=None, reverse=False) 对列表进行排序，就地修改，不返回值 list.clear() 清空列表 list.copy() 浅复制列表，只能拷贝最外层，修改内层则原列表和新列表都会变化

#2.元组( )
基本操作（创建及不可变性）

# 创建
tup = ( )

#不可变性
tup = (1,2,3,4)
tup.append(2)

3.string字符串
定义及基本操作（+，*，读取方式）

str = '字符串'
r1 = 'qwe'
r2 = 'rty'

q=r1+r2
q

w=r1*2
w

'qwerty'

'qweqwe'
读取方式：unicode编码，保存为UTF-8

字符串相关方法
+    字符串连接

*    重复输出字符串

[]    通过索引获取字符串中字符

[ : ]    截取字符串中的一部分

in    成员运算符 - 如果字符串中包含给定的字符返回 True

not in    成员运算符 - 如果字符串中不包含给定的字符返回 True
4.字符串格式化问题

print('%s %s' % ('one', 'two'))
one two

print('{1} {0}'.format('one', 'two'))
two one