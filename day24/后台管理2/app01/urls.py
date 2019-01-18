#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from app01 import views
urlpatterns = [
    url(r'^login/', views.login),
    url(r'^orm/', views.ORM),
    url(r'^index/', views.index),
    url(r'^user/',views.user),
    url(r'^groups/',views.groups),
    url(r'^user_detail-(\d+)/',views.user_detail),
    url(r'^userdel-(\d+)/',views.userdel),
    url(r'^useredit-(\d+)/',views.useredit),
    url(r'^groupdel-(\d+)/',views.groupdel),
]