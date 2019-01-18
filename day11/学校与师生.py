#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

class School(object):   #基类
    '''学校类'''

    def __init__(self, name, province, addr):
        self.name = name
        self.province = province
        self.addr = addr
        self.teachers = []
        self.students = []

    def enroll(self, stu_obj):
        '''注册'''
        self.students.append(stu_obj)
        print('恭喜%s学员注册成功'%stu_obj.name)

    def hire(self, tea_obj):
        '''注册'''
        self.teachers.append(tea_obj)
        print('%s员工成功入职'%tea_obj.name)

    def tell(self):
        '''信息输出'''
        print('''%s
        学校：%s,
        省份：%s,
        地址：%s
        '''%('*'*6, self.name,self.province,self.addr))

class SchoolMember(object):
    '''成员类'''

    def __init__(self, name, age, sex):
        '''成员初始化'''
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        '''信息输出'''
        print('''%s
        姓名：%s
        年龄：%s
        性别：%s
        '''%('*'*6, self.name, self.age, self.sex))

class Teacher(SchoolMember):
    '''老师类'''
    def __init__(self,name, age, sex, salary, course):
        '''老师初始化'''
        super(Teacher,self).__init__(name, age, sex)
        self.salary = salary
        self.course = course
    def tell(self):
        '''信息输出'''
        print('''
        *****老师信息******
            姓名：%s
            年龄：%s
            性别：%s
            工资：%s
            课程：%s
        '''%(self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        '''交课程'''
        print('%s 老师教 【%s】课程'%(self.name, self.course))
    pass
class Student(SchoolMember):
    '''学生类'''
    def __init__(self, name, age, sex, id, grade):
        '''老师初始化'''
        super(Student, self).__init__(name, age, sex)
        self.id = id
        self.grade = grade

    def tell(self):
        '''信息输出'''
        print('''
        *****学生信息******
           姓名：%s
           年龄：%s
           性别：%s
           学号：%s
           年级：%s
           ''' % (self.name, self.age, self.sex, self.id, self.grade))
    def pay_fees(self):
        '''付学费'''
        print('%s 学员已付费 ￥%s'%(self.name,1000))

school = School('Python学院',20,'中国')  #实例化类对象

t1 = Teacher('张三',28,'男',5000,'C++')
t2 = Teacher('李四',47,'女',50000,'Python')

s1 = Student('王五',18,'男',1901,'五')
s2 = Student('陈六',32,'女',1902,'六')

school.tell()   #调用信息输出功能
t1.tell()
s1.tell()

school.hire(t1)     #调用
school.hire(t2)
school.enroll(s1)
school.enroll(s2)
school.teachers[0].teach()
school.teachers[1].teach()
for student in school.students:
     student.pay_fees()




