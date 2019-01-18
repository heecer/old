from django.shortcuts import render,redirect,HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views import View
import os
# Create your views here.
USER_DICT = {
    '1':{'name':'python1','email':'python1@admin.com'},
    '2':{'name':'python2','email':'python2@admin.com'},
    '3':{'name':'python3','email':'python3@admin.com'},
    '4':{'name':'python4','email':'python4@admin.com'},
}

def login(request):
    error = ''
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('pwd',None)
        gender = request.POST.get('gender')
        favor = request.POST.getlist('favor')
        filename = request.POST.get('file')
        file_obj = request.FILES.get('file')

        print(user, pwd, gender, favor, type(file_obj))
        print(type(file_obj),file_obj.name)

        file_path = os.path.join('upload',file_obj.name)
        if user == 'root' and pwd == '123':
            f = open(file_path,'wb')
            for i in file_obj.chunks():
                f.write(i)
            f.close()
            return redirect('/login/')
        else:
            error = '用户名或密码错误'
    return render(request,'login.html',{'error':error})

def home(request):
    import random
    USER_INFO = []
    for i in range(5):
        temp = {'user':'aa'+str(i),'gender':random.choice(('男','女')),'email':'aa'+str(i)+'@admin.com'}
        USER_INFO.append(temp)
    if request.method == 'POST':
        u = request.POST.get('username',None)
        g = request.POST.get('gender',None)
        e = request.POST.get('email',None)
        temp = {'user':u,'gender':g,'email':e}
        USER_INFO.append(temp)
    return render(request,'home.html',{'user_list':USER_INFO})

class Index(View):
    '''Index继承父类View'''
    def dispatch(self, request, *args, **kwargs):
        print('之前')
        result = super(Index,self).dispatch(request, *args, **kwargs)
        print('之后')
        return result

    def get(self,request):
        print(request.method)
        return render(request,'index.html')

    def post(self, request):
        print(request.method)
        return render(request, 'index.html')

def User_Info(request):
    return render(request,'user_info.html',{'user_dict':USER_DICT})

def Detail(request,nid):
    # print(nid,uid)
    # return HttpResponse(uid)
    # nid = request.GET.get('nid')
    return render(request,'detail.html',{'user_detail':USER_DICT[nid]})

# def Index1(request,nid):
#     print(request.path_info)
#     return render(request,'index1.html')


def Index1(request,nid):
    from django.urls import reverse
    url1 = reverse('user_in',args=(15,))
    print(url1)
    return render(request,'index1.html')