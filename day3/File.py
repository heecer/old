#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
f = open('昨日重现','r+',encoding='utf-8')
print(f)
print('第一行：',f.readline())  #读取一行
# print(f.readlines())
# for i in range(5):  #多行读取
#     print(f.readline().strip())
# print('__________________')
# for index,line in enumerate(f.readlines()):   #读取到4行
#     if index == 4:
#         print('***********************')
#         break
#     print(line.strip())
# count = 0
# for line in f: #读取到6行
#     if count == 7:
#         print('88888888888888888888888888')
#         break
#     count +=1
#     print(line.strip())
# print(f.tell()) #读取光标位置
# print(f.read(5))
# print(f.tell())
# f.seek(0)   #返回首个字符
# print(f.readline())
# print(f.encoding)
# print(f.isatty())   #判断终端
# print(f.seekable()) #判断光标移动
# print(f.readable()) #判断文件可读性
f.seek(0)
f.write('----hello world')
print(f.readline())
# f.flush() #强制刷入硬盘
# print(f.readline())

f = open('二进制.txt','wb')    #二进制写入
f.write('hello world'.encode()) #字符编码
f = open('二进制.txt','rb')       #二进制读取
print(f.readline())