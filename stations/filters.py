from dj_rql.filter_cls import AutoRQLFilterClass

from stations.models import ClimateData


class ClimateDataFilterClass(AutoRQLFilterClass):
    MODEL = ClimateData