import fnmatch
import os
import shutil
from datetime import datetime

from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from ..data.models import *


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

            check_id = ClimateData.objects.get(RECORD=register_id)

            if check_id:

                error_files.append(file)              

            else:

                with transaction.atomic():      
                    ClimateData.objects.bulk_create(climate_data_list)

                shutil.move(os.path.join(files_to_read, file),
                    os.path.join(backup, file))
                
                climate_data_list.clear()

    for files_to_move in error_files:

        shutil.move(os.path.join(files_to_read, files_to_move),
            os.path.join(error, files_to_move))  

    return JsonResponse({"message": "Production Orders Created"},safe=False)