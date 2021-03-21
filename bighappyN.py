#!/usr/bin/env python3
#coding:utf-8

# 价值500万的代码--大乐透机选五注
#  
from random import sample
import time 

fmt='%Y-%m-%d %a %H:%M:%S'
Date=time.strftime(fmt,time.localtime(time.time()))

f = open("./SuerLotto.txt", 'w+')

print("SuerLotto ", Date, file=f)


for i in range(5):
    a = sample(range(1,36), 5)
    b = sample(range(1,13), 2)
    a.sort(), b.sort()
    print('[%02d %02d %02d %02d %02d]  [%02d %02d]' % (a[0], a[1], a[2], a[3], a[4], b[0],b[1]), file=f)
