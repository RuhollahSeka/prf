from django.db import models

from common.models import TimedModel
from requests.models import ProductRequest
from users.models import User


class Comment(TimedModel):
    commenter = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    product_request = models.ForeignKey(
        to=ProductRequest,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    text = models.TextField()
