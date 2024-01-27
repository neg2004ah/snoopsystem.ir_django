from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator



class CustomUser(AbstractUser):
    id_call = models.CharField(max_length=11)
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username