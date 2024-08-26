from typing import Dict, List
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from stations.serializers import ClimateDataSerializer
from stations.models import ClimateData
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, timedelta
from statistics import median

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
    
    