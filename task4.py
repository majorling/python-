1.函数关键字
用def定义函数。
2.函数的定义
函数，就是具有独立功能的代码块。可以方便快速开发，避免重复写代码，提升编码的效率以及代码的重用性。
def area(a,b):
    return a*b
area(4,7)
28

定义函数时，可以在小括弧内写入参数，用来接收参数用的，称为“形参”，在调用时，小括号中的参数，用来传递参数的，称为“实参”。上述a和b就是形参，而4和7就是实参。


3.函数参数与作用域
实参类别：
位置实参：调用函数时按照函数定义的参数位置、顺序来传递函数。
关键字实参：指定关键字（形参）的方式传递函数 ，通过“键-值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
默认值：可以给形参指定默认值
变量在函数内部定义的称为局部变量，只在函数内部有效。一旦函数执行完毕，局部变量就会被收回，无法访问。
写在函数外的就是全局变量，可以在文件内的任何地方被访问，当然在函数内部也可以。需要注意的是不能在函数内部随意改变全局变量的值，会报错。

4.函数返回值
函数返回的值被称为 返回值 。在函数中，可使用 return 语句将值返回到调用函数的代码行。 返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

5.file
打开文件方式（读写两种方式）
逐行读取，写入文件。
文件对象的操作方法
我们要对文件进行操作，首先要做的就是打开一个文件，python中提供了open( )和file()两个内建函数供我们使用。
open( )基本语法如下
flie_object = open(file_name,access_mode = ‘r’,buffering = -1)
其中file_name 是一个字符串，就是要打开文件的路径（可以是相对路劲也可以是绝对路径）
可选变量access_mode也是一个字符串，代表文件的打开模式，常用的有’r’读,’w’写,’a’追加
另外一个参数buffering 用于指示访问文件所采用的缓冲方式，0代表不缓冲，1代表缓冲一行，任何大于1的值代表给定缓冲区的大小，不提供该参数或者使用负数，代表使用系统默认缓冲机制。
file( )是一个工厂函数，具有和open( )相同的功能，可以任意替换
使用open打开文件，处理后要将文件关闭，否则在程序运行结束之前都不将文件句柄释放，将一直占据内存空间，如果担心忘记，可以使用with。
学习对excel及csv文件进行操作
读CSV：
import csv
打开文件，用 with open(“./csv/文件名.csv”,”r”) as csvfile:
读取csv文件，返回的是迭代类型 read = csv.reader(csvfile)

for i in read: print(i)
import csv#导入模块
#打开csv文件
with open("E:/Users/DELL/PycharmProjects/untitled1/互联网相关企业信息.csv","r") as csvfile:#r代表read
    #读取文件
    read = csv.reader(csvfile)
    # print(read)
    for i in read:#使用遍历的方式来读取文件
        print(i)

with open('./csvtest.csv','w')as csvfile:#这里的w代表write写入
    writer = csv.writer(csvfile)
    writer.writerow(['id','url','keywords'])
    data = [
        ('1','http://www.xiaoheiseo.com/','小黑'),
        ('2','http://www.baidu.com/','百度'),
        ('3','http://www.jd.com/','京东')

    ]

6.os模块

import os
#导入os模块
#print(os.name)
#查看操作系统 nt—windows
#posix—linux/unis/mac os
#print(os.uname())
#打印电脑详细信息
#不支持windows
#print(os.environ)
#获取操作系统的所有环境变量
#print(os.environ.get(“python2”))
#获取系统指定的环境变量

print(os.getcwd())
#查看当前文件所在的路径 current

print(os.listdir())
获取当前文件夹下所有的文件 不能深层获取
path=‘路径’
print(os.listdir(path))
#获取指定路径下所有的的文件

‘’’
#当前目录下创建一个文件夹
os.mkdir(“练习”)
#在指定的路径下创建一个文件夹
path1="“
os.mkdir()
#在指定路上创建多层级文件夹 mkdir（）创建单层级
os.makedirs(path1)









