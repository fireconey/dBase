from django.db import models

# Create your models here.
class user(models.Model):
    id=models.AutoField(primary_key=True)
    usr=models.CharField(max_length=30,null=False,unique=True)
    passwd=models.CharField(max_length=30,null=False)
    sex=models.CharField(max_length=10,null=False)
    birth=models.CharField(max_length=30,null=False)
    email=models.CharField(max_length=30,null=False)
    phone=models.CharField(max_length=30)


