#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socket,hashlib
client = socket.socket()    #实例链接对象
client.connect(('localhost',8000))  #连接配置
while True:
    cmd = input('>>:').strip()      #用户输入
    file_name = cmd.split()[1]
    if len(cmd) == 0:continue       #判断是否为空，重新输入
    if cmd.startswith('get'):       #判读输入是否是以‘get’开头
        client.send(cmd.encode('utf-8'))       #发送数据
        res_size = client.recv(1024)    #接收数据
        res_size = int(res_size.decode())
        print('文件大小：',res_size)
        client.send(b'ack')     #发送校验，避免粘包

        receive_size = 0
        m = hashlib.md5()       #实例MD5对象
        f = open(file_name + '.new', 'wb')  # 打开文件
        while receive_size < res_size:      #判断接收数据与文件大小
            if res_size - receive_size > 1024:  #接收一次完整数据大小1K
                size = 1024
            else:
                size = res_size - receive_size  #接收剩余的数据大小
                print('最后一次接收数据大小：',size)
            data = client.recv(size)    #接收数据
            m.update(data)      #数据加密
            receive_size += len(data)
            f.write(data)       #写入文件
        else:
            new_md5 = m.hexdigest()    #传输完成
            print('下载完成',new_md5)
            f.close()
        server_md5 = client.recv(1024)  #接收服务器端发送的MD5
        print('新文件MD5:',new_md5)
        print('服务器文件MD5:', server_md5)
client.close()