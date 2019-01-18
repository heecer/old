#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello World!</h>')