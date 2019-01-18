#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
s = [1,2,3,4,5,2,7,6]
s1 = [23,34,6,2,623]
s = set(s)  #集合取重
s1 = set(s1)
# print(s)
print(s.intersection(s1))   #交集
print(s&s1)
print(s.union(s1))  #并集
print(s|s1)
print(s.difference(s1))     #差集
print(s-s1)
print(s.symmetric_difference(s1))   #补集
print(s^s1)
print(s.issubset(s1))   #判断是否是子集
print(s.issuperset(s1)) #判断是否是父集
print(s.isdisjoint(s1)) #判断是否交集

s.add(9)    #添加
print(s)
s.update(s1)
print(s)
s.pop()     #删除首项
print(s)
s.remove(34)    #删除指定项
print(s)
s.discard(88)
print(s)