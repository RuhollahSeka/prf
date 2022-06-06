from django.db import models

from common.models import TimedModel
from customers.models import Customer


class CustomerAddress(TimedModel):
    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
        related_name='addresses',
    )

    line1 = models.TextField()

    line2 = models.TextField()

    city = models.CharField(
        max_length=128,
    )

    country = models.CharField(
        max_length=128,
    )

    postal_code = models.CharField(
        max_length=128,
    )
