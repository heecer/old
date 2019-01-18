#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socket,os,time
server = socket.socket()
server.bind(('localhost',8000))
server.listen()
while True:
    fd, addr = server.accept()
    print(fd,addr)
    while True:
        data = fd.recv(1024)
        if not data:
            print('客户端断开')
            break
        print('指令：',data)
        res = os.popen(data.decode('utf-8')).read()
        res_size = len(res.encode('utf-8'))
        if res_size == 0:
            res = '空命令'
        fd.send(str(res_size).encode('utf-8'))
        # time.sleep(0.5)     #缓冲区溢出，防止粘包
        client_ack = fd.recv(1024)
        fd.send(res.encode('utf-8'))
        print('Done')
server.close()
