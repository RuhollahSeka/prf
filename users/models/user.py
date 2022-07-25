from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        unique=True,
    )

    is_requester = models.BooleanField()

    is_fulfiller = models.BooleanField()
