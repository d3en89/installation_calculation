from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from core.settings import MEDIA_ROOT, BASE_DIR
import mimetypes
from openpyxl import Workbook

from calc.static.script.get_data_db import get_price
from calc.static.script import get_data_file
from calc.models import File_upload


def index(request : HttpRequest):
    list_price = {
        'all_works' : get_price()
    }

    match request.POST:
        case {'Send': 'Отправить'}:

            """ This case search and check file to upload on server
                    """

            file = File_upload(name=str(request.FILES.get('send_files')),
                               file_point=request.FILES.get('send_files'))
            if file.name == "None":
                return render(request, 'calc/index.html', list_price)
            else:
                file.save()
                get_data_file.main(MEDIA_ROOT, str(file.file_point))

    return render(request, 'calc/index.html', list_price)

def download_file(request):

        """  Func generate template xlsx to download,
        when use button Скачать шаблон """

        filename = 'temp_price.xlsx'
        filepath = f'{BASE_DIR}/calc/static/template/{filename}'
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = 'Price'
        columns = [
            'Индекс',
            'Название работ',
            'Количество',
            'Ед. измерения',
            'Цена',
            'Валюта',
        ]
        row_num = 1

        for col_num, column_title in enumerate(columns, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title

        workbook.save(response)
        return response
