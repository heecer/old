#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import json
info = {}
def write_info(dict):
    '''写入json文件'''
    info = json.dumps(dict,ensure_ascii=False)
    with open('city','w',encoding='utf-8')as f:
        f.write(info)

def open_info():
    '''打开json文件'''
    f = open('city','r',encoding='utf-8')
    info = json.loads(f.read())
    f.close()
    return info

def show_info(info):
    '''显示城市信息'''
    while True:
        if type(info) is dict:
            for i in info:
                print(i)
        else:
            flag = 1
            print(info)
            choice = input('最底层请选着： 1、增加；3、删除 ：').strip()
            while flag:
                if choice == '1'or choice == '3'or choice == 'b':
                    flag = 0
                else:
                    choice = input('请选着： 1、增加；3、删除 ：').strip()


        choice = input('请选着： 1、增加；2、城市；3、删除 ：').strip()
        return choice

def change_info(info):
    '''增加，修改，删除城市'''
    city = input('城市：').strip()
    companny = input('公司：').strip()
    if city not in info:
        info.setdefault(city,companny)
    else:
        change_or_del = input('修改c或者删除d：')
        if  change_or_del == 'c':
            info[city] = companny
        elif change_or_del == 'd':
            del info[city]
        else:
            show_info(info)
    write_info(info)
    choice = show_info(info)
    return choice
def choice_info(info):
    '''进入下一级菜单'''
    key = input('请选着城市：').strip()
    if key in info:
        Info = info[key]
        return key,Info,show_info(Info)

def do(a,info):
    '''增加，选着，删除，后退'''
    while True:
        if  a == '1':
            print(info)
            a = change_info(info)
        if a == '2':
            key,info,a= choice_info(info)
            do(a, info )
        # elif a == '3':
        #     info.pop(key)
        #     break
        elif a == 'b':
            show_info(info)
            break
        show_info(info)
def run():
    info = open_info()
    choice = show_info(info)
    while True:
        do(choice,info)
run()





