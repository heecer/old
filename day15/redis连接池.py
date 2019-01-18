#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import redis

pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name','张三')
print(r.get('name').decode())
r.setex('name','李四',5)
print(r.get('name'))