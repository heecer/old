#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
'''
roles = {
    1:{'name':'Alex',
       'role':'terrorist',
       'weapon':'AK47',
       'life_value': 100,
       'money': 15000,
       },
    2:{'name':'Jack',
       'role':'police',
       'weapon':'B22',
       'life_value': 100,
        'money': 15000,
       },
    3:{'name':'Rain',
       'role':'terrorist',
       'weapon':'C33',
       'life_value': 100,
       'money': 15000,
       },
    4:{'name':'Eirc',
       'role':'police',
       'weapon':'B51',
       'life_value': 100,
       'money': 15000,
       },
}
'''
class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("%s shooting..."%self.name)

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)


r1 = Role('Alex', 'police', 'AK47') #生成一个角色，类对象，类的实例化
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色
print(r1.shot())
print(r2)