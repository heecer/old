#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
f1 = open('昨日重现','r',encoding='utf-8')
f2 = open('昨日重现-修改版.txt',mode='w',encoding='utf-8')
for line in f1: #循环每一行
    if '肆意的快乐' in line: #匹配判断
        line = line.replace('我','世界')   #替换字符串
    f2.write(line)  #写入
f1.close()
f2.close()
