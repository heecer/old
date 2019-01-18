#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import threading
import queue
import time

q = queue.Queue(maxsize=10)     #最大队列数
def Product(name, speed):
    count = 0
    while True:
        count += 1
    # for i in range(10):
        q.put('\033[31;1m%s\033[0m包子[%s]'%(name,count))
        print('%s-->共生产了：%s'%(name,count))
        time.sleep(speed)
def Consumer(name, speed):
    # while q.qsize() > 0:
    while True:
        print('%s：吃了【%s】' %(name, q.get()))
        time.sleep(speed)
        # q.task_done()

pro = threading.Thread(target=Product,args=('张三', 1))
pro.start()
con = threading.Thread(target=Consumer,args=('李四', 0.1))
con.start()
con1 = threading.Thread(target=Consumer,args=('王五', 0.2))
con1.start()
pro1 = threading.Thread(target=Product,args=('陈1', 2))
pro1.start()