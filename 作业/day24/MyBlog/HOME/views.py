from django.shortcuts import render,HttpResponse,redirect
from HOME import models
# Create your views here.

def add_article(request):
    if request.method == 'GET':
        return render(request,'add_article.html')
    elif request.method == 'POST':
        obj = models.Article(request.POST)
        print(obj)
        return redirect('/article/0-0.html')
