from django.db import models


class Dimensions(models.Model):
    length = models.FloatField()

    width = models.FloatField()

    height = models.FloatField()
