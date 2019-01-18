#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import sys,os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
# os.mkdir(BASE_DIR+r'\1')
find_cmd = sys.argv[1]  #cmd环境中传参
replace_cmd = sys.argv[2]


with open(BASE_DIR+'\docs_change.txt' , 'w' , encoding='utf-8')as f:  #打开文件
    f1 = open(BASE_DIR + '\docs', 'r', encoding='utf-8')
    for line in f1:
        if find_cmd in line:
            line = line.replace(find_cmd,replace_cmd)
        f.write(line)
    f1.close()

exit('结束')
