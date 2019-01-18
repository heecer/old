#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import random
x = random.random()     #随机数[0,1)
print(x)
x = random.randint(1,9)     #随机整数
print(x)
x = random.randrange(1,9)   #随机区间值
print(x)
x = random.choice('hello')      #序列随机取值
print(x)
x = random.sample('world',2)    #抽样，序列中随机器几个元素
print(x)
x = [1,2,3,4,5,6]
random.shuffle(x)   #洗牌打乱
print(x)