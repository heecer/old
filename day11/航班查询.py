#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
class Flight(object):
    '''航班类'''
    def __init__(self,name:str):
        self.flight_name = name

    def cheak_status(self)->int:

        print('当前航班：%s' % self.flight_name)
        a= int(input('数字0-4：').strip())
        if a == 0:
            return 0
        elif a == 1:
            return 1
        elif a == 2:
            return 2
        elif a == 3:
            return 3
        else:
            return 4
    @property   #属性方法
    def flight_status(self):
        while True:
            status = self.cheak_status()
            if status == 0:
                print('航班离线')
            elif status == 1:
                print('航班安全抵达')
            elif status == 2:
                print('航班飞行中')
            elif status == 0:
                print('航班准备起飞')
            else:
                print('航班延迟')

air = Flight('波音747')
air.flight_status
