import datetime

import jwt
from django.contrib.auth.models import AbstractUser
from django.db import models
from quickstart.settings import JWT_SECRET, TOKEN_EXPIRATION


def generate_token(user):
    user_info = {
        'username': user.username,
        'email': user.email,
        'user_id': user.id
    }
    return jwt.encode({
        'user_info': user_info,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRATION)
    }, JWT_SECRET, algorithm='HS256')


class User(AbstractUser):
    pass


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
