from django.db import models
from django.db.models import Model
from django.forms import ModelForm

# Create your models here.

class UserInfo(Model):
    '''用户信息表
    @username: 用户名
    @password: 密码
    @email: 邮箱
    @phonenumber: 手机号码
    @nikename：昵称
    @avatar：头像
    @create_tiem：创建时间
    @update_time：更新时间
    '''

    nid = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    phonenumber = models.IntegerField(verbose_name='手机号码', unique=True)
    nikename = models.CharField(verbose_name='昵称', max_length=32)
    avatar = models.ImageField(verbose_name='头像')
    create_tiem = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

class Article(Model):
    '''文章表'''
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='博文标题', max_length=32)
    content = models.CharField(verbose_name='文章', max_length=200)
    # type_choices = [
    #     (0, 'Python'),
    #     (1, 'Java'),
    #     (2, 'HTML'),
    #     (3, 'CSS'),
    #     (4, 'Jquery'),
    #     (5, 'Jquery'),
    #     (6, 'others'),
    # ]
    # article_type = models.IntegerField(choices=type_choices, default=None)
    create_time = models.DateTimeField(verbose_name='新建时间', auto_now_add=True)
    edit_time = models.DateTimeField(verbose_name='编辑时间', auto_now=True)

    articletype = models.ForeignKey('ArticleType',on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Tag(Model):
    nid = models.AutoField(primary_key=True)
    tag = models.CharField(verbose_name='标签名称', max_length=32)

class Category(Model):
    '''分类表'''
    nid = models.AutoField(primary_key=True)
    category = models.CharField(verbose_name='分类',max_length=32)


class ArticleType(Model):
    nid = models.AutoField(primary_key=True)
    articletype = models.CharField(verbose_name='类型', max_length=32)

