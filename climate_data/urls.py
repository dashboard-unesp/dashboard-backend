
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
    path("", include("climate_data.data.urls", namespace="data")),
    
]

urlpatterns += i18n_patterns(path("", admin.site.urls))