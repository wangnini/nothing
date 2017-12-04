#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

'''
str = 'Hello World!'
print '-----------------字符串---------------------------'
print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串



# 列表[] 可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表

list = ['hah',231,'hhah',2.33]

print '---------------------列表-------------------------'
print list
print list[0]
print  list[1:3]
print list[2:]
print list * 2

# 元祖 () 内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

tuple = ('hh',213,'nishi',3.3)


print '----------------------元组-------------------------'
print tuple
print tuple[0]
print tuple[1:2]
print tuple[2:]
print tuple * 2

# 字典 {} 列表是有序的对象集合，字典是无序的对象集合，字典当中的元素是通过键来存取的，而不是通过偏移存取

dict ={}
dict ['one'] = 'this is one'
dict[2] = 'this is two'
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print '--------------------字典-------------------------------'
print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()
print tinydict['name']

# if 基本用法
flag = False
name =raw_input('请输入你的名字:\n')
if name == 'wangnini':
    flag =True
    print '欢迎小可爱',name
else:
    print 'who are you'


# while 循环 奇偶区分

list = [1, 2, 5, 45, 89, 56, 12]
j = []
o = []
while len(list)>0:
    list = list.pop()
    if(list % 2 == 0):
        o.append(list)
    else:
        j.append(list)


# for 循环
for num  in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j =num/i
            print '%d 等于 %d * %d' %(num,i,j)
            break
    else:
        print num,'是一个质数'
# 循环嵌套 输出2~100之间的素数：
i=2
while(i<100):
    j = 2
    while(j<=(i/j)):
        if not(i%j):
            break
        j=j+1
    if (j>i/j):
        print i,'是素数'
    i= i +1
print 'bye'
'''







