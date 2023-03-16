from django.db import models


class Seller(models.Model):
    company_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)

    objects = models.Manager


class Customer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.DateTimeField(max_length=50)

    objects = models.Manager

# Create your models here.
