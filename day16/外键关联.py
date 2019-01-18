#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import sqlalchemy
from sqlalchemy import create_engine
from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,String,Column,func,ForeignKey,Date,VARCHAR
from sqlalchemy.orm import sessionmaker,relationship
engine = create_engine("mysql+pymysql://root:123456@localhost/abc",
                        encoding='utf-8', echo=False)     #创建db连接对象
Base = declarative_base()
class Student(Base):
    '''创建students表'''
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    register_date = Column(Date, nullable=False)

    def __repr__(self):
        return '<%s name:%s,age:%s,Date:%s>' % (self.id, self.name, self.age, self.register_date)

class Study_Record(Base):
    '''创建表'''
    __tablename__ ='study_record'
    id = Column(Integer,primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(VARCHAR(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('students.id'))

    student = relationship('Student',backref='stu_record')     #外键关联
    def __repr__(self):
        return '<%s day:%s,status:%s,stu_id:%s>' % (self.student.name, self.day, self.status, self.stu_id)

Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()

# stu1 = Student(name = '张三',age=5,register_date='2018-10-13')
# stu2 = Student(name = '李四',age=10,register_date='2018-10-14')
# s_rec1_1 = Study_Record(day=1,status='签到',stu_id=1)
# s_rec1_2 = Study_Record(day=2,status='旷课',stu_id=1)
# s_rec1_3 = Study_Record(day=3,status='签到',stu_id=1)
# s_rec2_1 = Study_Record(day=1,status='签到',stu_id=2)
# s_rec2_2 = Study_Record(day=2,status='旷课',stu_id=2)
# s_rec2_3 = Study_Record(day=3,status='迟到',stu_id=2)
#
# Session.add_all([stu1,stu2,s_rec1_1,s_rec1_2,s_rec1_3,s_rec2_1,s_rec2_2,s_rec2_3])

stu_obj = Session.query(Student).filter(Student.name=='张三').first()
print(stu_obj)
print(stu_obj.stu_record)
record = Session.query(Study_Record).filter(Study_Record.day ==2 ).first()
print(record)
Session.commit()