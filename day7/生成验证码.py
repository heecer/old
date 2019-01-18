#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import random
verifi_cofe =''
for i in range(4):
    '''生成4位验证码'''
    current = random.randrange(0,4) #猜出的数
    if current == i :
        temp = chr(random.randint(65,125))   #ascii值转换字母,随机单个字母
    else:
        temp = random.randint(0,9)      #随机单个数字
    verifi_cofe += str(temp)
print(verifi_cofe)