#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
def add(x,y,f):
    return f(x)+f(y)
a = add(3,-6,abs)
print(a)