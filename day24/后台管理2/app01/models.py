from django.db import models

# Create your models here.
class UserInfo(models.Model):
    '''创建数据表类'''
    # 用户列，数据类型，长度
    #id列，自动创建
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=16, null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True,null=True)
    update_time = models.DateTimeField(auto_now=True,null=True)

    user_type_choices = (
        (1,'管理员'),
        (2,'超级用户'),
        (3,'普通用户'),
        (4,'游客'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)
    user_group = models.ForeignKey('UserGroup',to_field='uid',default=1,on_delete=models.CASCADE)


class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,db_column='用户组',null=True)
    create_time = models.DateTimeField(auto_now_add=True,null=True)
    update_time = models.DateTimeField(auto_now=True,null=True)
