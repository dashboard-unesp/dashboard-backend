from django.db import models

# Create your models here.

class BaseData (models.Model):
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
    VelVent_UOM = models.ForeignKey(
        BaseData,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        default= None,
        related_name = "VelVent_UOM",
    )
    DirVent = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "DirVent",
    )
    DirVent_UOM = models.ForeignKey(
        BaseData,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        default= None,
        related_name = "DirVent_UOM",
    )
    RadW = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "RadW",
    )
    RadW_UOM = models.ForeignKey(
        BaseData,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        default= None,
        related_name = "RadW_UOM",
    )
    RadFlukJ = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "RadFlukJTot",
    )
    RadFlukJ_UOM = models.ForeignKey(
        BaseData,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        default= None,
        related_name = "RadFlukJ_UOM",
    )
    Temp = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "Temp",
    )
    Temp_UOM = models.ForeignKey(
        BaseData,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        default= None,
        related_name = "Temp_UOM",
    )
    UR = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "UR",
    )
    UR_UOM = models.ForeignKey(
        BaseData,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        default= None,
        related_name = "UR_UOM",
    )
    Press = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "Press_mbar",
    )
    Press_UOM = models.ForeignKey(
        BaseData,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        default= None,
        related_name = "Press_UOM",
    )
    Chuva = models.DecimalField(
        max_digits = 12,
        decimal_places = 5,
        null = True,
        blank = True,
        help_text = "Texto explicativo do campo",
        verbose_name = "Chuva_mm_Tot",
    )
    Chuva_UOM = models.ForeignKey(
        BaseData,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        default= None,
        related_name = "Chuva_UOM",
    )

    def __str__(self):
        return self.RECORD