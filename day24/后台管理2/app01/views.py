from django.shortcuts import render,redirect,HttpResponse
import os
from app01 import models
# Create your views here.

def login(request):
    error = ''
    if request.method ==('GET'):
        return render(request,'login.html')
    elif request.method == 'POST':
        user = request.POST.get('username', None)
        pwd = request.POST.get('pwd', None)
        # print(user, pwd)
        result = models.UserInfo.objects.filter(username=user,password=pwd).first()
        # print(result)
        if result:
           return render(request,'index.html',{'user':user})
        else:
            error = '用户名或密码错误'
            return render(request, 'login.html', {'error': error})
    else:
        return render(request,'login.html')

def ORM(request):
    '''方式一'''
    # models.UserInfo.objects.create(
    #     username='root',password='123',)
    '''方式二'''
    # obj = models.UserInfo(username='admin',password='1234')
    # obj.save()
    '''方式三'''
    # dict = {'username':'python','password':'python123'}
    # models.UserInfo.objects.create(**dict)
    # result = models.UserInfo.objects.all()
    # a = []
    # for row in result:
    #     a.append(str(row.id )+ row.username +row.password+'<br>')
    # result1 = models.UserInfo.objects.filter(username='root',password='123')
    # print(result1)
    # return HttpResponse(a)
    # models.UserInfo.objects.filter(id=3).delete()
    # models.UserInfo.objects.filter(username='ddd').delete()
    # models.UserInfo.objects.create(username='java',password='java123',user_group=models.UserGroup.objects.filter(uid=1).first())
    models.UserInfo.objects.create(username='java',password='java123',user_group_id=1)
    return HttpResponse('OK')

def index(request):
    # models.UserGroup.objects.filter(caption='四川').update(caption='重庆')
    # user = request.GET.get('username')
    return render(request,'index.html')

def user(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        group_list =models.UserGroup.objects.all()
        return render(request,'user.html',{'user_list':user_list,'group_list':group_list})
    elif request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        models.UserInfo.objects.create(username=u,password=p)
        # user_list = models.UserInfo.objects.all()
        # return render(request,'user.html',{'user_list':user_list})
        return redirect('/app01/user/')

def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request,'user_detail.html',{'user_detail':obj})

def userdel(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/app01/useredit/')


def useredit(request,nid):
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        groups = models.UserGroup.objects.all()
        return render(request,'useredit.html',{'user_list':obj,'groups':groups})
    elif request.method == 'POST':
        id = request.POST.get('id',None)
        u = request.POST.get('username',None)
        p = request.POST.get('pwd',None)
        g = request.POST.get('group')
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p,user_group_id=g)
        return redirect('/app01/user/')
def groups(request):
    if request.method == 'GET':
        group_list = models.UserGroup.objects.all()
        return render(request,'groups.html',{'group_list':group_list})
    elif request.method == 'POST':
        g = request.POST.get('group')
        models.UserGroup.objects.create(caption=g)
        return redirect('/app01/groups/')


def groupdel(request,nid):
    models.UserGroup.objects.filter(uid=nid).delete()
    return redirect('/app01/groups/')