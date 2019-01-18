#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socket,hashlib
client = socket.socket()
client.connect(('localhost',8000))
while True:
    cmd = input('>>:').strip()
    file_name = cmd.split()[1]
    if len(cmd) == 0:continue
    if cmd.startswith('get'):
        client.send(cmd.encode('utf-8'))
        res_size = client.recv(1024)

        print('文件大小：',res_size.decode())
        client.send(b'ack')
        receive_size = 0
        receive_data = b''
        f = open(file_name+'.new','wb')
        while receive_size < int(res_size.decode()):
            data = client.recv(1024)
            receive_size += len(data)
            f.write(data)
        else:
            print('下载完成',receive_size)
            f.close()
client.close()





