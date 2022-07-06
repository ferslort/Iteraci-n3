from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
