#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

class ParentClass1:     #父类1
    def __init__(self,name):
        self.name = name

class ParentClass2:     #父类2
    pass
class SubClass1(ParentClass1):      #字类1
    pass
class SubClass2(ParentClass1,ParentClass2):     #字类2
    pass
print(SubClass1.__bases__)
print(SubClass2.__bases__)

class SubClass3(ParentClass1):      #字类3
    def __init__(self,name,id):
        ParentClass1.__init__(self,name)
        self.id = id
        super(SubClass3,self).__init__(name)#super调用父类方法


