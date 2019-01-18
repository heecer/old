#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socket,os
client = socket.socket()
client.connect(('localhost',8000))
while True:
    cmd = input('>>:').strip()
    if len(cmd) ==0:continue
    client.send(cmd.encode('utf-8'))
    rec_size = client.recv(1024)
    print('数据大小：',rec_size)
    client.send('ack'.encode('utf-8'))
    receiver_size = 0
    receiver_data = b''
    while receiver_size < int(rec_size.decode('utf-8')):
        data = client.recv(1024)
        receiver_size += len(data)
        receiver_data += data
    else:
        print('接收到数据大小',receiver_size)
        print(receiver_data.decode('utf-8'))
client.close()
