from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from users.views import UserViewSet, MeViewSet

from stations.sync_data import sync_files
from stations.views import ClimateDataViewSet


schema_view = get_swagger_view(title='Unesp Dashboard API')

stations_router = DefaultRouter()
users_router = DefaultRouter()

stations_router.register('climate', ClimateDataViewSet, basename="CDT")

users_router.register('users', UserViewSet, 'UVT')
users_router.register('me', MeViewSet, 'MVT')

urlpatterns = [
    *stations_router.urls,
    *users_router.urls,
    path('sync-files', sync_files),
    path('docs', schema_view)
]