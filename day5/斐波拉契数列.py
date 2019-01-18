#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
def fibo(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
    exit('结束')
fibo(10)