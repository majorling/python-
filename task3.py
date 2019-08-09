#Task3 字典、集合、判断语句、循环语句等
#1.dict字典
#1.1定义
字典是另一种可变容器模型，且可存储任意类型对象。字典使用键值(keys)
和值(values)存储。

#1.2创建
字典的每个键值(key= > value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})
中格式如下所示：d = {key1: value1, key2: value2}
其中，键值要求唯一，一个key对应一个value，值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  # 创建dict
print(dict1)
print(dict1['Michael'])  # 访问dict
dict1['Michael'] = 100  # 修改dict
print(dict1)
del dict1['Michael']
print(dict1)
dict1.clear()
print(dict1)
# del dict1
# print(dict1)
{'Michael': 95, 'Bob': 75, 'Tracy': 85}
95
{'Michael': 100, 'Bob': 75, 'Tracy': 85}
{'Bob': 75, 'Tracy': 85}
{}
#1.3字典的方法

dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 删除字典内的所有元素
dict1.clear()
print('dict1:', dict1)
# 返回一个字典的浅复制
dict2 = dict1.copy()
print(dict2)
dict1: {}
{}

dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用

# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)

# 输出结果
print(dict1)
print(dict2)
print(dict3)
{'user': 'root', 'num': [2, 3]}
{'user': 'root', 'num': [2, 3]}
{'user': 'runoob', 'num': [2, 3]}

# 创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
seq = ('name', 'age', 'sex')
val = (1, 2, 3)
dict = dict.fromkeys(seq)
print(dict)
dict = dict.fromkeys(seq, 12)
print(dict)
dict = dict.fromkeys(seq, val)
print(dict)
{'name': None, 'age': None, 'sex': None}
{'name': 12, 'age': 12, 'sex': 12}
{'name': (1, 2, 3), 'age': (1, 2, 3), 'sex': (1, 2, 3)}

# 返回指定键的值
dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dict1.get('Bob'))
print(dict1.get('Bib', 'NA'))
75
NA

# 判断键是否在字典中
'Bob' in dict1

True

# 以列表返回可遍历的(键, 值) 元组数组
print(dict1.items())
dict_items([('Michael', 95), ('Bob', 75), ('Tracy', 85)])

# 返回一个迭代器，可以使用 list() 来转换为列表
print(dict1.keys())
print(list(dict1.keys()))
dict_keys(['Michael', 'Bob', 'Tracy'])
['Michael', 'Bob', 'Tracy']

# 返回指定键的值，如果键不存在于字典中，将会添加键并将值设为default
print(dict1.setdefault('Bib'))
None

# 把字典dict2的键/值对更新到dict里
dict = {'name': 'Runoob', 'age': 7}
dict2 = {'sex': 'female'}
dict3 = {'age': 8}
dict.update(dict2)
print(dict)
dict.update(dict3)
print(dict)
{'name': 'Runoob', 'age': 7, 'sex': 'female'}
{'name': 'Runoob', 'age': 8, 'sex': 'female'}

# 返回一个迭代器，可以使用 list() 来转换为列表
print(dict.values())
print(list(dict.values()))
dict_values([95, 75])
[95, 75]

# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。否则，返回default值。
dict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dict.pop('Michael'))
print(dict)
95
{'Bob': 75, 'Tracy': 85}

# 随机返回并删除字典中的一对键和值(一般删除末尾对)。
dict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dict)
print(dict.popitem())
print(dict)
{'Michael': 95, 'Bob': 75, 'Tracy': 85}
('Tracy', 85)
{'Michael': 95, 'Bob': 75}
#2.集合
#2.1特性
集合（set）是一个无序的不重复元素序列。
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

#2.2创建
可以使用大括号{}或者set()函数创建集合，注意：创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典。创建格式：parame = {value01, value02, ...}或者set(value)

# 创建集合set
s = set([1, 1, 2, 2, 3, 3])
print(s)
s = {1, 2, 4, 6, 4}
print(s)
{1, 2, 3}
{1, 2, 4, 6}

#2.3方法

# 添加元素
s.add(8)
print(s)
s.update([12, 6, 4])
print(s)
{1, 2, 4, 6, 8}
{1, 2, 4, 6, 8, 12}

# 删除元素
s = {1, 2, 4, 6, 4}
s.remove(2)  # 元素不存在会报错
print(s)
s.discard(9)  # 不存在不会报错
print(s)
print(s.pop())  # 随机删除元素
print(s)
s.clear()  # 清空集合
print(s)
{1, 4, 6}
{1, 4, 6}
1
{4, 6}
set()

# 集合运算

# 返回多个集合的差集
set1 = {1, 2, 5, 8}
set2 = {1, 2, 3, 5}
set3 = set1.difference(set2)
print(set3)

# 交集
print(set.intersection(set1, set2))

# 并集
print(set.union(set1, set2))

# 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
print(set.isdisjoint(set1, set2))

# 判断x是不是y的子集
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
print(x.issubset(y)
print(y.issuperset(x))
{8}
{1, 2, 5}
{1, 2, 3, 5, 8}
False
True
True
#3.判断语句（要求掌握多条件判断）
if < 条件判断1 >:
    <
    执行1 >
elif < 条件判断2 >:
< 执行2 >
elif < 条件判断3 >:
< 执行3 >
else:
< 执行4 >

#4.三目表达式
为真时的结果 if 判断条件 else 为假时的结果


x = 100
y = 200
print(x if (x > y) else y)
200

#5.循环语句
#5.1 for ... in循环
for < variable > in < sequence >:
    <
    statements >
else:
< statements >

sum = 0
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in seq:
    sum = sum + x
print(sum)
55

#5.2while循环
while < 判断条件 > ：
< 语句 >
else:
< 语句 >
或者

while < 判断条件 > ：
< 语句 >

a = 1
while a < 10:
    #     print (a)
    a = a + 2
print(a)