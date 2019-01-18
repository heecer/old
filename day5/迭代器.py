#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from collections import Iterable,Iterator
#可迭代对象Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance('',Iterable))
print((i for i in range(4)),Iterable)
print(isinstance(1234,Iterable))

#可迭代对象Iterable
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance((),Iterator))
print(isinstance('',Iterator))
print((i for i in range(4)),Iterator)
print(isinstance(1234,Iterator))

#可迭代对象变成迭代器
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter(()),Iterator))
print(isinstance(iter(''),Iterator))
print((i for i in range(4)),Iterator)
