from django import forms
from webapp.models import WebappUsr as umodel
from django.forms import ValidationError


def usrValidate(value):
    data_usr=0
    try:
        data_usr=umodel.objects.get(usr=value)
    except:
        data_usr=0
    if data_usr==0:
        raise ValidationError("用户名错误")

def passwdValidate(value):
    data_passwd=0
    try:
        data_passwd=umodel.objects.get(passwd=value)
    except:
        data_passwd=0
    if data_passwd==0:
        raise  ValidationError("密码错误")

class Loading(forms.Form):
    usr=forms.CharField(max_length=10,
                        validators=[usrValidate],
                        error_messages={"required":"用户名不能为空"})
    passwd=forms.CharField(max_length=20,
                           validators=[passwdValidate],
                           error_messages={"required":"密码不能为空"})







