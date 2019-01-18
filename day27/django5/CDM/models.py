from django.db import models

# Create your models here.

class Admin(models.Model):
    '''超级管理员'''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class Usergroup(models.Model):
    '''用户组'''
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=64)

class User(models.Model):
    '''用户'''
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    user_to_group = models.ForeignKey(to='Usergroup',to_field='id',on_delete=models.CASCADE)
