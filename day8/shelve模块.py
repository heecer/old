#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import shelve,datetime,json
info = {'name':'python',
        'age':30,
        'job':'IT'
        }
user = {'张三':'male',
        '李四':'female',
        '王五':'male'
        }
f = shelve.open('shelve_info')     #保存数据
f['name'] = info
f['user'] = user
f['datetime'] = datetime.datetime.now()
f.close()

f1 = shelve.open('shelve_info')     #提取数据
print(f1.get('name'))
print(f1.get('user'))
print(f1.get('datetime'))
f1.close()

f2 = open('json_info','w')
json.dump(info,f2)      #保存为json格式
f2.close()
f3 = open('json_info','r+')
print(type(json.loads(f3.read())) )


