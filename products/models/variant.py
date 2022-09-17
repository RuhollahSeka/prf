from django.db import models

from common.models import TimedModel
from products.models import Dimensions, Component, Product, Ingredient


class Variant(TimedModel):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='variants',
    )

    name = models.CharField(
        max_length=256,
    )

    code = models.CharField(
        max_length=128,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    barcode = models.CharField(
        max_length=32,
    )

    carton_barcode = models.CharField(
        max_length=32,
        blank=True,
    )

    dimensions = models.OneToOneField(
        to=Dimensions,
        on_delete=models.DO_NOTHING,
    )

    weight = models.FloatField()

    components = models.ManyToManyField(
        to=Component,
        related_name='variants',
    )

    ingredients = models.ManyToManyField(
        to=Ingredient,
        related_name='variants',
    )

    image = models.ImageField(
        upload_to='images/variants/',
        max_length=1024,
        null=True,
        blank=True,
    )

    additional_information = models.TextField(
        blank=True,
    )
