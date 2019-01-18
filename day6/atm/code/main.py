#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

'''临时账户数据存储，认证'''
use_data = {
    'account_ID': None,
    'is_authenticated': False,
    'account_data': None
}

def run():
    '''
    当程序开始运行，调用此程序，处理用户交互信息
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)