#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #项目根目录
sys.path.append(BASE_DIR)   #添加环境变量路径

# from conf import settings
from code import main
main.login()