#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import threading
import time
event = threading.Event()   #事件标志位
def lighter():
    count = 0
    event.set()     #默认设置绿灯
    while True:
        if count > 3 and count < 7:
            event.clear()   #清除标志位
            print('\033[41;1m红灯\033[0m')
        elif count > 7:
            event.set()     #设定标志位
            count = 0
        else:
            print('\033[42;1m绿灯\033[0m')
        time.sleep(1)
        count += 1
def car(name):
    while True:
        if event.is_set():
            print('\033[32;1m绿灯亮\033[0m %s通行' % name)
        else:
            print('\033[31;1m红灯亮\033[0m %s等待' % name)
            event.wait()

l = threading.Thread(target=lighter)
l.start()
car1 = threading.Thread(target=car,args=('福特',))

car1.start()