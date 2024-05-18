
from django.contrib import admin
from django.urls import path

from ..data import views as v

app_name = "data"

urlpatterns = [
    path("sync_files/", v.sync_files, name="sync_files"),
]
