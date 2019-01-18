#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import re
r = 'pythonABC123abc*&'
print(re.match('.*',r))     #从头搜索
print(re.search('n\d*',r))
print(re.search('[0-9]+',r))
print(re.search('(ABC|abc)',r).group())
print(re.findall('(ABC|abc)',r))
a = re.search('(?P<name>[a-zA-z]+)(?P<id>[0-9]+)(?P<pd>\D+)',r).group()
print(a)
b = re.search('(?P<name>[a-zA-z]+)(?P<id>[0-9]+)(?P<pd>\D+)',r).groupdict()
print(b)
c = re.findall('(?P<name>[a-zA-z]+)(?P<id>[0-9]+)(?P<pd>\D+)',r)
print(c)
# b = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city")
# print(b)

