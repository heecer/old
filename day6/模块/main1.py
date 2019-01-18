#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from module_1 import say
'''导入模块的某种方法'''
'''相当于
def say():
    print('hello world')
'''
say()
# move()    #没有导入
from module_1 import move as m
'''模块方法取名 '''
m()