import datetime

import jwt
from django.contrib.auth.models import AbstractUser
from django.db import models
from quickstart.settings import JWT_SECRET, TOKEN_EXPIRATION


class User(AbstractUser):
    pass


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
