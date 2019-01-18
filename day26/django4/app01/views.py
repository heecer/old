from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django import views
from django.utils.decorators import method_decorator

from utils import pagination
# Create your views here.

def index(request):
    # print(NAME)
    # r = reverse('root')
    r = reverse('author:index')
    # return HttpResponse('<h1>%s--->%s</h1>'%(name,r))
    print(request.environ)
    for k,v in request.environ.items():
        print(k,v)
    return HttpResponse('<h1>--->%s</h1>'%(r))


def template(request):
    request_dict = request.environ
    return render(request,'template.html',{'request_dict':request_dict})

def test1(request):
    request_dict = request.environ
    return render(request,'test1.html',{'request_dict':request_dict})

def test2(request):
    user_list = [i for i in range(5)]
    return render(request,'test2.html',{'user_list':user_list})

user_list = [i for i in range(2000)]
data_count = len(user_list)

def test3(request):
    user_str = 'AsfwaeGewrvGGHJJJ'
    page_str = '''
        <div>
            <a href="/a/test3/?p=1">1</a>
            <a href="/a/test3/?p=2">2</a>
            <a href="/a/test3/?p=3">3</a>
        </div>'''
    pages = mark_safe(page_str)

    current_page = int(request.GET.get('p', 1))
    current_cookie = request.COOKIES.get('per-page-size')

    '''********************************************'''
    '''********************************************'''
    # page_num = 11
    # data_num = 10
    # start = (current_page-1) * data_num
    # end = current_page * data_num


    # count, remainder = divmod(data_count, data_num)
    # if remainder:
    #     count += 1
    # if count < page_num:
    #     start_page = 1
    #     end_page = count + 1
    # else:
    #     if current_page <= (page_num+1)/2:
    #         start_page = 1
    #         end_page = page_num
    #     else:
    #         start_page = current_page - (page_num-1)/2
    #         end_page = current_page + (page_num+1)/2
    #         if (current_page + (page_num-1)/2) > count:
    #             start_page = count - page_num +1
    #             end_page = count + 1
    # page_list = []
    # if current_page ==1:
    #    prev = '<a class="page" href="javascript:void(0);">上一页</a>'
    # else:
    #     prev = '<a class="page" href="/a/test3/?p=%s">上一页</a>' % (current_page-1)
    # page_list.append(prev)
    # for i in range(int(start_page), int(end_page)):
    #     if i == current_page:
    #         temp = '<a class="page active" href="/a/test3/?p=%s">%s</a>' % (i, i)
    #     else:
    #         temp = '<a class="page" href="/a/test3/?p=%s">%s</a>' % (i, i)
    #     page_list.append(temp)
    # if current_page == count:
    #     Next = '<a class="page" href="javascript:void(0);">下一页</a>'
    # else:
    #     Next = '<a class="page" href="/a/test3/?p=%s">下一页</a>' % (current_page+1)
    # page_list.append(Next)
    #
    # jump = '''
    # <input type="text" />
    # <a onclick="jumpTo(this,'/a/test3/?p=');" id="i1">跳转</a>
    # '''
    # page_list.append(jump)
    # pages_str =mark_safe(''.join(page_list))
    '''********************************************'''
    '''********************************************'''
    print(current_cookie)
    per_page_data = int(current_cookie)
    page_obj = pagination.Page(current_page, data_count,per_page_data)
    data = user_list[page_obj.start:page_obj.end]
    pages_str = page_obj.page_str('/a/test3/')
    return render(request,'test3.html',{'user_str':user_str,'data':data,
                                        'pages_str':pages_str})

user_dict = {'root':{'pwd':'123'},
             'guest': {'pwd': 'abc'},}

def auth(func):
    def wrapper(request,*args,**kwargs):
        v = request.COOKIES.get('cookiename')
        if not v:
            return redirect('/a/login/')
        return func(request,*args,**kwargs)
    return wrapper


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        user = user_dict.get(u)
        if not user:
            return render(request,'login.html')
        if p == user['pwd']:
            res = redirect('/a/home/')
            res.set_cookie('cookiename',u,max_age=10,path='/')

            '''********************************************'''
            '''********************************************'''
            # import datetime
            # current_date = datetime.datetime.utcnow()    #当前时间
            # current_date += datetime.timedelta(seconds=5)   #当前时间延迟5秒
            # res.set_cookie('cookiename', u, expires=current_date)
            '''********************************************'''
            '''********************************************'''

            return res
        else:
            return render(request,'login.html')
@auth
def home(request):
    u = request.COOKIES.get('cookiename',)
    if not u:
        return redirect('/a/login')
    else:
        return render(request,'home.html',{'username':u})



@method_decorator(auth,name='dispatch')
class Order(views.View):

    # @method_decorator(auth)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(Order,self).dispatch(request, *args, **kwargs)

    # @method_decorator(auth)
    def get(self,request):
        v = request.COOKIES.get('cookiename')
        if not v:
            return redirect('/a/login/')
        return render(request,'home.html',{'username':v})