#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
class Cat(object):
    '''猫类'''
    def __init__(self, name):
        '''初始化，构造函数'''
        self.name = name

    @staticmethod       #静态方法
    def eat(self, food):
        print('%s eat %s' % (self.name, food))

cat = Cat('python')
cat.eat(cat,'fish')

