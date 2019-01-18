#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import hashlib

md5 = hashlib.md5()
md5.update(b'hello')
print(md5.hexdigest())
md5.update('world'.encode('utf-8'))
print(md5.hexdigest())