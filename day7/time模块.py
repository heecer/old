#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import time,datetime
'''时间日期模块'''
print(time.time())
print(time.localtime())     #时间戳转换成本地时间元组格式，9个元素
print(time.gmtime())    #时间错转换成UTC的时间元组
x = time.localtime()    #时间错转换成本地的时间元组
print('\033[31;1m%s\033[0m'%x.tm_year)
print(time.mktime(x))   #时间元组转换成时间戳

print(time.strftime('%Y-%m-%d %X'))     #时间元组转换成格式化的字符串时间
print(time.strptime('2018-09-16 22:51:25','%Y-%m-%d %X'))    #字符串时间转换成时间元组
print(time.asctime(time.localtime()))   #时间元组转换成字符串
print(time.ctime(time.time()))      #时间戳转换成字符串

