#!/usr/bin/env python3
#coding:utf-8

# 价值500万的代码
import random
import time 

fmt='%Y-%m-%d %a %H:%M:%S'
Date=time.strftime(fmt,time.localtime(time.time()))

f = open("./2Colors.txt", 'w+')

print("2Colors ", Date, file=f)

i = 1
while i < 6:
    a1 = random.randint(1, 33)
    a2 = random.randint(1, 33)
    a3 = random.randint(1, 33)
    a4 = random.randint(1, 33)
    a5 = random.randint(1, 33)
    a6 = random.randint(1, 33)
    b1 = random.randint(1, 16)

    a = [a1, a2, a3, a4, a5, a6]
    b = [b1]
    a.sort(), b.sort()

    print('[%02d %02d %02d %02d %02d %02d]  [%02d]' % (a[0], a[1], a[2], a[3], a[4], a[5], b[0]), file=f)
    i += 1
