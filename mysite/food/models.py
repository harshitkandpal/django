from django.db import models
from users.models import CustomerUser

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.ImageField(upload_to='item_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ManyToManyField("food.Item")
    user = models.ForeignKey("users.CustomerUser", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    table_number = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return f"Order {self.id} by {self.user.username} on {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}"
