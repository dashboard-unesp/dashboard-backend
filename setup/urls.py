from django.urls import path
from rest_framework.routers import DefaultRouter

from stations.sync_data import sync_files
from stations.views import ClimateDataViewSet, ClimateDataViewSet2

route = DefaultRouter()

route.register('climate', ClimateDataViewSet, basename="CDT")
route.register('climate2', ClimateDataViewSet2, basename="CDT2")

urlpatterns = [
    *route.urls,
    path('sync-files/', sync_files)
]