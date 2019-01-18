#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
def fibo(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b
        a,b = b,a+b
        n += 1
f = fibo(10)    #斐波拉契生成器
print(f.__next__())
print(f.__next__())
print('****继续****')
for i in f:
    print(i)