from django.contrib.postgres.fields import DecimalRangeField
from django.db import models

from common.models import TimedModel
from products.models import Variant


class ChemicalProperties(TimedModel):
    variant = models.OneToOneField(
        to=Variant,
        on_delete=models.CASCADE,
    )

    physical_state = models.CharField(
        max_length=64,
    )

    colour = models.CharField(
        max_length=128,
    )

    odour = models.CharField(
        max_length=128,
    )

    ph_range = DecimalRangeField(
        null=True,
        blank=True,
    )

    melting_point = models.FloatField(
        null=True,
        blank=True,
    )

    flash_point = models.FloatField(
        null=True,
        blank=True,
    )

    explosive_characteristics = models.TextField(
        blank=True,
    )

    vapour_pressure = models.FloatField()

    density = DecimalRangeField(
        null=True,
        blank=True,
    )

    solubility = models.TextField(
        blank=True,
    )
