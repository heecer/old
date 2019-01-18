from django.db import models
from django.db.models import Model

# Create your models here.

class User(Model):
    '''用户数据表类'''
    name = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(max_length=16,verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    user_type = models.ForeignKey(to='UserType',to_field='id',on_delete=models.CASCADE)
    user2app = models.ManyToManyField(to='App')  # 第三张表关联
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class UserType(Model):
    type = models.CharField(max_length=32)

class App(Model):
    '''应用数据表'''
    app_name = models.CharField(max_length=32)


#################################
# class UserToApp(Model):
#     '''User和APP,多对多第三张表'''
#     uid = models.ForeignKey(to='User',to_field='id',on_delete=models.CASCADE)
#     aid = models.ForeignKey(to='App',to_field='id',on_delete=models.CASCADE())
#################################