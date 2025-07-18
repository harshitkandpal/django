from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomerUser(AbstractUser):

    roleOptions = [
        ('1', 'Admin'),
        ('2', 'Customer'),
        ('3', 'Staff'),
    ]
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    password = models.CharField(max_length=128, blank=False, null=False )
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=roleOptions)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username