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
else:
    exit('输入超过3次\n猜数字游戏结束')


# while True:
#     if count == 3:
#         break
#     guess_age = int(input('age:'))
#     if guess_age == AGE:
#         print('猜到了，666')
#         break
#     elif guess_age < AGE :
#         print('猜小了')
#     elif guess_age > AGE:
#         print('猜大了')
#     count += 1
# print('猜数字游戏结束')


for i in range(3):
    guess_age = int(input('age:'))
    if guess_age == AGE:
        print('猜到了，666')
        break
    elif guess_age < AGE :
        print('猜小了')
    elif guess_age > AGE:
        print('猜大了')
    count += 1
else:
    print('输入超过3次\n猜数字游戏结束')