#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

#服务器端
import socket
server = socket.socket()     #创建链接对象
server.bind(('localhost',6969))      #绑定要监听的地址端口
server.listen()      #监听,默认监听无数个，监听几个
print('等待监听')
fd, addr = server.accept()      #等待接收,返回请求链接对象fd和请求地址addr
print('正在监听',fd,addr)

data = fd.recv(1024)     #接收数据
print('data:',data.decode('utf-8'))
fd.send(data.upper())    #发送返回数据
server.close()       #关闭服务器

