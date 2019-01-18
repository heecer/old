#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
while True:
    for i in menu:
        print(i)
    choice = input('选择：')
    if choice in menu:
        while True:
            for j in menu[choice]:
                print('\t',j)
            choice2 = input('选择：')
            if choice2 in menu[choice]:
                while True:
                    for k in menu[choice][choice2]:
                        print('\t\t',k)
                    choice3 = input('选择')
                    if choice3 in menu[choice][choice2]:
                        while True:
                            for  m in menu[choice][choice2][choice3]:
                                print('\t\t\t',m)
                            choice4 = input('最后一层，请按b返回上层：')
                            if  choice4 == 'b':
                                break
                            elif choice4 == 'q':
                                exit(print('\033[31;1m%s\033[0m'%'退出'))
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit(print('\033[31;1m%s\033[0m' % '退出'))
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit(print('\033[31;1m%s\033[0m' % '退出'))

    elif choice == 'q':
        exit(print('\033[31;1m%s\033[0m' % '退出'))