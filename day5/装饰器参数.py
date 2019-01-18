#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
use,passwd = 'python','123'
def auth(auth_type):    #装饰参数
    '''装饰器auth'''
    print(auth_type)
    def wrapper(func):
        '''外层wrapper'''
        def wrapper1(*args,**kwargs):
            '''附加功能'''
            if auth_type == 'local':
                print('****本地验证*****')
                user_name = input('用户名：').strip()
                if user_name == use:
                    password = input('密码：').strip()
                    if password == password:
                        print('\033[34;1m%s\033[0m' % '本地登录成功')
                        func(*args, **kwargs)
                else:
                    exit('\033[31;1m%s\033[0m' % '用户名不存在')
            elif auth_type == 'ldap':
                exit('服务器验证')
        return wrapper1
    return wrapper

def index():
    '''网站首页'''
    print('首页')
@auth(auth_type = 'local')
def home():
    '''用户主页'''
    print('主页')
@auth(auth_type = 'ldap')
def bbs():
    '''用户论坛'''
    print('论坛')
index()
home()
bbs()