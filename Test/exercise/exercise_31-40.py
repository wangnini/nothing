#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017-12-04
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


def week(letter):
    if letter == 'M':
        print '星期一'
    elif letter == 'W':
        print '星期三'
    elif letter == 'F':
        print '星期五'
    elif letter == 'T':
        second = raw_input('请输入第二个字母')
        if second == 'u':
            print '星期二'
        elif second == 'h':
            print '星期四'
        else:
            print '输入错误'
    elif letter == 'S':
        second = raw_input('请输入第二个字母')
        if second == 'a':
            print '星期六'
        elif second == 'u':
            print '星期天'
        else:
            print '输入错误'
    else:
        print '输入错误'

