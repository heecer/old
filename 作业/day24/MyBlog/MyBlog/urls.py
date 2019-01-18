"""MyBlog URL Configuration

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
from django.conf.urls import url,include
from MyBlog import views

urlpatterns = [
    # url(r'',views.index),
    url(r'^login.html/$',views.login),
    url(r'^register.html/$',views.register),
    url(r'^check_code.html/$',views.check_code),
    # url(r'^article/$',views.article),
    url(r'^article/(?P<articletype_id>\d+)-(?P<category_id>\d+).html$',views.article),
    url(r'^cmdb/',include('CMDB.urls')),
    url(r'^home/',include('HOME.urls')),
    url(r'^weather/',views.weather),
    url(r'^jsonp/',views.jsonp),

]
