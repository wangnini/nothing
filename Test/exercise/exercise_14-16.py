#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-11-27
Updated on 2017-11-28
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
#14.将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
def num(n):
    list = []
    n = int(n)
    while n not in [1]:
        for i in range(2, n + 1):
            if n % i == 0:
                n /= i  # n 等于 n/i
                list.append(str(i))
                break  # 跳出循环，重新计算
    print '*'.join(list)

try:
    m=input('请输入一个正整数:')
    while not isinstance(m,int) or m<= 0 :
       print'你输入的数据不符合规则，请重新输入！',
       m = input('请重新输入一个正整数:')
    else:
        num(m)
except Exception:
    print '不可输入字符串！'


def reduceNum(n):
    print '{} = '.format(n),
    if not isinstance(n, int) or n <= 0 :
        print '请输入一个正确的数字 !'
        exit(0)
    elif n in [1] :
        print '{}'.format(n)
    while n not in [1] : # 循环保证递归
        for index in xrange(2, n + 1) :
            if n % index == 0:
                n /= index # n 等于 n/index
                if n == 1: 
                    print index 
                else : # index 一定是素数
                    print '{} *'.format(index),
                break
reduceNum(90)
reduceNum(100)


#15.利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

score = int(raw_input('请输入成绩：'))
while score <0 or score >100:
    print '你输入的分数有误，请重新输入'
    score =int(raw_input('请重新输入成绩：'))
else:
    if score>= 90:
        grade ='A'
    elif score>= 60 and score <90:
        grade ='B'
    elif score<60:
        grade ='C'
    print '您的成绩是',grade
'''

#16.输出指定格式的日期


if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)

    print(miyazakiBirthDate.strftime('%d/%m/%Y'))

    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)

    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))