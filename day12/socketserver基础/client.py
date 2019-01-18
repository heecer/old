#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socket
host_port = ('localhost', 7000)
client = socket.socket()
client.connect(host_port)
while True:
    data = input('**:').strip()
    if len(data) == 0:continue
    client.send(data.encode('utf-8'))
    msg = client.recv(1024).decode()
    print(msg)
client.close()
