#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))    #实例化pika通信对象
channel = connection.channel()  #创建管道
channel.queue_declare(queue='hello')    #创建队列
channel.basic_publish(exchange='',  #发送信息
                      routing_key='hello',  #队列名
                      body='Hello,World!')  #消息
print('-->>Sent: Hello,World!')
connection.close()
