from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField()
    
