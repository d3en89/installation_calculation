from django.contrib import admin
from .models import Data_inner, Data_innet_hash

# Register your models here.
#admin.site.regsiter(Data_inner)

class DataInnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'index_sheet', 'name_of_works', 'quantity', 'uom', 'cost', 'curency']

class HashAdmin(admin.ModelAdmin):
    list_display = ['id', 'price_hash']

admin.site.register(Data_inner, DataInnerAdmin)
admin.site.register(Data_innet_hash, HashAdmin)