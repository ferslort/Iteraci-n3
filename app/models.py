from django.db import models

# Create your models here.

class UserCustom(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


class Supplier(models.Model):
    razon = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)
