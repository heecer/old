#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
def add(*args): #接收多个形参
    print(args)
print(1,2,3,4)
print(*[1,2,3,4])

def add2(**kwargs): #接收多个字典形参
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
add2(name='Python',age=20)

def add3(name,age=20,**kwargs):
    print(name)
    print(age)
    print(kwargs)
add3('Python',sex='m',hobby=100)