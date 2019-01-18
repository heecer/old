#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
class Dog:
    '''定义类'''
    def __init__(self,name):
        self.name = name    #
    def dulk(self):
        print('%s:汪汪队'%(self.name))
d1 = Dog('张三').dulk()   #类实例化，类对象
d2 = Dog('李四').dulk()
