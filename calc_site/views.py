from django.shortcuts import render
from django.http import HttpRequest
from calc_site.static.script.get_data_db import get_price
# Create your views here.


def index(request: HttpRequest):
        ### All Price
    list_price = {
        'all_works': get_price('all'),
        'all_works_short': get_price('all')[0:46],
        'inner': get_price('inner'),
        'out': get_price('out')
    }


    return render(request, 'calc_site/calc_index.html', list_price)



