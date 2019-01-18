#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import json
info = {
    'name':'python',
    'job':'IT',
    'sex':'falm'
}
print(json.dumps(info))
f = open('缓存','w',encoding='utf-8')
# f.write(str(info))
f.write(json.dumps(info))
f.close()