from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    score = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return str(self.username)