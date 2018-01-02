# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class WebappCt(models.Model):
    id_field = models.IntegerField(db_column='id ', primary_key=True, blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    usr = models.ForeignKey('WebappUsr', models.DO_NOTHING, db_column='usr')
    ct = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'webapp_ct'


class WebappGrp(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    usr = models.ForeignKey('WebappUsr', models.DO_NOTHING, db_column='usr')
    grp = models.CharField(max_length=8)
    loc = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'webapp_grp'


class WebappImg(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    usr = models.ForeignKey('WebappUsr', models.DO_NOTHING, db_column='usr')
    img = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = False
        db_table = 'webapp_img'
# Unable to inspect table 'webapp_infolead'
# The error was: list index out of range


class WebappLoc(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    sheng = models.CharField(max_length=8, blank=True, null=True)
    shi = models.CharField(max_length=8)
    xiang = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'webapp_loc'


class WebappUsr(models.Model):
    id = models.IntegerField(primary_key=True)
    usr = models.CharField(unique=True, max_length=30)
    passwd = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    birth = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    loc = models.TextField()  # This field type is a guess.
    infold = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'webapp_usr'
