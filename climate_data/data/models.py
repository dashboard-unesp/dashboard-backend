from django.db import models
from uuid import uuid4
# Create your models here.

class BaseData (models.Model):
    id_base_data = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    code = models.CharField(
        max_length= 20,
        null = True,
        blank = True,
        verbose_name = "code",
    )
    value = models.CharField(
        max_length= 20,
        null = True,
        blank = True,
        verbose_name = "value",
    )
    type = models.CharField(
        max_length= 20,
        null = True,
        blank = True,
        verbose_name = "type",
    )
    
    def __str__(self):
        return self.value    
    
class ClimateData (models.Model):
    id_climate_data = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    TIMESTAMP = models.DateTimeField(
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "Time Stamp",
    )
    RECORD = models.PositiveIntegerField(
        null = True,
        unique=True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "Record",
    )
    VelVent = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "VelVent ms",
    )

    DirVent = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "DirVent",
    )

    RadW = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "RadW",
    )

    RadFlukJ = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "RadFlukJTot",
    )

    Temp = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "Temp",
    )

    UR = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "UR",
    )

    Press = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "Press_mbar",
    )

    Chuva = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "Chuva_mm_Tot",
    )


    # def __str__(self):
    #     return self.RECORD