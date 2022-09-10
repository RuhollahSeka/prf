from django.db import models

from common.models import TimedModel


class Variant(TimedModel):
    name = models.CharField(
        max_length=256,
    )

    code = models.CharField(
        max_length=128,
        unique=True,
    )
