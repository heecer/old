#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import configparser
'''创建配置文件'''
conf = configparser.ConfigParser()
conf['default'] = {'ServerAliveInterval' : '45',
                    'Compression' : 'yes',
                    'CompressionLevel' : '9',
                    'ForwardX11' : 'yes'}
conf['bitbucket.org'] = {}
conf['bitbucket.org']['user'] = 'python'
conf['topsecret.server.com']  = {}
conf['topsecret.server.com']['Port'] = '50022'
conf['topsecret.server.com']['ForwardX11'] = 'no'
with open('conf.ini','w') as cf:
    conf.write(cf)
conf1 = configparser.ConfigParser()
conf1.read('conf.ini')
print(conf1.sections())
print(conf1.options('default'))


