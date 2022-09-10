from django.db import models

from common.models import TimedModel


class PrecautionaryPhrase(TimedModel):
    code = models.CharField(
        max_length=128,
    )

    phrase = models.TextField()
