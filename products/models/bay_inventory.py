from django.db import models

from common.models import TimedModel
from products.models import Variant, Bay


class BayInventory(TimedModel):
    variant = models.ForeignKey(
        to=Variant,
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
        unique_together = ('variant', 'bay')
