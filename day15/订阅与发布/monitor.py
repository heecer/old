#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import redis

class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='localhost')   #连接Redis服务器
        self.chan_sub = 'fm104.5'   #接收频道
        self.chan_pub = 'fm104.5'   #发布频道

    def public(self, msg):
        '''发布消息'''
        self.__conn.publish(self.chan_pub, msg)     #发布频道，消息
        return True

    def subscribe(self):
        '''订阅频道'''
        pub = self.__conn.pubsub()  #打开收音机
        pub.subscribe(self.chan_sub)    #调到频道
        pub.parse_response()    #准备接收
        return pub