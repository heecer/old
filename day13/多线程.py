#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import threading,time

def run(n):
    start = time.time()
    time.sleep(2)
    print('task', n)
    end = time.time()
    return print(end - start)
t1 = threading.Thread(target=run,args=('email',))
t2 = threading.Thread(target=run,args=('calc',))
t1.start()
t2.start()
# run('t1')
# run('t2')
print(threading.current_thread())   #主线程，程序本生
print(threading.activeCount())      #线程个数