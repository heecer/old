#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
use,passwd = 'python','123'
def auth(func):
    '''auth装饰器'''
    def wrapper(*args,**kwargs):
        user_name = input('用户名：')

        if user_name == use:
            password = input('密码：')
            if password == password:
                print('\033[34;1m%s\033[0m'%'登录成功')
                func(*args,**kwargs)
        else:
            exit('\033[31;1m%s\033[0m'%'用户名不存在')
    return wrapper

def index():
    '''网站首页'''
    print('首页')
@auth
def home():
    '''用户主页'''
    print('主页')
@auth
def bbs():
    '''用户论坛'''
    print('论坛')
index()
home()
bbs()