from django.db import models

from common.models import TimedModel
from products.models import PrecautionaryPhrase, Variant


class HazardIdentification(TimedModel):
    variant = models.OneToOneField(
        to=Variant,
        on_delete=models.CASCADE,
    )

    hazard_phrases = models.TextField(
        blank=True,
    )

    precautionary_phrases = models.ManyToManyField(
        to=PrecautionaryPhrase,
    )
