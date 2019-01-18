"""django4 URL Configuration

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
app_name = 'app01'
urlpatterns = [
    url(r'^index/', views.index,name='index'),
    # url(r'^index/', views.index,{'admin':'root'},name='index'),
    url(r'^template/', views.template),
    url(r'^test1/', views.test1),
    url(r'^test2/', views.test2),
    url(r'^test3/', views.test3),
    url(r'^login/$', views.login),
    url(r'^home/$', views.home),
    url(r'^order/$', views.Order.as_view()),
]
