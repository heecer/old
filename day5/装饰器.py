#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import time

def wrapper(func):
    '''wrapper高阶函数'''
    start_time = time.time()
    stop_time = time.time()
    print('运行时间：\033[31;1m%s\033[0m秒' % (stop_time - start_time))
    return  func  #返回func()内存地址

def timer(func):
    '''高阶函数'''
    def wrapper():
        '''wrapper嵌套函数'''
        start_time = time.time()
        func()  #func()函数
        stop_time = time.time()
        print('运行时间：\033[31;1m%s\033[0m秒' % (stop_time - start_time))
    return wrapper  #返回wrapper内存地址
runtime = timer(time.localtime) #执行timetime.localtime()所用时间结果的内存地址
runtime()   #运行时间

def timer1(func):
    '''装饰器timer'''
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print('运行时间：\033[31;1m%s\033[0m秒'%(stop_time-start_time))
    return wrapper
@timer1
def time_sleep(s):
    '''延迟打印'''
    time.sleep(s)
    print('延迟\033[31;1m%s\033[0m秒'%s)

time_sleep(3)