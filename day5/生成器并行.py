#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
# c = consumer('python')
# c.__next__()
# b = '韭菜鸡蛋'
# c.send(b)
# c.__next__()
# c.__next__()

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        print('--------')
        c2.send(i)

producer("alex")

