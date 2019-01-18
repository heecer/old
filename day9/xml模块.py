#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import xml.etree.ElementTree as et
xml = et.parse('xmltest.xml')
root = xml.getroot()
print(root)
print(root.tag)
#查
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)
#改
for year in xml.iter('year'):
    new_year = int(year.text)+5
    year.text = str(new_year)
    year.set('updated','year')
xml.write('xmltest更新.xml')
#删
xml1 = et.parse('xmltest更新.xml')
root1 = xml1.getroot()
for country in xml1.findall('country'):
    rank = int(country.find('rank').text)
    if rank >50 :
        root1.remove(country)
xml1.write('xml删减版.xml')
#增     在new_xml.py文件文件中



