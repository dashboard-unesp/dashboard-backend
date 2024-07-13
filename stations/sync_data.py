import fnmatch
import os
import shutil
from datetime import datetime

from django.conf import settings
from django.db import transaction
from django.db.models import Sum, Max, Avg, Min
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view

from stations.serializers import ClimateDataSerializer
from stations.models import ClimateData
from rest_framework.response import Response
from rest_framework import  status

@csrf_exempt
@require_http_methods(['GET'])
def sync_files(self):

    files_to_read = os.path.abspath(os.path.join(settings.BASE_DIR, '..' + "/PI_files/"))

    backup = files_to_read + "\BACKUP"

    error = files_to_read + "\ERROR"

    climate_data_list = []

    error_files = []

    files = fnmatch.filter(os.listdir(files_to_read), "*.dat")

    for file in files:

        with open(files_to_read + "/" + file, 'r', encoding='utf8') as arquivo:
            lines = arquivo.readlines()[4:]
            for line in lines:
                value = line.split(",")
                data_hora = value[0]
                data_hora_sem_aspas = data_hora.replace('"', '')
                formatted_date = datetime.strptime(data_hora_sem_aspas, '%Y-%m-%d %H:%M:%S')
                register_id = float(value[1])
                VelVent_ms = float(value[2])
                DirVent = float(value[3])
                RadW = float(value[4])
                RadFlukJ_Tot = float(value[5])
                Temp = float(value[6])
                new_ur = float(value[7])
                Press_mbar = float(value[8])
                Chuva_mm_Tot = float(value[9])
                
                climate_data = ClimateData(
                    datetime=formatted_date,
                    record=register_id,
                    wind_speed=VelVent_ms,
                    wind_direction=DirVent,
                    RadW=RadW,
                    RadFlukJ=RadFlukJ_Tot,
                    degrees=Temp,
                    ur=new_ur,
                    pressure=Press_mbar,
                    rain_amount=Chuva_mm_Tot,
                )
                climate_data_list.append(climate_data)

        try:

            check_id = ClimateData.objects.get(RECORD=register_id)

            error_files.append(file)           

        except:
            with transaction.atomic():
                ClimateData.objects.bulk_create(climate_data_list)
                
                climate_data_list.clear()

    if len(error_files) > 0:

        for files_to_move in error_files:

            shutil.move(os.path.join(files_to_read, files_to_move),
                os.path.join(error, files_to_move))
        
    new_files = [file for file in files if file not in error_files]

    if len(new_files) > 0:

        for file in files:
            
            shutil.move(os.path.join(files_to_read, file),
                os.path.join(backup, file))

    return JsonResponse({"message": "Production Orders Created"},safe=False)

@api_view(['GET'])
def index(request, start_date, end_date):
    objeto = {}
    media_dir_vent = ClimateData.objects.filter(TIMESTAMP__gte=start_date, TIMESTAMP__lte=end_date).aggregate(media_dir_vent=Avg('DirVent'))
    vel_max_vent = ClimateData.objects.filter(TIMESTAMP__gte=start_date, TIMESTAMP__lte=end_date).aggregate(vel_max_vent=Max('VelVent'))
    somatoria_chuva = ClimateData.objects.filter(TIMESTAMP__gte=start_date, TIMESTAMP__lte=end_date).aggregate(somatoria_chuva=Sum('Chuva'))
    temp_max = ClimateData.objects.filter(TIMESTAMP__gte=start_date, TIMESTAMP__lte=end_date).aggregate(temp_max=Max('Temp'))
    temp_min = ClimateData.objects.filter(TIMESTAMP__gte=start_date, TIMESTAMP__lte=end_date).aggregate(temp_min=Min('Temp'))
    objeto['mediaDirecaoVento'] = media_dir_vent['media_dir_vent']
    objeto['velocidadeMaximaVento'] = vel_max_vent['vel_max_vent']
    objeto['somatoriaChuva'] = somatoria_chuva['somatoria_chuva']
    objeto['temperaturaMaxima'] = temp_max['temp_max']
    objeto['temp_min'] = temp_min['temp_min']
    #serialized_rows = ClimateDataSerializer(dataRows, many=True)
    return Response(objeto, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_view(request, start_date, end_date):
    objeto = {}
    dataRows = ClimateData.objects.all()
    serialized_rows = ClimateDataSerializer(dataRows, many=True)
    return Response(serialized_rows.data, status=status.HTTP_200_OK)