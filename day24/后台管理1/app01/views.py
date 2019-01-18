from django.shortcuts import render
from app01 import views
# Create your views here.

def login(request):
    return render(request,'login.html')