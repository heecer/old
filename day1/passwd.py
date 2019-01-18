#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import getpass  #密文模块
Username = 'oldboy'
Password = '1234'
username = input('userame:')
# password = input('password:')
password = getpass.getpass('password:')
if username == Username and password == Password:
    print('''
    *****登陆成功*********
    姓名：{}
    密码：{}'''.format(username,password))
else:
    print('姓名或者密码输入错误')
# print(username,password)
