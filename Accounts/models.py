from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("regular", "Regular User"),
        ("analyst", "Analyst"),
    )
    phone = models.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="regular")

    def __str__(self):
        return self.username