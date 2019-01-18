from django.shortcuts import render,redirect,HttpResponse
from app001 import models
import json
# Create your views here.


def business(request):
    if request.method == 'GET':
        groups = models.Business.objects.all()
        groups_dict = models.Business.objects.all().values('id','group','code')
        groups_tuple = models.Business.objects.all().values_list('id','group','code')
        return render(request,'business.html',{ 'groups':groups,'groups_dict':groups_dict,'groups_tuple':groups_tuple})
    elif request.method == 'POST':
        g = request.POST.get('group_id')
        models.Business.objects.create(group=g)
        return redirect('/business/')

def host(request):
    if request.method == 'GET':
        hosts = models.Host.objects.all()
        host_dict = models.Host.objects.filter(nid__gt=0).values()
        host_tuple = models.Host.objects.filter(nid__gt=0).values_list()
        group_name = models.Host.objects.all().values('nid','hostname','ip','port','host_group_id','host_group__group')
        groups = models.Business.objects.all()
        return render(request,'host.html',{'hosts':hosts,'host_dict':host_dict,'host_tuple':host_tuple,'groups':groups,'group_name':group_name})
    elif request.method == 'POST':
        h = request.POST.get('hostname')
        p = request.POST.get('port')
        ip = request.POST.get('ip')
        g = request.POST.get('group_id')
        models.Host.objects.create(hostname=h,port=p,ip=ip,host_group_id=g)
        return redirect('/host/')

def add_ajax(request):
    import json
    ret = {'status':True,'error':None,'data':None}
    try:
        h = request.POST.get('hostname')
        p = request.POST.get('port')
        ip = request.POST.get('ip')
        g = request.POST.get('group_id')
        print(request.method,h,ip,p,g,sep='\t')
        if h and len(h) > 4:
            models.Host.objects.create(hostname=h, port=p, ip=ip, host_group_id=g)
        else:
            ret['status'] = False
            ret['error'] = '输入格式不对'
    except Exception as e:
        ret['status'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret))

def edit_ajax(request):

    ret = {'status':True,'error':None,'data':None}
    try:
        nid =request.POST.get('host_id')
        h = request.POST.get('hostname')
        p = request.POST.get('port')
        ip = request.POST.get('ip')
        g = request.POST.get('group_id')
        if h and len(h) > 4:
            models.Host.objects.filter(nid=nid).update(hostname=h, port=p, ip=ip, host_group_id=g)
        else:
            ret['status'] = False
            ret['error'] = '输入格式不对'
    except Exception as e:
        ret['status'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret))

def delet_ajax(request):
    host_id = request.POST.get('host_id')
    models.Host.objects.filter(nid=host_id).delete()
    return HttpResponse('OK')

def app(request):
    if request.method == 'GET':
        apps = models.Application.objects.all()
        hosts = models.Host.objects.all()
        return render(request,'app.html',{'apps':apps,'hosts':hosts})
    elif request.method == 'POST':
        appname =  request.POST.get('appname')
        host_id =  request.POST.getlist('host_list')

        # obj = models.Application.objects.create(name=appname)
        # obj.r.add(*host_id)
        return redirect('/app/')

def ajax_add_app(request):
    ret = {"status": True, "error": None, "data": None}
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('pwd'))
        # print(request.POST.getlist('host_list'))
    return HttpResponse(json.dumps(ret))