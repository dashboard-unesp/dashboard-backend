from rest_framework import serializers
from stations.models import ClimateData

class ClimateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimateData
        fields = '__all__'
