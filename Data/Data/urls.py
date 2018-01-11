"""Data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from webapp import views  as view

urlpatterns = {
    url('admin/', admin.site.urls),
    url("index", view.index),
    url("regist", view.regist),
    url("loading", view.loading),
    url("topbar",view.topbar),
    url("userInfo",view.userInfo),
    url("goods",view.goods),
    url("info",view.info),
    url("quite",view.quite),
    # url("e")
    # url("gs",view.goods),
    # url("gb", view.gb),
    # url("tim",view.tim),
    url("eval",view.eval),
    url(r"^$",view.index),
    url("detail",view.infodetail),
    url("t",view.t)

    # url("reg",view.reg),
    # url("oop",view.load2),

}
