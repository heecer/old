#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
def handle_index():
    f = open('Views/index.html','rb')
    data = f.read()
    f.close()
    return data
    # return ["<h1>Hello,Index</h1>".encode('utf-8'),]

def handle_date():
    return ["<h1>Hello,Date</h1>".encode('utf-8'),]