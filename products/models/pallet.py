from django.db import models

from common.models import TimedModel
from products.models import PalletType, Dimensions, Variant


class Pallet(TimedModel):
    type = models.ForeignKey(
        to=PalletType,
        on_delete=models.DO_NOTHING,
        related_name='pallets',
    )

    variant = models.OneToOneField(
        to=Variant,
        on_delete=models.CASCADE,
    )

    pallet_weight = models.FloatField()

    pallet_dimensions = models.OneToOneField(
        to=Dimensions,
        on_delete=models.DO_NOTHING,
        related_name='pallet',
    )

    pallet_wrapping = models.CharField(
        max_length=256,
    )

    layers_count = models.PositiveSmallIntegerField()

    cartons_per_layer = models.PositiveSmallIntegerField()

    units_per_carton = models.PositiveSmallIntegerField()

    carton_weight = models.FloatField()

    carton_dimensions = models.OneToOneField(
        to=Dimensions,
        on_delete=models.DO_NOTHING,
        related_name='carton',
    )

    formation_diagram = models.FileField(
        upload_to='images/pallets/formations/',
        max_length=1024,
        null=True,
        blank=True,
    )

    formation_note = models.TextField(
        blank=True,
    )
