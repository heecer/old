#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='localhost', port=8080, username='wupeiqi', password='123')
#连接配置
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stderr.read()
print(result)
# 关闭连接
ssh.close()