from django.shortcuts import render
from django.http import HttpResponse
from calc.static.script.get_data_db import get_price

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the calc index.")
    list_price = {
        'all_works' : get_price()
    }
    return render(request, 'calc/index.html', list_price)


##### TEST ZONE ######

# list_price = {
#     'all_works' : get_price()
# }

#print(list_price['all_works'])