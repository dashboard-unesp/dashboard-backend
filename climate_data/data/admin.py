from django.contrib import admin

from .models import *


class BaseDataAdmin(admin.ModelAdmin):
    list_display = ('code', 'value', 'type')
    search_fields = ('code', 'value', 'type')

admin.site.register(BaseData, BaseDataAdmin)

class ClimateDataAdmin(admin.ModelAdmin):
    list_display = ('RECORD', 'TIMESTAMP', 'VelVent', 'DirVent', 'RadW', 'RadFlukJ', 'Temp', 'UR', 'Press', 'Chuva')
    search_fields = ('RECORD',)
    list_filter = ()

admin.site.register(ClimateData, ClimateDataAdmin)