#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import importlib

# a = __import__('day11.静态方法')
# print(a)
# obj = a.静态方法.Cat('python')
# print(obj.eat(obj,'鱼'))
a = importlib.import_module('day11.静态方法')
print(a)
cat = a.Cat('python')
print(cat.name)
print(cat.eat(cat,'fish'))