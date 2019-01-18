#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socket
client = socket.socket()
client.connect(('localhost',7000))
while True:
    msg = input('>>:').strip()
    if len(msg) == 0:continue
    client.send(msg.encode('utf-8'))
    # print(data.decode())
    f = open('1.mkv','wb')
    data = client.recv(102400000)
    f.write(data)
    f.close()
    server_msg = client.recv(1024).decode()
    print(server_msg)

client.close()
