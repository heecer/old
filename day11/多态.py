#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

class Animal(object):
    '''动物类'''
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    '''猫类'''
    def talk(self):
        print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
    '''狗类'''
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


# def func(obj):  # 一个接口，多种形态
#     obj.talk()

c1 = Cat('小晴')
d1 = Dog('李磊')

# func(c1)
# func(d1)

Animal.animal_talk(c1)
