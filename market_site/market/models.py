from django.db import models

# Create your models here.

class Items(models.Model):
    article = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    vat = models.DecimalField(max_digits=15, decimal_places=2)
    discount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name
