from django.db import models

from common.models import TimedModel
from products.models import Warehouse


class Bay(TimedModel):
    warehouse = models.ForeignKey(
        to=Warehouse,
        on_delete=models.CASCADE,
        related_name='bays'
    )

    code = models.CharField(
        max_length=128,
        unique=True,
    )
