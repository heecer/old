from django.shortcuts import render, redirect, HttpResponse
from HOME import models
from django.forms import Form,ModelForm,fields, widgets

from io import BytesIO
from MyBlog.check_code import create_validate_code
# Create your views here.

class RegisterModelForm(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ('nikename','username','password','email','phonenumber',)
        error_messages ={
            "__all__":{}
        }

# class LoginForm(Form):
#     '''登录表单'''
#     # 用户标签
#     name = fields.CharField(label='用户名',
#                             max_length=32,
#                             widget=widgets.Input(attrs={'class': 'user'}),
#                             error_messages={'required': '用户名不能为空',
#                                             'max_length': '不能超过32个字符'})
#     # 密码标签
#     password = fields.CharField(label='密码',
#                                 max_length=16,
#                                 min_length=6,
#                                 widget=widgets.PasswordInput(attrs={'class': 'pwd'}),
#                                 error_messages={'required': '密码不能为空',
#                                                 'min_length': '不能小于6个字符',
#                                                 'max_length': '不能大于16个字符', })
#     # 邮箱标签
#     email = fields.EmailField(label='邮箱',
#                               error_messages={'required': '邮箱不能为空',
#                                               'code': '邮箱格式不对'})
    # 验证码标签
    # code = fields.ChoiceField(label='验证码',
    #                           choices=models.App.objects.values_list('id','user_app'))
    # def __init__(self,*args, **kwargs):
    #     '''自动更新加载'''
    #     super(LoginForm,self).__init__(*args, **kwargs)
    #     self.fields['code'].choices = models.App.objects.values_list('id','app_name')




def index(requset):
    return render(requset, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        code = request.POST.get('check_code')
        auth = models.UserInfo.objects.filter(username=u, password=p).first()

        if code.upper() == request.session['CheckCode'].upper():
            nikename = auth.nikename
            if auth:
                request.session['auth'] = nikename
                return redirect('/article/0-0.html')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method =='GET':
        MF = RegisterModelForm()
        return render(request, 'register.html',{'modelform':MF})
    elif request.method =='POST':
        MF = RegisterModelForm(request.POST)
        if MF.is_valid():
            MF.save()
            return redirect('/login.html')
        else:
            return render(request, 'register.html', {'modelform': MF})


def check_code(request):
    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream, format='PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())

def logout(request):
    request.session.clear()
    return redirect('/login.html')


def article(request, *args, **kwargs):
    '''筛选文章'''
    condition ={}
    for k,v in kwargs.items():
        kwargs[k] = int(v)
        if v == '0':
            pass
        else:
            condition[k] = v
    article_type = models.ArticleType.objects.all()     #所有的文章类型对象
    categorys = models.Category.objects.all()       #所有的分类对象
    # articles = models.Article.objects.all()
    # articles = models.Article.objects.filter(articletype_id=1,category=1)
    articles = models.Article.objects.filter(**condition)  #类型+分类，筛选文章

    return render(request, 'article.html',
                  {'articles':articles,
                   'article_type':article_type,
                   'categorys':categorys,
                   'arg_dict': kwargs,
                   })

import requests
def weather(request):
    weather_response = requests.get('http://www.weather.com.cn/data/sk/101040100.html')
    weather_response.encoding ='utf-8'
    return render(request,'weather.html',{'weather_response':weather_response.text})


def jsonp(request):
    return render(request, 'jsonp.html')