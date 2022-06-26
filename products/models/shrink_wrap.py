from django.db import models

from common.models import TimedModel


class ShrinkWrap(TimedModel):
    name = models.CharField(
        max_length=128,
        unique=True,
    )
