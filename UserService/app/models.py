from django.db import models



from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    description = models.CharField(max_length=255, choices=[('buyer', 'Buyer'), ('seller', 'Seller')])
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    nationality = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=10)
    gstin_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username
