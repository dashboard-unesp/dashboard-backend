from django.urls import path
from rest_framework.routers import DefaultRouter

from stations.views import ClimateDataViewSet
from stations.sync_data import sync_files

route = DefaultRouter()

route.register('climate', ClimateDataViewSet, basename="CDT")

urlpatterns = [
    *route.urls,
    path('sync-files/', sync_files)
]