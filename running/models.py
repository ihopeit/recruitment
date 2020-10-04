# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    areaid = models.AutoField(primary_key=True)
    countryid = models.PositiveIntegerField()
    chn_name = models.CharField(max_length=64)
    eng_name = models.CharField(max_length=64, blank=True, null=True)
    sort = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'area'



class Country(models.Model):
    countryid = models.AutoField(primary_key=True)
    chn_name = models.CharField(max_length=64)
    eng_name = models.CharField(max_length=64, blank=True, null=True)
    country_logo = models.CharField(max_length=120, blank=True, null=True)
    sort = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'country'


    def __str__(self):
        return self.chn_name if self.chn_name else ""


class Province(models.Model):
    provinceid = models.AutoField(primary_key=True)
    countryid = models.ForeignKey(Country, db_column='countryid', null=True, on_delete=models.SET_NULL)
    areaid = models.PositiveIntegerField(blank=True, null=True)
    chn_name = models.CharField(max_length=64)
    eng_name = models.CharField(max_length=64, blank=True, null=True)
    sort = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'province'

    def __str__(self):
        return self.chn_name if self.chn_name else ""

from smart_selects.db_fields import ChainedForeignKey


class City(models.Model):
    cityid = models.AutoField(primary_key=True)
    countryid = models.ForeignKey(Country, db_column='countryid', null=True, on_delete=models.SET_NULL)
    areaid = models.PositiveIntegerField(blank=True, null=True)
    provinceid = models.ForeignKey(Province, db_column='provinceid', null=True, on_delete=models.SET_NULL)

    chn_name = models.CharField(max_length=64)
    eng_name = models.CharField(max_length=64, blank=True, null=True)
    sort = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'city'

    def __str__(self):
        return self.chn_name if self.chn_name else self.eng_name if self.eng_name else ""