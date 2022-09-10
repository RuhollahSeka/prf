from django.db import models

from common.models import TimedModel


class Company(TimedModel):
    name = models.CharField(
        max_length=128,
    )

    email = models.EmailField()

    contact_phone_number = models.CharField(
        max_length=32,
    )

    emergency_phone_number = models.CharField(
        max_length=32,
    )
