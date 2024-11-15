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


class ClimateDataViewSet(ModelViewSet):
    serializer_class = ClimateDataSerializer
    queryset = ClimateData.objects.all()

    def list(self, request):
        params = request.query_params

        date_from = params.get('date_from', f'{datetime.now()}'.split(' ')[0])
        date_to = params.get('date_to', f'{datetime.now() - timedelta(7)}'.split(' ')[0])

        queryset = ClimateData.objects.filter(datetime__range=[date_from, date_to])
        serializer = ClimateDataSerializer(data=queryset, many=True)
        
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @staticmethod
    def calc_from_daily_data(data: List[ClimateData]) -> Dict[str, float]:
        degrees = []

        for obj in data:
            degrees.append(obj.degrees)
        response = ClimateDataViewSet.calc_min_and_max_temp_from_daily_data(degrees)
        
        response['median'] = median(degrees)
        response['datetime'] = data[0].datetime
        
        return response

    @staticmethod
    def calc_min_and_max_temp_from_daily_data(daily_degrees: List[float]) -> Dict[str, float]:
        return dict(minTemp=min(daily_degrees), maxTemp=max(daily_degrees))


    @action(methods=['GET'], detail=False, url_path='barchart')
    def get_barchart(self, request) -> List[Dict]:

        params = request.query_params
        date_from = params.get('date_from', f'{datetime.now()}'.split(' ')[0])
        date_to = params.get('date_to', f'{datetime.now() - timedelta(7)}'.split(' ')[0])
        queryset = ClimateData.objects.filter(datetime__range=[date_from, date_to])
    
        grouped_data = {}
        for item in queryset:
            day = item.datetime.day
            if day not in grouped_data:
                grouped_data[day] = []
            grouped_data[day].append(item)

        response = []
        for group, data in grouped_data.items():
            daily_data = self.calc_from_daily_data(data)
            response.append(daily_data)
 
        return Response(data=response, status=status.HTTP_200_OK)
    

class ClimateDataViewSet2(ModelViewSet):
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
    
    def create(self, request):
        return super().create(request, *args, **kwargs)