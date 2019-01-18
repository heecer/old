#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import pickle
f = open('缓存1','rb')
# data = pickle.loads(f.read())
data = pickle.load(f)   #data = pickle.loads(f.read())
f.close()
print(data['job'])