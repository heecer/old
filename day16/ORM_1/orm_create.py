#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:123456@localhost/A",
                        encoding='utf-8', echo=False)
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
#多外键关联
    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(32))
    city = Column(String(32))
    state = Column(String(32))

Base.metadata.create_all(engine)  #创建表结构