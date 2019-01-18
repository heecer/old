#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))    #实例化pika通信对象
channel = connection.channel()  #创建管道
channel.queue_declare(queue='hello1',durable=True)    #创建队列,持久队列
channel.basic_publish(exchange='',  #发送信息
                      routing_key='hello1',  #队列名
                      body='Hello,World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2     # make message persistent持久信息
                      ) ) #消息
print('-->>Sent: Hello,World!')
connection.close()
