#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import sys
print(sys.getdefaultencoding())#默认编码
s = '你好'
#uft-8转GBK
s1 = s.encode('utf-8')  #utf-8编码成Union,二进制码
s2 = s1.decode('GBK')   #二进制解码成GBK
print(s2)
#GBK转utf-8
s3 = s2.encode('GBK')   #gbk编码成Union,二进制码
s4 = s3.decode('utf-8') #二进制解码成utf-8
print(s4)
s5 = u'你好'  #
print(type(s5))
s6 = s5.encode().decode('GBk')
print(s6)

