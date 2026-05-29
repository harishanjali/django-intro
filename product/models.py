from django.db import models

# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=30)
    pprice = models.FloatField()
    pcategory = models.CharField(max_length=30)