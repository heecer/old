#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import pymysql

connect = pymysql.connect(host='localhost',port=3306,
                          user='root',password='123456',db='test')  #创建链接

cursor = connect.cursor()   #创建游标
# effect_row = cursor.execute('show tables')  #执行SQL语句，并返回响应行数
# print(effect_row)
# print(cursor.fetchone())    #显示数据
# print(cursor.fetchone())    #显示数据
# effect_row1 = cursor.execute('select * from student')
# print(cursor.fetchall())
# effect_row2 = cursor.execute('select * from programming')
# print(cursor.fetchall())
data = [
    ("jave",10,"018-10-7"),
    ("ruby",1,"2018-10-7"),
]
# cursor.executemany("insert into student (name,age,register_date) values(%s,%s,%s)",data)
# connect.commit()
cursor.execute('delete from student where stu_id>3')
connect.commit()
cursor.execute('select * from student')
print(cursor.fetchall())
cursor.close()
connect.close()