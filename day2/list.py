#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
list1=['a','b','c','d','e']

# print(list1[1])
# print(list1[1:3])
# print(list1[-1])
# print(list1[-3:-1])
# print(list1[-3:])
list1.append('f')#追加
list1.insert(-1,'f')#插入
list1.remove('f')
list1.pop(-1)
del list1[0]
print(list1)
Index= list1.index('d')
print(Index)