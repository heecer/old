#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import pickle
info = {
    'name':'python',
    'job':'IT',
    'sex':'falm'
}
print(pickle.dumps(info))
f = open('缓存1','wb')
# f.write(pickle.dumps(info))
pickle.dump(info,f) #f.write(pickle.dumps(info))
f.close()