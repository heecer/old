#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import os ,sys
print(__file__)     #相对路径
print(os.path.abspath(__file__))    #文件绝对路径
print(os.path.dirname(os.path.abspath(__file__)))   #文件绝对路径