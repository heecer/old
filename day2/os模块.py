#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import os
# os.system('calc')
cmd_res = os.system('dir')#输出到屏幕上，无内存存储
print('--->',cmd_res)
cmd_res = os.popen('dir').read()
print('--->>',cmd_res)
os.mkdir('test.py')
os.mkdir('os')