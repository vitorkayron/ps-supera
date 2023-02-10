from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30, blank=True, null=False)
    price = models.DecimalField(blank=True)
    score = models.IntegerField(blank=True)
