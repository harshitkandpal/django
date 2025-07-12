from django.db import models

# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    room_image = models.ImageField(upload_to='room_images/', blank=True, null=True)
    room_description = models.TextField(blank=True, null=True)
    max_occupancy = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - {self.room_number}"