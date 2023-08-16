from django.shortcuts import render
from django.http import HttpResponse, request, HttpRequest
from core.settings import MEDIA_ROOT

from calc.static.script.get_data_db import get_price
from calc.static.script import get_data_file
from calc.models import File_upload

# Create your views here.

def index(request : HttpRequest):
    #return HttpResponse("Hello, world. You're at the calc index.")
    list_price = {
        'all_works' : get_price()
    }
    match request.POST:
        case {'Send': 'Отправить'}:
            file = File_upload(name=str(request.FILES.get('send_files')),
                               file_point=request.FILES.get('send_files'))
            if file.name == "None":
                return render(request, 'calc/index.html', list_price)
            else:
                file.save()
                get_data_file.main(MEDIA_ROOT, str(file.file_point))

    return render(request, 'calc/index.html', list_price)
