from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.ImageField(upload_to='item_images/', blank=True, null=True)
