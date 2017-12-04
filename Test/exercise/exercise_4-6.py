#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-11-25
Updated on 2017-11-26
@author: nwang
@email:  nwang@abcft.com
@Version :1.0
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import  time
import  sys
reload(sys)
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'

# 4.输入某年某月某日，判断这一天是这一年的第几天？
m = [1, 3, 5, 7, 8, 10, 12]  # 大月
def calc(y1,m1,d1):
    sum = 0
    total = 0
    d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 平年
    r = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # run年
    for i in range(0, m1 - 1):
        if y1 % 400 == 0 or (y1 % 4 == 0 and y1 % 100 != 0):  # 闰年
            sum = sum + r[i]
        else:
            sum = sum + d[i]
    total = sum +d1
    print '这一天是第%d天' % (total)
    return;

year = int(raw_input('请输入年份:\n'))
while year <= 0:
    print '你输入的年份有误，请重新输入'
    year = int(raw_input('请重新输入年份:\n'))
else:
    month = int(raw_input('请输入月份:\n'))
    while month>13 or month <0:
        print '你输入的月份有误，请重新输入'
        month = int(raw_input('请重新输入月份:\n'))
    else:
        if month in m:
            day = int(raw_input('请输入天:\n'))
            while day > 31 or day < 1:  # 大月不超过31天
                print '大月不能超过31天或者小于1天，请重新输入'
                day = int(raw_input('请重新输入天:\n'))
            else:
                calc(year,month,day);
        else:
            day = int(raw_input('请输入天:\n'))
            while day > 30 or day < 1:
                print '小月不能超过30天或者小于1天'
                day = int(raw_input('请重新输入天:\n'))
            else:
                calc(year, month, day);
'''
# 5.输入三个整数x,y,z，请把这三个数由小到大输出。
l=[]
for i in range(3):
    x = int(raw_input('请输入整数：\n'))
    l.append(x)
l.sort() #升序
print '三个数字从小到大',l
l.sort(reverse=True) #降序
print '三个数字从大到小',l

'''
#6.斐波那契数列。
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# F(n)=F（n-1）+F(n-2)
# 递归
num = int(raw_input('请输入求的数：'))
def fib(n):
    if n ==1 or n==2:
        return 1;
    return fib(n - 1) + fib(n - 2)
print '第%d个数为%d'%(num,fib(num))




