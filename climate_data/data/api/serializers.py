from rest_framework import serializers
from climate_data.data import models

class ClimateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClimateData
        fields = '__all__'

