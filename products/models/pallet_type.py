from django.db import models

from common.models import TimedModel


class PalletType(TimedModel):
    name = models.CharField(
        max_length=128,
        unique=True,
    )
