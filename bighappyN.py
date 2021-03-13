#!/usr/bin/env python3
#coding:utf-8

# 价值500万的代码
import random
import time 

fmt='%Y-%m-%d %a %H:%M:%S'
Date=time.strftime(fmt,time.localtime(time.time()))

f = open("./SuerLotto.txt", 'w+')

print("SuerLotto ", Date, file=f)

i = 1
while i < 6:
    a1 = random.randint(1, 35)
    a2 = random.randint(1, 35)
    a3 = random.randint(1, 35)
    a4 = random.randint(1, 35)
    a5 = random.randint(1, 35)
    b1 = random.randint(1, 12)
    b2 = random.randint(1, 12)

    a = [a1, a2, a3, a4, a5]
    b = [b1, b2]
    a.sort(), b.sort()

    print('[%02d %02d %02d %02d %02d]  [%02d %02d]' % (a[0], a[1], a[2], a[3], a[4], b[0],b[1]), file=f)
    i += 1
