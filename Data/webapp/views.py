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
utemp=0
def index(request):
    ob="登录"
    rg="注册"
    if flag==0:
        ob="登录"
    if flag==1:
        ob="退出"
        rg="已登录"

    return  render(request,"index.html",{"ob":ob,
                                         "rg":rg})


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
            print(umodle)
            initphoto=data["img"]
            model.WebappUsr(usr=data["usr"],
                            passwd=data["passwd"],
                            sex=data["sex"],
                            birth=data["birth"],
                            wx=data["wx"],
                            phone=data["phone"],
                            loc=data["loc"],
                            img=initphoto
                            ).save()

            return  HttpResponse("temp")
        elif usr["flag"]=="submit":
            for i in umodle.errors:
                dic[i]=umodle.errors.get(i)
            return HttpResponse(str(dic))

        if onlyu.is_valid() and usr["flag"]=="im":
            if not os.path.exists("webapp/static/"+usr["usr"]):
                os.mkdir("webapp/static/"+usr["usr"])
            with open("webapp/static/"+usr["usr"]+"/"+file["file"].name,"wb+") as f:
                for i in file["file"]:
                    f.write(i)
            return HttpResponse("static/"+usr["usr"]+"/"+file["file"].name)
        elif usr["flag"]=="im":
            for i in onlyu.errors:
                dic[i]=onlyu.errors.get(i)
            return  HttpResponse(str(dic))
        elif usr["flag"]=="cancel":
            import shutil
            shutil.rmtree("webapp/static/" + usr["ucancel"])
            return HttpResponse("ok")

    else:
        obj=form.Regist()
        return  render(request,"pages/regist.html",{"im":initphoto,
                                                    "obj":obj})








def  loading(request):
    global  flag,utemp
    t = True  #获取的密码是『请输入密码』的标记
    if request.method=="POST":
        r = request.POST

        #由于每次获取时都莫名其妙的有空格所以再
        #同时在html有的语句不支持如（strip）所以
        #处理好之后导入数据
        pw = r["passwd"].strip()
        u=r["usr"].strip()
        print(pw)
        #导入数据到表单中便于验证
        obj=ldform(r)

        #验证通过就到首页
        if obj.is_valid():
            data=obj.clean()
            flag=1
            utemp=u
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
        obj=ldform()
        return  render(request,"pages/loading.html",{"obj":obj,
                 "b":t,
                 "u":"请输入账号",
                 "pw":"请输入密码"})



def topbar(request):
    global flag
    print(flag)
    if flag==1 and request.method=="POST":
        data=request.POST
        mark=data["mark"].strip()
        if mark=="img":
            return  HttpResponseRedirect("userInfo")
        elif mark=="quite":
            flag=0
            return  HttpResponseRedirect("/index")
        return HttpResponseRedirect(mark)

    elif flag==0 and request.method=="POST":
        data=request.POST
        mark=data["mark"].strip()
        if mark=="img":
            return HttpResponseRedirect("index")
        return  HttpResponseRedirect(mark)


        # return  HttpResponseRedirect("index")
    else:
        return HttpResponseRedirect("/index")

def quite(request):
    global flag
    flag=0
    return  HttpResponseRedirect("/index")







def userInfo(request):
    global  utemp
    ob = "登录"
    rg = "注册"
    query=model.WebappUsr
    usr=""
    sex=""
    birth=""
    passwd=""
    wx=""
    phone=""
    loc=""
    img=""
    if flag == 1:
        ob = "退出"
        rg = "已登录"
    if request.method=="POST":
        print("yuyuy"+utemp)
        data=request.POST
        query(usr=data["usr"],
              sex=data["sex"],
              birth=data["birth"],
              passwd=data["passwd"],
              wx=data["wx"],
              phone=data["phone"],
              loc=data["loc"])
        query.save()
        utemp=data["usr"]

    try:
        query = query.objects.get(usr=utemp)
        usr = query.usr
        print(query.usr + "11")
        sex = query.sex
        if int(sex)==0:
            sex="男"
        elif int(sex)==1:
            sex="女"
        birth = query.birth
        passwd = query.passwd
        wx = query.wx
        phone = query.phone
        loc = query.loc
        img=query.img
    except:
        print("查询有错误")
    return  render(request,"pages/uinfo.html",
                   {"ob":ob,
                     "rg":rg,
                    "usr":usr,
                    "sex":sex,
                    "birth":birth,
                    "passwd":passwd,
                    "wx":wx,
                    "phone":phone,
                    "loc":loc,
                    "img":img
                   })



def goodsBackstage(request):
    ob="登录"
    rg = "注册"
    if flag==1:
        ob="退出"
        rg = "已登录"
    return  render(request,"pages/goodsbackstage.html",
                   {"ob":ob,
                     "rg":rg

                   })

def info(request):
    ob="登录"
    rg = "注册"
    if flag==1:
        ob="退出"
        rg = "已登录"
    return  render(request,"pages/info.html",
                   {"ob":ob,
                     "rg":rg

                   })

def timenews(request):
    ob="登录"
    rg = "注册"
    if flag==1:
        ob="退出"
        rg = "已登录"
    return  render(request,"pages/timenews.html",
                   {"ob":ob,
                     "rg":rg

                   })

def eval(request):
    ob="登录"
    rg = "注册"
    if flag==1:
        ob="退出"
        rg = "已登录"
    return  render(request,"pages/eval.html",
                   {"ob":ob,
                     "rg":rg

                   })
def goods(request):
    ob="登录"
    rg="注册"
    if flag==1:
        ob="退出"
        rg = "已登录"
    return  render(request,"pages/goods.html",{"ob":ob,
                                               "rg":rg})
