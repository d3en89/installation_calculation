from django.contrib import admin
from .models import Data_inner

# Register your models here.
#admin.site.regsiter(Data_inner)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'index_sheet', 'name_of_works', 'quantity', 'uom', 'cost', 'curency']

admin.site.register(Data_inner, ProductAdmin)