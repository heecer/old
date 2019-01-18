#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import threading,time
class MyThread(threading.Thread):
    def __init__(self,name,Time):
        super(MyThread,self).__init__()
        self.name = name
        self.Time = Time

    def run(self):
        print('线程',self.name)
        time.sleep(self.Time)
        # print('线程结束',self.name)


t1 = MyThread('cmd',2)
t2 = MyThread('mspaint',4)

start_time = time.time()
t1.start()
t2.start()
t1.join()       #线程等待
print('主线程结束')
t2.join()
print('用时：',time.time() - start_time)


t_obj = []
start = time.time()
for i in range(50):
    t = MyThread(str(i),2)
    t.setDaemon(True)       #守护线程
    t.start()
    t_obj.append(t)
# for t in t_obj:
#     t.join()
print('用时：',time.time() - start)