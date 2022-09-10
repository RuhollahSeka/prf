from django.db import models

from common.models import TimedModel


class InternationalRegulation(TimedModel):
    code = models.CharField(
        max_length=32,
        unique=True,
    )
