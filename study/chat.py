#! /usr/bin/env python
# -*- coding: utf-8 -*-
import  sys

f= open("in.txt")
line = f.readline()
while line:
    line =f.readline()
    f2=open("core.txt")
    for line1 in f2.readline():
        print line1
f.close()
