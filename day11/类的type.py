#!/usr/bin/env python
# -*- coding:utf-8 -*-
 # Author:Haccer
def Dog(self,name):
    self.name = name

dog = type('Dog',(object,),{'func':Dog})
print(type(dog))
d = dog()
print(d.func('python'))
