#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socket,os,hashlib
server = socket.socket()
server.bind(('localhost',8000))
server.listen()
while True:
    fd, addr = server.accept()
    print(fd, addr)
    while True:
        data = fd.recv(1024)
        if not data:
            print('客户端断开')
            break
        cmd, file_name = data.decode().split()
        print(cmd,file_name)

        if os.path.isfile(file_name):
            f = open(file_name,'rb')
            m = hashlib.md5()
            file_size = os.stat(file_name).st_size
            fd.send(str(file_size).encode('utf-8'))
            fd.recv(1024)
            for line in f:
                m.update(line)
                fd.send(line)
            f.close()
            print('MD5值：', m.hexdigest())
            fd.send(m.hexdigest().encode('utf-8'))
        print('Done')
server.close()
