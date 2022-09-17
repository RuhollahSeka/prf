from django.db import models

from common.models import TimedModel
from products.models import GHSStatement


class Ingredient(TimedModel):
    chemical_name = models.CharField(
        max_length=256,
    )

    n_cas = models.CharField(
        max_length=256,
    )

    hazard_phrases = models.ManyToManyField(
        to=GHSStatement,
        related_name='ingredients',
    )
