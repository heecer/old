#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import hmac
m = hmac.new('name'.encode('utf-8'),'张三'.encode('utf_8'))
print(m.hexdigest())
