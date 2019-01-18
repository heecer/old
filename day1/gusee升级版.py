#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
AGE = 28
count=0
while count < 3:
    guess_age = int(input('age:'))
    if guess_age == AGE:
        print('猜到了，666')
        break
    elif guess_age < AGE :
        print('猜小了')
    elif guess_age > AGE:
        print('猜大了')
    count += 1
    if count == 3:
        contine_comfire = input('是否继续玩y/n：')
        if contine_comfire != 'n':
            count = 0
        else:
            print('猜数字游戏结束')
