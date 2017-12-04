#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-11-30
Updated on 2017-11-30
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
#20.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
high = 100
total = []
for i in range(0,10):
    high =float(high/2)
    total.append(high)

print '第10次落地经过了%f米，第十次反弹%f米'%((sum(total)-total[-1])*2+100,high)


#21.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，
# 又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。
# 求第一天共摘了多少。
x=1
for day in range(0,9):
    x=(x+1)*2
print x
'''

#22.两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print 'order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k))

