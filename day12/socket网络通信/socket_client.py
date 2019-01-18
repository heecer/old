#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

#客户端
import socket

client = socket.socket()     #配置通信协议，生成链接对象
client.connect(('localhost',6969))  #访问地址，端口

client.send(b'Hello World')  #发送数据
data = client.recv(1024)    #接收服务器端的返回数据
print('data:',data.decode('utf-8'))
client.close()  #关闭客户端



