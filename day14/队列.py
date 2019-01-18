#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import queue
'''队列'''
q = queue.Queue()   #先进先出
q.put(1)
q.put(2)
q.put(3)
for i in range(q.qsize()):
    print(q.get())


q1 = queue.LifoQueue()   #后进先出
q1.put(1)
q1.put(2)
q1.put(3)
for i in range(q1.qsize()):
    print(q1.get())

q = queue.PriorityQueue()   #先进先出
q.put((1,'v'))
q.put((4,'b'))
q.put((9,'a'))
for i in range(q.qsize()):
    print(q.get())