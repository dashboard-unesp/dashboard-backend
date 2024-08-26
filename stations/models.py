from django.db import models
from uuid import uuid4

class BaseData(models.Model):

    id_base_data = models.UUIDField(primary_key=True, default=uuid4, auto_created=True)
    
    code = models.CharField(max_length=20, null=True, blank=True)
    value = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    
    class Meta:
        pass
    
class ClimateData(models.Model):

    id_climate_data = models.UUIDField(primary_key=True, default=uuid4, auto_created=True)

    datetime = models.DateTimeField(null=True, blank=True)
    record = models.PositiveIntegerField(null=True, blank=True, unique=True)

    wind_speed = models.DecimalField(
        max_digits=12,
        decimal_places=5,
        null=True,
        blank=True,
    )

    wind_direction = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
    )

    RadW = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
    )

    RadFlukJ = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
    )

    degrees = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
    )

    ur = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
    )

    pressure = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
    )

    rain_amount = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
    )

    class Meta:
        pass
