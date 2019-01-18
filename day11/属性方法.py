#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
class Cat(object):
    '''猫类'''
    def __init__(self, name):
        '''初始化，构造函数'''
        self.name = name
        self.__food = None

    @property       #属性方法
    def eat(self):
        print('%s eat %s' % (self.name,self.__food))

    @eat.setter     #设置参数
    def Eat(self,food):
        self.__food =  food
        print('传入参数')
    @eat.deleter
    def eat(self):
        del self.__food
        print('删除属性')
    def __call__(self, *args, **kwargs):
        '''特殊成员方法'''
        print('对象后面加括号，触发执行',args,kwargs)
cat = Cat('python')
cat.eat
cat.Eat = '鱼'
cat.eat
# del cat.eat
# cat.eat
print(Cat.__module__)
print(Cat.__class__)
cat(1,2,3,name='python')
print(Cat.__dict__)
print(Cat.__str__(cat))