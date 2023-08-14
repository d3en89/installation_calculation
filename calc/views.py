from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, request
from django.views.generic import CreateView


from calc.static.script.get_data_db import get_price
from calc.static.script import get_data_file

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the calc index.")
    list_price = {
        'all_works' : get_price()
    }
    # if request.method == 'POST' and request.FILES:
    #     print(request.FILES)
    #     file = request.FILES['price_file']
    #     fs = FileSystemStorage()
    #     filename = fs.save(file.name, file)
    #     file_path = fs.url(filename)
    #     return render(request, 'calc/index.html', list_price)

    if request.method == 'POST' and request.POST['Update']:
        get_data_file.main()
    return render(request, 'calc/index.html', list_price)


##### TEST ZONE ######

# list_price = {
#     'all_works' : get_price()
# }

#print(list_price['all_works'])