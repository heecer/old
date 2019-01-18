#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socket
import os
server = socket.socket()
server.bind(('localhost',7000))
server.listen(5)
while True:
    fd, addr = server.accept()
    print(fd, addr)
    while True:
        data = fd.recv(102400000)
        print(data.decode())
        if  data.decode() == 'q':break
        else:
            # msg = input('>>：').strip().encode('utf-8')    #发送消息
            # res = os.popen(data.decode()).read()    #传送命令
            # fd.send(res.encode('utf-8'))
            f = open('E:/1.mkv','rb')   #文件传输
            data1 = f.read()
            fd.sendall(data1)
            f.close()
        fd.send('Done'.encode('utf-8'))
server.close()