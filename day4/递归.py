#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

def add_recursive(a):
    print(a)
    if a < 10:
        add_recursive(a + 1)

add_recursive(0)