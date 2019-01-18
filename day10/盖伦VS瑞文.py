#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer


class Garen:
    """定义英雄盖伦类型"""
    camp = 'Demacia'    #阵容

    def __init__(self, name, aggressivity = 58, life_value = 455):
        """英雄初始化"""
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def attack(self, enemy):
        """攻击"""
        enemy.life_value -= self.aggressivity


class Riven:
    """定义瑞文英雄类型"""
    camp = 'Noxus'  #阵容

    def __init__(self, name, aggressivity = 54, life_value =414):
        """英雄初始化"""
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def attack(self, enemy):
        """攻击"""
        enemy.life_value -= self.aggressivity

g1 = Garen('草丛伦')
r1 = Riven('兔女郎')
count = 0
while g1.life_value * r1.life_value >= 0:
    count += 1
    print('第%s回合'%count)
    print(g1.life_value,r1.life_value)
    r1.attack(g1) if count % 2 == 1 else g1.attack(r1)


