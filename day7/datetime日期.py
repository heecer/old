#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import datetime
date = datetime.datetime.now()  #当前时间
print(date)
date = datetime.datetime.now()+datetime.timedelta(3)    #当前时间加3天
print(date)
date = datetime.datetime.now()+datetime.timedelta(-3)    #当前时间减3天
print(date)
date = datetime.datetime.now()+datetime.timedelta(hours=3)    #当前时间加3小时
print(date)
date = datetime.datetime.now()+datetime.timedelta(hours=-3)    #当前时间减3小时
print(date)