#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import shutil,os,time
f1 = open('test','r',encoding='utf-8')
f2 = open('test复制版','w',encoding='utf-8')
shutil.copyfileobj(f1,f2)   #拷贝文件句柄
shutil.copyfile('test','test改进版')   #拷贝文件
# shutil.copytree('test1','test2')
Path = os.path.dirname(__file__)
print(Path)
# shutil.copytree(Path,'day9')  #递归复制文件夹
# shutil.rmtree('day9')   #递归删除文件
shutil.make_archive('\\test','zip')
time.sleep(3)
os.remove('test.zip')