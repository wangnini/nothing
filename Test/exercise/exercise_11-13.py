#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-11-26
Updated on 2017-11-27
@author: nwang
@email:  nwang@abcft.com
@Version :1.0
'''
import math
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#11.古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''
#程序分析：兔子的规律为数列1,1,2,3,5,8,13,21...递归
num = int(raw_input('请输入第几个月：'))
def fib(n):
    if n ==1 or n==2:
        return 1;
    return fib(n - 1) + fib(n - 2)
print '第%d个月兔子数量为%d只'%(num,fib(num))


#12.判断101-200之间有多少个素数，并输出所有素数。
list =[]
for i in range(101,200):
    flag = True
    for j in range(2,i-1): #除了1和他本身外，没有被其他数整除
        if i%j ==0:
            flag =False
            continue  #continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
    if flag ==True:
        list.append(i)
print list
print '一共有%d个素数'%len(list)
'''

#13.打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
list =[]
for m in range(100,999):
    if (m/100)**3 +(m / 10 % 10)**3 + (m % 10) **3 == m:
        list.append(m)
print list
print '一共有%d个水仙花数'%len(list)





