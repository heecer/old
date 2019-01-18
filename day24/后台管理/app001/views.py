from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def join(request):
    error = '123'
    if request.method == 'post':
        user = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if user == 'root' and  pwd == '123':
            print(user,pwd)
            return redirect('http://www.baidu.com')
        else:
            error =  '用户名或密码错误'
    return render(request, 'join.html', {'error':error})

def admin(request):
    return HttpResponse("<h1 style='background-color: blue;text-align: center;color: white;'>欢迎进入Django WEB</h1>")