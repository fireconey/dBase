from django.shortcuts import render
from django.http import HttpResponse
from webapp import models as model
from django.http import HttpResponseRedirect
from .forms import Loading as ldform
# Create your views here.
def index(request):
    #user.objects.create(usr="th",passwd="123",sex="男",
     #                   birth="19890615",email="1132224184@qq.com")
    return  render(request,"index.html",context={"th":11,"tu":34})

def  regist(request):
    return  render(request,"pages/regist.html")

def  loading(request):
    if request.method=="POST":
        obj=ldform(request.POST)
        if obj.is_valid():
            data=obj.clean()
            return  HttpResponseRedirect("index")
        else:
            return render(request,"pages/loading.html",
                          {"obj":obj,"p":request.POST})
    else:
        obj=ldform()
        return  render(request,"pages/loading.html",{"obj":obj})

def di(request):
    return  render(request,"pages/ldinfo.html")

def datainfo(request):
    return  render(request,"pages/datainfo.html")

def goods(request):
    return  render(request,"pages/goods.html")

def gb(request):
    return  render(request,"pages/goodsbackstage.html")

def tim(request):
    return render(request,"pages/timenews.html")

def eval(request):
    return render(request,"pages/eval.html")
def reg(request):
    return  render(request,"pages/reg.html")

def load2(request):
    usr=request.POST["usr"]
    passwd=request.POST["passwd"]
    db_usr="empty"
    try:
      db_usr=model.WebappUsr.objects.get(usr=str(usr))
    except:
        print("有异常")
    if db_usr=="empty":
        return render(request, "pages/test.html", {"usr":"cuwo"})
    return HttpResponseRedirect("/index")