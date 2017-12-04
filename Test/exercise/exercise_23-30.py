#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-12-01
Updated on 2017-12-04
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


#26.利用递归方法求5!。


#27.利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


#28.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁
# 最后问第一个人，他说是10岁。请问第五个人多大？



#29.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。



#30.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。





