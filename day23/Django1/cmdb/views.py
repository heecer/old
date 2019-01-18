from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import random
USER_LIST = []
for i in range(10):
    temp = {'user':'python'+str(i),
            'gender':random.choice(['男','女']),
            # 'gender':'男',
            'email':'python'+str(i)+'@admin.com'}
    USER_LIST.append(temp)
def login(request):
    # f = open('templates/login.html','r',encoding='utf-8')
    # data = f.read()
    # f.close()
    error_msg = ''
    print(request.method)
    if request.method == 'POST':
        # user = request.POST['user']
        # pwd = request.POST['pwd']
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        print(user,pwd)
        if user == 'root' and pwd == '1234':
            return redirect('/home')
        else:
            error_msg = '用户名或密码错误'
    return render(request,'login.html',{'error_msg':error_msg})
    # data = render(request,'login.html')
    # return HttpResponse(data)
def home(request):
    if request.method == 'POST':
        u = request.POST.get('username',None)
        g = request.POST.get('gender',None)
        e = request.POST.get('email',None)
        temp_dic ={'user':u,'gender':g,'email':e}
        USER_LIST.append(temp_dic)
    return render(request,'home.html',{'user_list':USER_LIST})

def index(request):
    pass
    # return render(request,'index.html')