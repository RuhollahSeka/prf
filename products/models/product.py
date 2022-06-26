from django.db import models

from common.models import TimedModel


class Product(TimedModel):
    name = models.CharField(
        max_length=256,
    )

    code = models.CharField(
        max_length=128,
    )
