from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=10, unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
