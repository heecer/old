#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import pika,time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare('hello1',durable=True)

def callback(ch, method, properties, body):
    # time.sleep(20)
    print('-->>Received: %r'%body.decode())
    # ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello1'
                    , no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()