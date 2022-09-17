from django.db import models

from common.models import TimedModel


class GHSStatement(TimedModel):
    TYPE_PRECAUTIONARY = 'precautionary'
    TYPE_HAZARD = 'hazard'
    TYPE_CHOICES = (
        (TYPE_PRECAUTIONARY, 'precautionary'),
        (TYPE_HAZARD, 'hazard'),
    )

    code = models.CharField(
        max_length=128,
    )

    type = models.CharField(
        max_length=32,
        choices=TYPE_CHOICES,
    )

    phrase = models.TextField()
