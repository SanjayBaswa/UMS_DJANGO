import pandas as pd
from django.shortcuts import render

from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from io import TextIOWrapper
import csv
import pandas


@api_view(['GET', 'POST'])
def recv_data(request):
    print(request.data)
    return JsonResponse(request.data, safe=False)


@api_view(['POST'])
def fetch_file(request, ewon_ip , file_path):
    if request == 'POST':
        print(ewon_ip)
        print(request.data())

        #thrw ftp get data



    return JsonResponse({ewon_ip:file_path}, safe=False)

# @api_view(['POST'])
# def fetch_file(request):
#     my_parameter = 'NOT RUN'
#     if request.method == 'POST':
#         print("Received POST data:", request.POST)
#         my_parameter = request.POST.get('helo')
#         print(my_parameter)
#     return HttpResponse(f"You submitted: {my_parameter}")
#     # return JsonResponse({"hi":"hii"}, safe=False)


@api_view(['GET', 'POST'])
def read_csv(request):
    csv_file = request.FILES.get('fisier')

    if not csv_file:
        return JsonResponse({'error': 'No file uploaded'}, status=400)

    # Assuming the CSV file has two columns: 'column1' and 'column2'
    csv_columns = ['Name', 'Average_Voltage', 'Trip_Command', 'Average_Current', 'Difference_Unit-Consumed',
                   'Frequency', 'KWH', 'Power_Factor', 'Active_Power', 'Reactive_Power', 'VH', 'ACB_ON', 'Department',
                   'timestamp', 'UID', 'Apparent_Power']
    # Decode the CSV file and read its content
    csv_data = []
    try:
        csv_file_wrapper = TextIOWrapper(csv_file.file, encoding='utf-8')
        csv_reader = csv.reader(csv_file_wrapper)
        next(csv_reader, None)
        for row in csv_reader:
            row_data = dict(zip(csv_columns, row))
            csv_data.append(row_data)

    except csv.Error as e:
        return JsonResponse({'error': f'Error reading CSV file: {e}'}, status=500)
    return JsonResponse({'success': True, 'data': csv_data}, status=200)
