#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
str = 'hello Python {你好}'
print(str.capitalize())
print(str.count('o'))
print(str.encode('utf-8'))
print(str.endswith('thon'))
print(str[str.find('Py'):])#字符串切片
print(str.format(你好='你好，Python'))#格式化
print(str.format_map({'你好':'Python'}))#字典格式化
print(str.isalpha())#判断纯英文
print(str.isalnum())#判断阿拉伯文
print(str.islower())#判断小写
print(str.isupper())#判断大写
print(str.isspace())#判断空格
print(str.isdigit())#判断整数
print(str.isnumeric())#判断数字
print(str.isdecimal())#判断十进制
print(str.isidentifier())#判断合法的变量名
print(str.istitle())#判断标题
print('~'.join(str))#插入
print(str.center(50,'-'))#左右补全
print(str.ljust(30,'-'))#右补全
print(str.rjust(30,'-'))#左补全
print(str.lower())#小写
print(str.upper())#大写
print(str.strip())#取空格和回车\n

p=str.maketrans('abcdefghij','0123456789')#翻译
print(str.translate(p))
print(str.replace('o','O'))#替换
print(str.rfind('o'))#查找到最后的位置
print(str.split())#分割成列表
print('a\nb\nc'.splitlines())#换行符分割
print('a\nb\nc'.split('\n'))
print(str.swapcase())#大小写互转
print(str.title())#转标题

