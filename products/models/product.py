from django.db import models

from common.models import TimedModel
from products.models import Brand


class Product(TimedModel):
    name = models.CharField(
        max_length=128,
    )

    brand = models.ForeignKey(
        to=Brand,
        on_delete=models.DO_NOTHING,
        related_name='products',
    )
