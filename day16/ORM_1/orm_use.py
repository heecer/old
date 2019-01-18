#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from day16.ORM_1 import orm_create as dorm
from sqlalchemy.orm import sessionmaker
import time

Session_class = sessionmaker(bind=dorm.engine)
Session = Session_class()

addr1 = dorm.Address(street='空港',city='渝北',state='渝')
addr2 = dorm.Address(street='观音桥',city='江北',state='渝')
addr3 = dorm.Address(street='朝天门',city='渝中',state='渝')
# Session.add_all([addr1,addr2,addr3])
# time.sleep(3)
cus1 = dorm.Customer(name='张三',billing_address_id=addr1,shipping_address_id=addr2)
cus2 = dorm.Customer(name='李四',billing_address_id=addr3,shipping_address_id=addr3)

Session.add_all([addr1,addr2,addr3,cus1,cus2])
Session.commit()
