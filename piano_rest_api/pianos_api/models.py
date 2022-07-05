from django.db import models

# Create your models here.

class Piano(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
