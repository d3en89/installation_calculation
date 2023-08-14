from django.db import models
from core.settings import MEDIA_ROOT
# Create your models here.

class Data_inner(models.Model):
    id = models.AutoField(verbose_name='id', auto_created=True, primary_key=True)
    index_sheet = models.IntegerField(verbose_name='Индекс')
    name_of_works = models.CharField(max_length=200, verbose_name='Название работ')
    quantity = models.IntegerField(verbose_name='Количество', default=1)
    uom = models.CharField(max_length=10, verbose_name='Ед. измерения', default='шт')
    cost = models.IntegerField(verbose_name='Цена')
    curency = models.CharField(max_length=5, verbose_name='Валюта', default='руб')


class Data_innet_hash(models.Model):
    id = models.AutoField(verbose_name='id', auto_created=True, primary_key=True)
    price_hash = models.CharField(max_length=200, verbose_name='Hash')

class File_upload(models.Model):
    name = models.CharField(max_length=10)
    file_point = models.FileField(upload_to=MEDIA_ROOT)

