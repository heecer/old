#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
shopping_list = []
with open(r'E:\老男孩\作业\day2\foods.txt','r+',encoding='utf-8') as f:
    foods_list = eval(f.read())
with open(r'E:\老男孩\作业\day2\user.txt','r+',encoding='utf-8') as f:
    user_info = eval(f.read())
while True:
    user = input('请输入用户：')
    if user in user_info:   #判断用户是否存在
        print('{}的余额：{}元'.format(user,user_info[user]))
    else:
        money = input('请输入金额：')
        while not money.isnumeric():    #判断是否是数字
            money = input('请重新输入金额：')
        money = int(money)
        user_info.setdefault(user,money)
        user_info[user] = money
        f = open(r'E:\老男孩\作业\day2\user.txt','w+',encoding='utf-8')
        f.write(str(user_info))
        f.close()
    print(user_info)
    break
seq = 0
for i in foods_list:
    seq += 1
    print(seq,i,foods_list[i])
choice = input('请选着商品序号：')
while not choice.isnumeric():
    choice = input('请重新输入：')
choice = int(choice)
while choice >=0 and choice < seq:
    pass
    # print(foods_list.keys())
#     if foods_list[] < user_info[user]:
#         shopping_list.append(foods_list[])
#         user_info[user] -= foods_list[]
#         print('%s-->加入购物车，余额：\033[31;1m%s\033[0m' % ())
#     else:
#         print('\033[41;1m你的余额不足，剩余%s元\033[0m' % ())
# else:
#     print('输入的商品不存在：{}'.format(choice))
# if choice == 'q':  # 退出
#     print('shopping list'.center(50, '-'))
#     for i in shopping_list:  # 循环遍历购物车列表
#         print(i)
#     # print('你的余额：\033[31;1m%s\033[0m'%money)
#     exit(print('你的余额：\033[31;1m%s\033[0m' % ))
# else:
#     print('输入错误')