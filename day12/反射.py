#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
class Cat(object):
    '''猫类'''
    def __init__(self, name):
        '''初始化，构造函数'''
        self.name = name
        self.__food = None

    def eat(self,food):
        '''吃'''
        print('%s eat %s' % (self.name,food))

def sleep(self):
    print('%s 正在睡觉……'%self.name)
cat = Cat('python')
choice = input('>>:').strip()
if hasattr(cat,choice):
    getattr(cat,'eat')('fish')
else:
    setattr(cat,choice,sleep)
    getattr(cat,choice)(cat)
    delattr(cat,choice)
    getattr(cat, choice)(cat)
