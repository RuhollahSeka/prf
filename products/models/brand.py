from django.db import models

from common.models import TimedModel
from products.models import Company


class Brand(TimedModel):
    owner = models.ForeignKey(
        to=Company,
        on_delete=models.DO_NOTHING,
        related_name='owning_brands',
    )

    manufacturer = models.ForeignKey(
        to=Company,
        on_delete=models.DO_NOTHING,
        related_name='manufactured_brands',
    )
