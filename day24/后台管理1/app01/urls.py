#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from app01 import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.Index.as_view()),
    # url(r'^home/', views.home),
    url(r'^login/', views.login),
    # url(r'^user_info/', views.User_Info),
    # url(r'^detail-(?P<nid>\d+).html', views.Detail),
    # url(r'^index1/(\d+)/', views.Index1,name='user_in'),
    # url(r'^detail-(\d+)-(\d+).html', views.Detail),
    # url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.Detail),
]