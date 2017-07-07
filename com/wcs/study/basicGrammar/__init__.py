# -*- coding: UTF-8 -*-

print "------------------------------保留字----------------------------------------"
# 保留字
import keyword

print keyword.kwlist

print "------------------------------if else----------------------------------------"

# if else
if not True:
    print 'true'
else:
    print 'false'

a = 1
if a == 3:
    print 'a=3'
elif a == 2:
    print 'a=2'
else:
    print 'a=', a

print "-------------------------------输出---------------------------------------"

# 输出hello world
print 'hello world'
print 'hello+world', 22, 444

print "-------------------------------输出---------------------------------------"

# 输入
inputText = 111  # input '\n 输入点东西吧。。。。' 
print '您输入的是：', inputText

print "-------------------------------数据类型---------------------------------------"

# 数据类型
a, b, c, d = 100, 222.2, True, 'haha'
print type(a), type(b), type(c), type(d)  # 返回类型名
print isinstance(a, int)  # 判断是否为该类型，可以判断父类

print 2 / 4
print 5 * 6
print 5 // 2  # 除法，取整
print 6 % 4
print 1 + 2
print 5 - 3
print 2 ** 4  # 幂运算，即2^4

str = "hello world! welcome to beijing"
print 'str=', str
print 'str[0]=', str[0]  # 第一个
print 'str[0:3]=', str[0:3]  # 第一个到第三个
print str[0:1]  # 第一个
print str[0:0]  # 第一个到第0个，无输出
print str[0:]  # 第一个到最后
print str[0:-1]  # 第一个到倒数第二个
print str * 2  # 打印两遍
print r'啊啊\r\n'  # r不解析转移字符

print "-----------------------------集合-----------------------------------------"

# 集合
# list 定义用中括号[]
lst = ['haha', 33, 24.55, True]
lst.reverse()
lst.append('yaya')
lst.insert(2, 'haha')
print 'lst.index(33)=', lst.index(33)
print lst[2]
print 'lst.pop()=', lst.pop()
print 'lst.count("haha")=', lst.count('haha')
print 'lst=', lst
print 'list("abcde")=', list('abcde')

# tuple 只读的list，不可变，定义用小括号()
tup = ('啊啊', 99, False, [44, 55])
print tup.count(99)
print tup
print list(tup)

# dict 字典，类似map, 语法同json
dic = {'name': 'charles', 'age': 33, 'sex': 'male'}
print dic.get('name')
print dic
for d in dic:
    print d
    print dic.get(d)
dic1 = {'adress': '北京', 'mobile': 18301208055}
dic = dict(dic, **dic1)
print dic

# set
ss = {'haha', 'bb', 33, 33}
print ss

lis1 = [[0 for x in range(0, 3)] for y in range(4)]
lis1[1][2] = 55
print lis1

lis2 = [[1, 4, 5, 6], [5, 2, 7, 9]]
print lis2[1][0]
print lis2

print 'range(4)=', range(4)
print 'range(0,4)=', range(0, 4)

print "----------------------------------------------------------------------"
