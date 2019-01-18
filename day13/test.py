#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import threading

def hello():
    print('hello world')
t = threading.Timer(10,hello) #定时启动线程
t.start()