# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class WebappImg(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.CharField(unique=True, max_length=8)
    usr = models.ForeignKey('WebappUsr', models.DO_NOTHING, db_column='usr')


class WebappLoc(models.Model):
    id = models.IntegerField(primary_key=True)
    sheng = models.CharField(max_length=8, blank=True, null=True)
    shi = models.CharField(max_length=8)
    xiang = models.CharField(max_length=8)

class WebappNews(models.Model):
    id = models.IntegerField(primary_key=True)
    usr = models.ForeignKey('WebappUsr', models.DO_NOTHING, db_column='usr')
    img = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    loc = models.CharField(max_length=30)
    flag = models.CharField(max_length=10)


class WebappShoping(models.Model):
    id = models.IntegerField(primary_key=True)
    usr = models.ForeignKey('WebappUsr', models.DO_NOTHING, db_column='usr')
    img = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    loc = models.CharField(max_length=30)
    flag=models.CharField(max_length=10)



class WebappUsr(models.Model):
    id = models.IntegerField(primary_key=True)
    usr = models.CharField(unique=True, max_length=30)
    passwd = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    birth = models.CharField(max_length=30)
    wx = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    loc = models.TextField()
    infold = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=30)

