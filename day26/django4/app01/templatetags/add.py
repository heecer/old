#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def Add(a1,a2):
    return a1+a2

@register.filter
def ADD(a1,a2):
    return a1+a2