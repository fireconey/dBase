from django.shortcuts import render
from django.http import  HttpResponse
from webapp import models as model
from django.http import HttpResponseRedirect
from .forms import Loading as ldform
from . import forms as form
from django.views.decorators.csrf import csrf_exempt
import os
import  threading
# Create your views here.
#登录检查标记
flag=0
def index(request):
    #user.objects.create(usr="th",passwd="123",sex="男",
     #                   birth="19890615",email="1132224184@qq.com")
    return  render(request,"index.html",context={"th":11,"tu":34})


@csrf_exempt
def  regist(request):
    global  flag
    print(flag)
    if flag==1:
        return HttpResponseRedirect("index")

    dic={}
    initphoto="../static/img/loading.jpg"
    if request.method=="POST":
        file=request.FILES
        usr=request.POST
        umodle=form.Regist(usr)
        onlyu=form.Usr(usr)
        if umodle.is_valid() and usr["flag"]=="submit":
            data=umodle.clean()
            try:
                initphoto="../static/img/"+file["file"].name
            except:
                initphoto="../static/img/loading.jpg"
            model.WebappUsr(usr=data["usr"],
                            passwd=data["passwd"],
                            sex=data["sex"],
                            birth=data["birth"],
                            wx=data["wx"],
                            phone=data["phone"],
                            loc=data["loc"],
                            img=initphoto
                            ).save()

            return  HttpResponse("null")
        elif usr["flag"]=="submit":
            for i in umodle.errors:
                dic[i]=umodle.errors.get(i)
            return HttpResponse(str(dic))

        if onlyu.is_valid() and usr["flag"]=="im":
            print(22)
            if not os.path.exists("webapp/static/"+usr["usr"]):
                os.mkdir("webapp/static/"+usr["usr"])
            with open("webapp/static/"+usr["usr"]+"/"+file["file"].name,"wb+") as f:
                for i in file["file"]:
                    f.write(i)
            return HttpResponse("static/"+usr["usr"]+"/"+file["file"].name)
        else:
            for i in onlyu.errors:
                dic[i]=onlyu.errors.get(i)
            return  HttpResponse(str(dic))
    else:
        obj=form.Regist()
        return  render(request,"pages/regist.html",{"im":initphoto,
                                                    "obj":obj})








def  loading(request):
    global  flag
    t = True  #获取的密码是『请输入密码』的标记
    if request.method=="POST":
        r = request.POST

        #由于每次获取时都莫名其妙的有空格所以再
        #同时在html有的语句不支持如（strip）所以
        #处理好之后导入数据
        pw = r["passwd"].strip()
        u=r["usr"].strip()

        #导入数据到表单中便于验证
        obj=ldform(request.POST)

        #验证通过就到首页
        if obj.is_valid():
            data=obj.clean()
            flag=1
            return  HttpResponseRedirect("/index")
        else:
            flag=0
            if pw!="请输入密码":
                t=False
            else:
                t=True
            return render(request,"pages/loading.html",
                  {"obj":obj,
                  "u":u,
                  "b":t,
                  "pw":pw})
    else:
        flag=0
        obj=ldform()
        return  render(request,"pages/loading.html",{"obj":obj,
                 "b":t,
                 "u":"请输入账号",
                 "pw":"请输入密码"})



def topbar(request):
    global flag
    if flag==1 and request.method=="POST":
        data=request.POST
        mark=data["mark"]
        if mark=="img":
            return  HttpResponseRedirect("userInfo")
        elif mark=="quite":
            flag=0
            return  HttpResponseRedirect("/index")
    else:
        print(222)
        return HttpResponseRedirect("/index")










def userInfo(request):
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




