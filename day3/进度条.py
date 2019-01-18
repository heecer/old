#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import sys ,time

for i in range(10):
    sys.stdout.write('#')   #输出到屏幕
    sys.stdout.flush()  #强制刷新输出
    time.sleep(1)   #间隔一秒