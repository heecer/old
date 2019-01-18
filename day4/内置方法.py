#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
print(abs(-1))  #绝对值
print(all([0,-1,1]))    #判断所有元素非零值
print(any((0,-1,1)))    #判断任意元素非零值
print(bytearray())

calc = lambda n:n**2 if n<5 else n**3   #lambda加三元运算
print(calc(6))
filter = filter(lambda n:n>5,range(10))     #过滤
for i in filter:
    print(i)
calc = map(lambda n:n*2,range(5))  #映射
print(calc)

# import functools
# calc = functools.reduce(lambda x,y:x*y,range(1,9))  #累积，阶乘
# print(calc)

a = {'a':1,'b':3,'c':4,'d':2}
print(sorted(a))    #健值排序
print(sorted(a.items()))    #按健值排序
print(sorted(a.items(),key = lambda n:n[1]))    #按value值排序

a = [1,2,3,4]
b = ['a','b','c','d']
c = zip(a,b)
d = map(a,b)

for i in c:
    print(i)
