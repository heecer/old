#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
a = [i*2 for i in range(5)] #列表生成式
# exit(a)
#生成器b
b = (i*2 for i in range(10))
print(b)    #生成器b对象内存地址
# for i in b:
#     print(i)
print(b.__next__())
print(b.__next__())