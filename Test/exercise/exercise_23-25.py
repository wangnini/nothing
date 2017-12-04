#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-12-01
Updated on 2017-12-01
@author: nwang
@email:  nwang@abcft.com
@Version :1.0
'''
import math
import datetime
import sys
import  itertools
reload(sys)
sys.setdefaultencoding('utf-8')
#23.打印出如下图案（菱形）:
'''
   *
  ***
 *****
*******
 *****
  *** 
   *

def paintlx(l):
    for i in range(l / 2):
        print ' ' * (l / 2 - i) + '*' * (i * 2 + 1)
    print '*' * l
    for i in range(l / 2 - 1, -1, -1):
        print ' ' * (l / 2 - i) + '*' * (i * 2 + 1)
while True:
    l = raw_input('请输入菱形腰长(奇数)，默认为7：')
    if l == '':
        l = 7
        paintlx(int(l))
        break
    elif int(l) % 2 == 0:
        print '说了是奇数！'
    else:
        paintlx(int(l))
        break

#24.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

a=2.0
b=1.0
list =[]
list.append(a/b)
for  i in range(1,20):
    b,a=a,a+b
    list.append(a/b)
print sum(list)

'''
#25.求1+2!+3!+...+20!的和。
a =1
list =[]
for i in range(1,21):
    a=a*i
    list.append(a)
print sum(list)

