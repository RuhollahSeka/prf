from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'

    is_requester = models.BooleanField()

    is_fulfiller = models.BooleanField()
