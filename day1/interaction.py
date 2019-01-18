#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

'''请输入用户的信息'''
name=input('username:')
password=input('password:')
age=input('age:')
job=input('job:')
salary=input('salary:')
print(name,password,end="\n")

info='''
------info of %s------
姓名：%s
年龄：%s
工作：%s
工资：%s
''' %(name,name,age,job,salary)#%s  占位符


info_2='''
------info of {}------
姓名：{}
年龄：{}
工作：{}
工资：{}
'''.format(name,name,age,job,salary)
# print(info_2)

info_3='''
------info of {Name}------
姓名：{Name}
年龄：{Age}
工作：{Job}
工资：{Salary}
'''.format(Name=name,Age=age,Job=job,Salary=salary)
print(info_3)