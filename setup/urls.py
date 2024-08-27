from django.urls import path
from rest_framework.routers import DefaultRouter

from stations.views import ClimateDataViewSet
from stations.sync_data import sync_files

from users.views import UserViewSet

stations_router = DefaultRouter()
users_router = DefaultRouter()

stations_router.register('climate', ClimateDataViewSet, basename="CDT")

users_router.register('users', UserViewSet, 'UVT')

urlpatterns = [
    *stations_router.urls,
    *users_router.urls,
    path('sync-files/', sync_files)
]