
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from rest_framework import routers
from climate_data.data.api import viewsets as dadosviewsets
from climate_data.data.views import index, list_view

route = routers.DefaultRouter()
route.register(r'barchart<str:startDate>', dadosviewsets.ClimateDataViewSet, basename="barchart")
route.register(r'dados/piechart/<str:startDate>', dadosviewsets.ClimateDataViewSet, basename="piechart")
route.register(r'dados/list/<str:startDate>', dadosviewsets.ClimateDataViewSet, basename="listageral")

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
    path("", include("climate_data.data.urls", namespace="data")),
    path("filter/<str:start_date>/<str:end_date>", index, name="filter"),
    path("list/<str:start_date>/<str:end_date>", list_view, name="list-all"),
    path("", include(route.urls)),

]

urlpatterns += i18n_patterns(path("", admin.site.urls))