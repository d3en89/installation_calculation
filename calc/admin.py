from django.contrib import admin
from .models import Data_inner, File_upload

# Register your models here.
#admin.site.regsiter(Data_inner)

class DataInnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'index_sheet', 'name_of_works', 'quantity', 'uom', 'cost', 'curency']

class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file_point']

admin.site.register(Data_inner, DataInnerAdmin)
admin.site.register(File_upload, FileAdmin)