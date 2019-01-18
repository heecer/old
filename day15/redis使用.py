#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import redis

r = redis.Redis(host='127.0.0.1',port=6379)
r.set('python','hell world')
print(r.get('python'))
