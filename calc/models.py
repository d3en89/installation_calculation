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


class File_upload(models.Model):
    #id = models.AutoField(verbose_name='id', auto_created=True, primary_key=True)
    name = models.CharField(max_length=100, default="price.xlsx")
    file_point = models.FileField(upload_to='/tmp/')

