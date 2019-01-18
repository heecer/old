#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

with open(r"E:\老男孩\作业\day1\user.txt",'r+') as f_name:
    Name = eval(f_name.read())
    count = 0
    while count < 3:
        username = input('username:')
        password = input('password:')
        # password = getpass.getpass('password:')
        if username in Name and password == Name[username]:
            print('''
            *******登录成功******
            欢迎进入Python世界，{}'''.format(username))
            break
        else:
            with open(r'E:\老男孩\作业\day1\newuser.txt', 'a+') as f_user:
                f_user.write('{}:{}\n'.format(username, password))
            print('用户名或者密码错误，请重新输入!','剩余%d次' %(2-count))

        count += 1
    if count == 3:

        print('错误次数超过3次，10分钟后重新登录')


