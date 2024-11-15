import os
import shutil
import fnmatch

from datetime import datetime
from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from stations.models import ClimateData


@csrf_exempt
@require_http_methods(['POST'])
def sync_files(request):
    files_to_read = os.path.abspath(os.path.join(settings.BASE_DIR, '..' + "/pi_univesp_backend/PI_files/"))

    os.makedirs(files_to_read, exist_ok=True)
    print(f"Novo arquivo recebido: {request}")

    if 'file' not in request.FILES:
        return JsonResponse({"message": "Nenhum arquivo enviado!"}, safe=False)

    file = request.FILES['file']
    print(f"arquivo aqui: {file}")

    file_path = os.path.join(files_to_read, file.name)
    print(f"Path do arquivo: {file_path}")

    # Salva o arquivo no diretório especificado
    with open(file_path, 'wb+') as destino:
        for chunk in file.chunks():
            destino.write(chunk)

    files_to_read = os.path.abspath(os.path.join(settings.BASE_DIR, '..' + "/pi_univesp_backend/PI_files/"))
    backup = files_to_read + r"\BACKUP"
    error = files_to_read + r"\ERROR"

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

    return JsonResponse({"message": "Production Orders Created"}, safe=False)