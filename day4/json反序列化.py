#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import json
f = open('缓存','r',encoding='utf-8')
# data = f.read()
data = json.loads(f.read())
f.close()
print(data['job'])
# print(eval(data)['job'])