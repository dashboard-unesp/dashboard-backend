from rest_framework.viewsets import ModelViewSet
from stations.serializers import ClimateDataSerializer
from stations.models import ClimateData
from rest_framework.response import Response
from rest_framework import status
import json

class ClimateDataViewSet(ModelViewSet):
    serializer_class = ClimateDataSerializer

    def list(self, request):
        params = request.query_params

        date_from = params.get('date_from')
        date_to = params.get('date_to')

        print(date_from)

        if not date_from:
            return Response(data={'message': 'invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={'message': 'valid endpoint'}, status=status.HTTP_200_OK)
