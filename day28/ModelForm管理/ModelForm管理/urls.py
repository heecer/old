"""ModelForm管理 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app01 import views

urlpatterns = [
   url(r'index/$',views.index),
   url(r'userInfo/$',views.userInfo),
   url(r'edit-(\d+)/$',views.userEdit),
   url(r'ajax_request/$',views.ajax_request),
   url(r'ajax_view/$',views.ajax_view),
   url(r'upload_file/$',views.upload_file),
   url(r'upload/$',views.upload),
   url(r'checkcode/$',views.checkcode),
   url(r'check_code.html/$',views.check_code),
   url(r'validatecode/$',views.validatecode),
   url(r'kindeditor/$',views.kindeditor),
   url(r'upload_img/$',views.upload_img),
   url(r'file_manager/$',views.file_manager),
]
