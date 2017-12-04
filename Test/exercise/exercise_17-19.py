#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-11-28
Updated on 2017-11-29
@author: nwang
@email:  nwang@abcft.com
@Version :1.0
'''
import math
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
#17.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
def calc(string):
    letters = 0
    space = 0
    digit = 0
    others = 0
    for i in string:
        if i.isalpha(): #英文字母
            letters +=1
        elif i.isspace():
            space +=1
        elif i.isdigit():
            digit +=1
        else:
            others +=1
    print' char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)

if __name__ == '__main__':
    s = raw_input('请输入一串字符:')
    calc(s)

#18.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
times =int(raw_input('请输入相加的次数：'))
num = int(raw_input('请输入计算的数字：'))
total =0
sum = 0
for i in range(times):
    sum += (10 ** i)
    total += sum * num
print total
'''

#19.一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
w=[]
for  i in range(1,1001):
    y = []
    for j in range(1,i-1):
        if i %j ==0:
            y.append(j)

    if sum(y) ==i:
        w.append(i)
        print y
print '1000内的完数为:',w

