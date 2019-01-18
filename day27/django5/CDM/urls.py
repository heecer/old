"""django5 URL Configuration

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
from django.views import View
from CDM import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^home/$', views.home),
    url(r'^users/$', views.users),
    url(r'^groups-(?P<nid>\d+)/$', views.groups),
    # url(r'^login_verfy/$', views.login_verfy),
    url(r'^add_user/$', views.add_user),
    url(r'^add_group/$', views.add_group),
    url(r'^edit_user-(?P<nid>\d+)/$', views.edit_user),
    url(r'^del_user/$', views.del_user),
]
