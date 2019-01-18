#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))  #连接pika服务器连接

channel = connection.channel()  #创建管道

channel.queue_declare(queue='rpc_queue')    #声明队列


def fib(n):
    '''斐波拉契数列'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))    #返回客户端发送配置
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()   #开始发送