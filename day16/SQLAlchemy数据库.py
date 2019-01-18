#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,func
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:123456@localhost/test",
                       encoding='utf-8', echo=False)     #创建db连接对象

Base = declarative_base()  # 生成orm基类

class User(Base):
    '''创建数据表类'''
    __tablename__ = 'ABC'  # 表名
    id = Column(Integer, primary_key=True)  #字段名和格式
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return '<%s name:%s,passwd:%s>'%(self.id,self.name,self.password)

class Student(Base):
    __tablename__ = 'student'
    stu_id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable= False)
    age = Column(Integer,nullable=False)
    register_date = Column(onupdate=True,nullable=False)
    def __repr__(self):
        return '<%s name:%s,AGE:%s,Date:%s>'%(self.stu_id,self.name,self.age,self.register_date)

Base.metadata.create_all(engine)  # 创建表结构
#创建数据
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例,相当于cursor

# user_obj = User(name="张三", password="1234")  # 生成你要创建的数据对象
# user_obj1 = User(name="李四", password="1234")
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj1)
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
data = Session.query(User).filter_by().all()
print(data)
# data1 = Session.query(User).filter(User.id==1).first()
# data1.password = 'abc123'
# print(Session.query(User).filter(User.name.in_(['张三','李四'])).count())   #统计
# print(Session.query(User.name,func.count(User.name)).group_by(User.name).all())     #分组统计
# stu1 = Student(name ='张三',age = 20,register_date='2018-10-13')
# stu2 = Student(name ='李四',age = 25,register_date='2018-10-13')
# Session.add(stu1)
# Session.add(stu2)
print(Session.query(User,Student).filter(User.id == Student.stu_id).all())
Session.commit()  # 现此才统一提交，创建数据