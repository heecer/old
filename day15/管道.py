#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import redis

pool = redis.ConnectionPool(host='localhost', port=6379,db=2)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

pipe.set('name', 'alex')
pipe.set('role', 'sb')

pipe.execute()