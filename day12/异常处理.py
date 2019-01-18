#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
a = 'python'
try:
     int(a)
except Exception as e:      #万能异常
    print('异常:',e)
except (IndexError,KeyError) as e:
    print('异常:', e)
else:       #当没有异常，就执行
    print('当没有异常，就执行')
finally:        #不管有无异常，都要执行
    print('不管有无异常，都要执行')