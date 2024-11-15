from datetime import date, datetime, timedelta
from statistics import median
from typing import Dict, List

from dj_rql.drf import RQLFilterBackend
from django.db.models import Avg, Max, Min
from django.db.models.functions import TruncDate
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from stations.filters import ClimateDataFilterClass
from stations.models import ClimateData
from stations.serializers import ClimateDataSerializer

from django.db import transaction
from django.http import JsonResponse


class ClimateDataViewSet(ModelViewSet):
    serializer_class = ClimateDataSerializer
    queryset = ClimateData.objects.all()
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ClimateDataFilterClass

    def list(self, request):

        climate_data = self.filter_queryset(self.queryset)

        if not climate_data.exists():
            return Response(data={'error': 'No data available in the specified range'}, status=status.HTTP_404_NOT_FOUND)

        first_record = climate_data.earliest('datetime')
        last_record = climate_data.latest('datetime')

        temperature_stats = climate_data.aggregate(
            max_degrees = Max('degrees'),
            min_degrees = Min('degrees'),
            avg_degrees = Avg('degrees')
        )

        rain_stats = climate_data.aggregate(
            max_rain_amount = Max('rain_amount'),
            min_rain_amount = Min('rain_amount'),
            avg_rain_amount = Avg('rain_amount')
        )

        pressure_stats = climate_data.aggregate(
            max_pressure = Max('pressure'),
            min_pressure = Min('pressure'),
            avg_pressure = Avg('pressure')
        )

        daily_avg_temperatures = climate_data.annotate(
            date=TruncDate('datetime')
        ).values('date').annotate(
            avg_temperature=Avg('degrees')
        ).order_by('date')

        daily_avg_rain_amount = climate_data.annotate(
            date=TruncDate('datetime')
        ).values('date').annotate(
            avg_rain_amount=Avg('rain_amount')
        ).order_by('date')

        response_data = {
            'first_datetime': first_record.datetime,
            'last_datetime': last_record.datetime,
            'max_temperature': temperature_stats['max_degrees'],
            'min_temperature': temperature_stats['min_degrees'],
            'avg_temperature': temperature_stats['avg_degrees'],
            'max_rain_amount': rain_stats['max_rain_amount'],
            'min_rain_amount': rain_stats['min_rain_amount'],
            'avg_rain_amount': rain_stats['avg_rain_amount'],
            'max_pressure': pressure_stats['max_pressure'],
            'min_pressure': pressure_stats['min_pressure'],
            'avg_pressure': pressure_stats['avg_pressure'],
            'daily_avg_temperatures': list(daily_avg_temperatures),
            'daily_avg_rain_amount': list(daily_avg_rain_amount),
        }

        return Response(data=response_data, status=status.HTTP_200_OK)
    
    @action(methods=['POST'], url_path='send', detail=False)
    def post_new_data(self, request):
        file = request.FILES['file']
        climate_data_list=[]

        with file.open('rb') as arquivo:
            lines = arquivo.readlines()[4:]
            for line in lines:
                line = str(line).replace("b'", "").replace("\\r\\n'", "")
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
            with transaction.atomic():
                ClimateData.objects.bulk_create(climate_data_list)
                climate_data_list.clear()         
            return JsonResponse({"message": "Production Orders Created"},safe=False)
        except:
            return Response(data={"message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

        