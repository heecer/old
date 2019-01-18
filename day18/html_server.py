#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socket


def handle_request(connection):
    '''处理请求并返回'''
    data = connection.recv(1024)
    connection.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    connection.send(bytes("<h1 style='background-color:red;'>Hello, Seven<h1>",encoding='utf-8'))

def main():
    '''服务端接受'''
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',9000),)
    server.listen(5)
    while True:
        fd, addr = server.accept()
        handle_request(fd)
        fd.close()

if __name__ == '__main__':
    main()
