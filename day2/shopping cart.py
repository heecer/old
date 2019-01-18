#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
products = [
    ('Iphone', 8999),
    ('Mac Pro', 1300),
    ('Starbuck Latte', 31),
    ('Python Book', 99),
]
shopping_list = []
money = input('请输入你的存款：')
if money.isdigit():  #整数判断
    money = int(money)
    while True:
        for index , item in enumerate(products):  #枚举商品列表
            # print(products.index(item),item)
            print(index,item)
        # break
        choose = input('请选着商品：')
        if choose.isdigit():  #整数判断
            choose = int(choose)
            if choose < len(products) and choose >=0:  #判断输入是否在商品数量范围
                pro_item = products[choose]
                if money >= pro_item[1]:  #判断余额与商品的价格
                    shopping_list.append(pro_item)  #添加到购物车列表
                    money -= pro_item[1]  #扣钱
                    print('%s-->加入购物车，余额：\033[31;1m%s\033[0m' %(pro_item,money))
                else:
                    print('\033[41;1m你的余额不足，剩余%s元\033[0m'%(money))
            else:
                print('输入的商品不存在：{}'.format(choose))
        elif choose == 'q':#退出
            print('shopping list'.center(50,'-'))
            for i in shopping_list:  #循环遍历购物车列表
                print(i)
            # print('你的余额：\033[31;1m%s\033[0m'%money)
            exit(print('你的余额：\033[31;1m%s\033[0m'%money))
        else :
            print('输入错误')


