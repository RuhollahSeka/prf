from django.db import models


class Component(models.Model):
    name = models.CharField(
        max_length=256,
    )

    code = models.CharField(
        max_length=128,
    )
