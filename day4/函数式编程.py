#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import time
def open_write():   #定义过程
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('test','a+')as f:
        ''''打开文件，写入'''
        f.write('%s :hell world\n'%time_current)

def fun1():
    '''comment'''
    print('功能1')
    open_write()
    # with open('test', 'ab')as f:
    #     ''''打开文件，写入'''
    #     f.write('hell world')

def fun2():
    '''comment'''
    print('功能2')
    open_write()
    # with open('test', 'ab')as f:
    #     ''''打开文件，写入'''
    #     f.write('hell world')
    return 'OK'

def fun3():
    '''comment'''
    print('功能3')
    open_write()
    # with open('test', 'ab')as f:
    #     ''''打开文件，写入'''
    #     f.write('hell world')
    return 1,'hell',['hello','world'],{'name':'python'}

print(fun1())   #返回None
print(fun2())   #返回object
print(fun3())   #返回tupel类型
