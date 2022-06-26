from django.db import models

from common.models import TimedModel
from products.models import Product


class ProductRequestItem(TimedModel):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='request_items',
    )

    quantity = models.PositiveIntegerField()

    expiry_date = models.DateField(
        null=True,
        blank=True,
    )

    note = models.TextField(
        blank=True,
    )
