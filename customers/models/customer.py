from django.db import models

from common.models import TimedModel


class Customer(TimedModel):
    name = models.CharField(
        max_length=256,
    )

    country = models.CharField(
        max_length=128,
    )
