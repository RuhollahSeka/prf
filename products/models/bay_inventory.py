from django.db import models

from common.models import TimedModel
from products.models import Product, Bay


class BayInventory(TimedModel):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='inventories',
    )

    bay = models.ForeignKey(
        to=Bay,
        on_delete=models.CASCADE,
        related_name='inventories',
    )

    quantity = models.IntegerField(
        default=0,
    )

    class Meta:
        unique_together = ('product', 'bay')
