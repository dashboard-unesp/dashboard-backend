import fnmatch
import os
from datetime import datetime

from data.models import *
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(['GET'])
def sync_production_documents(self):

    files_to_read = os.path.abspath(os.path.join(settings.BASE_DIR, '..' + "/PI_files/"))

    backup = files_to_read + "\BACKUP"

    climate_data_list = {}

    files = fnmatch.filter(os.listdir(files_to_read), "*.dat")

    for file in files:

        with open(files_to_read + "/" + file, 'r', encoding='utf8') as arquivo:
            lines = arquivo.readlines()[4:]
            for line in lines:
                value = line.split(",")
                data_hora = value[0]
                formatted_date = datetime.strptime(data_hora, '%Y-%m-%d  %H:%M:%S')
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
                    TIMESTAMP=formatted_date,
                    RECORD=register_id,
                    VelVent=VelVent_ms,
                    DirVent=DirVent,
                    RadW=RadW,
                    RadFlukJ=RadFlukJ_Tot,
                    Temp=Temp,
                    UR=new_ur,
                    Press=Press_mbar,
                    Chuva=Chuva_mm_Tot,
                )
                climate_data_list.append(climate_data)
                
            
            ClimateData.objects.bulk_create(climate_data_list)

    return JsonResponse({"message": "Production Orders Created"},safe=False)