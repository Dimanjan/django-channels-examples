from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=200)
    imgae=models.URLField(max_length=1000)
    price=models.CharField(max_length=200)
    market_cap=models.CharField(max_length=200)

    def __str__(self):
        return self.name