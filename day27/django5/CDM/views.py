from django.shortcuts import render,redirect,HttpResponse
from django.db import models
from CDM import models
from django import forms
from django.forms import fields,widgets

import json
# Create your views here.
response = {'statue':True,'error':None,'data':None}

#############COOKIE认证#############
'''
def auth(func):
    # 认证装饰器
    def wrapper(request,*args,**kwargs):
        v = request.COOKIES.get('user')
        if not v:
            return redirect('/python/login/')
        else:
            return func(request,*args,**kwargs)
    return wrapper
'''
##########################

def auth(func):
    def wrapper(request,*args,**kwargs):
        if request.session.get('is_login',None):
            # u = request.session.get('username',None)
            return func(request, *args, **kwargs)
        else:
            return redirect('/python/login/')
    return wrapper
'''
def login(request):
    """登录界面"""
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        v = request.POST.get('VerfCode')
        auth = models.Admin.objects.filter(name=u,password=p).first()
        print(auth)
        # if u == 'root' and p == '123':
        if auth:
            print(u,p)
            # response['data']={'user':u,'pwd':p}
            # return HttpResponse(json.dumps(response))
            res = redirect('/python/home/')
            res.set_cookie('user',u,max_age=120)

            return res
        else:
                # response['statue'] = False
                response['error'] = '用户名错误'
                # return HttpResponse(json.dumps(response))
                return render(request,'login.html',{'response':response})
    else:
        return redirect('/python/login/')
'''

def login(request):
    '''登录界面'''
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        v = request.POST.get('VerfCode')
        auth = models.Admin.objects.filter(name=u,password=p).first()
        # print(auth)
        # if u == 'root' and p == '123':
        if auth:
            request.session['username'] = u
            request.session['is_login'] = True
            if request.POST.get('free-login',None) == '1':
                request.session.set_expiry(value=10)
            # return render(request,'home.html')
            return redirect('/python/home/')
        else:
                # response['statue'] = False
                response['error'] = '用户名错误'
                # return HttpResponse(json.dumps(response))
                return render(request,'login.html',{'response':response})
    else:
        return redirect('/python/login/')

def logout(request):
    '''退出界面'''
    request.session.clear()
    return redirect('/python/login/')

'''Ajax认证'''
# def login_verfy(request):
#     user_dict={}
#     if request.method == 'POST':
#         user_dict['user'] = request.POST.get('user')
#         user_dict['pwd'] = request.POST.get('pwd')
#         return HttpResponse(json.dumps(user_dict))

@auth
def home(request):
    '''主界面'''
    # u = request.COOKIES.get('user')
    u = request.session.get('username', None)
    if not u:
        # u = request.POST.get('user')
        return redirect('/python/login/')
    else:
        group_list = models.Usergroup.objects.all()
        group_obj = GroupFM()
        return render(request, 'home.html', {'user': u,'group_list':group_list,'group_obj':group_obj})

def users(request):
    '''用户主机页面'''
    pass

class GroupFM(forms.Form):
    '''添加用户组，并验证'''
    group_name = fields.CharField(
        max_length=6,
        error_messages={"max_length":"名字不能超过6个字符",
                        'required':'名字不能为空'},
        label='用户组名：'
    )

@auth
def groups(request,nid):
    '''用户组，主机组页面'''
    u = request.session.get('username',None)
    user_obj = models.User.objects.filter(user_to_group_id=nid)

    return render(request,'group_info.html',{'user_obj':user_obj,'user':u})



def add_group(request):
    '''添加用户组'''
    if request.method == 'POST':
        group_obj = GroupFM(request.POST)

        if group_obj.is_valid():
            new_group = group_obj.cleaned_data
            if not models.Usergroup.objects.filter(group_name=new_group['group_name']):
                models.Usergroup.objects.create(**new_group)
            return HttpResponse('OK')



def add_user(request):
    '''添加用户'''
    ret = {'status': True, 'error': None, 'data': None}
    try:
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        g = request.POST.get('group_id')
        if u and len(u) > 4:
            models.User.objects.create(user_name=u, password=p, user_to_group_id=g)
        else:
            ret['status'] = False
            ret['error'] = '输入格式不对'
    except Exception as e:
        ret['status'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret))

class FM(forms.Form):
    '''Form表单数据验证，生成HTML'''
    usser_groups = models.Usergroup.objects.all().values_list()
    user_name = forms.CharField(max_length=16,
                           error_messages={
                               'required':'用户名不能为空',
                               'max_length':'最多16个字符',
                           },
                           label='用户名：')
    password = forms.CharField(max_length=16,min_length=6,
                          error_messages={
                                'required':'密码不能为空',
                                'max_length':'最多16个字符',
                                'min_length':'最少6个字符',
                          },
                          widget= widgets.PasswordInput(),
                          label='密码：')
    user_to_group = forms.ChoiceField(
        label='用户组：',
        choices= usser_groups,
    )

def edit_user(request,nid):
    '''修改用户'''
    if request.method == 'GET':
        user_info = models.User.objects.filter(id=nid).first()
        user_dict = {'user_name':user_info.user_name,
                     'password':user_info.password,
                     'user_to_group':user_info.user_to_group.id}
        user_obj = FM(initial=user_dict)

        # user_info = models.User.objects.filter(id=nid).first()
        # group_Name = user_info.user_to_group.group_name
        return render(request,'edit_user.html',{"user_obj":user_obj,"user_info":user_info})
    elif request.method == 'POST':
        user_obj = FM(request.POST)
        r = user_obj.is_valid()
        print(r)
        if user_obj.is_valid():
            user_update = user_obj.cleaned_data
            models.User.objects.filter(id=nid).update(**user_update)     #form表单数据些写入数据库
            return redirect('/python/groups-%s'%nid)
        else:
            print(user_obj.errors.as_json())
        return render(request,"edit_user.html",{"user_obj":user_obj})

def del_user(request):
    '''删处用户'''
    nid = request.POST.get('id',None)
    models.User.objects.filter(id=nid).delete()
    return HttpResponse("OK")