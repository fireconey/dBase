from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import user
# Create your views here.
def index(request):
    #user.objects.create(usr="th",passwd="123",sex="男",
     #                   birth="19890615",email="1132224184@qq.com")
    return  render(request,"index.html",context={"th":11,"tu":34})

def  regist(request):
    return  render(request,"pages/regist.html")

def  ld(request):
    return  render(request,"pages/loading.html")

def ldinfo(request):
    return  render(request,"pages/ldinfo.html")

def datainfo(request):
    return  render(request,"pages/datainfo.html")
