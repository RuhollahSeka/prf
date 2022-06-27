from django.db import models

from common.models import TimedModel
from products.models import Product
from product_requests.models import ProductRequest
from users.models import User


class Job(TimedModel):
    fulfiller = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='jobs',
    )

    product_request = models.ForeignKey(
        to=ProductRequest,
        on_delete=models.CASCADE,
        related_name='jobs',
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='jobs',
    )

    quantity = models.PositiveIntegerField()
