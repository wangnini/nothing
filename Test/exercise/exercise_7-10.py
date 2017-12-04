#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-11-26
Updated on 2017-11-26
@author: nwang
@email:  nwang@abcft.com
@Version :1.0
'''
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
#7.将一个列表的数据复制到另一个列表中。
list1=[1,2,3]
list2=list1[:]
print list2

#8.输出 9*9 乘法口诀表。

for i in range(1,10):
    l=[]
    for j in range(1,i+1):
        l.append(str(j)+"*"+str(i)+"="+str(i*j))
    print '|'.join(l)
'''
# 9.暂停一秒输出。
  #使用time模块

dict ={'key1':1,'key2':2,'key3':3}
for key,value in dict.items(): #dict.items()以列表返回可遍历的(键, 值) 元组数组
    print key,value
    time.sleep(1)

# 10.暂停一秒输出，并格式化当前时间。

localtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) #time.localtime(time.time())获取当前时间
print '本地时间为',localtime
time.sleep(1)
print '本地时间为',localtime
