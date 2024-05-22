from rest_framework import viewsets
from climate_data.data.api import serializers
from climate_data.data import models
class ClimateDataViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClimateDataSerializer
    queryset = models.ClimateData.objects.all()
