from django.contrib.auth.models import AbstractUser
from django.db import models
ROLE_CHOICES = [
    ('ADMIN', 'Admin'),
    ('EMPLOYEE', 'Employee'),
]

class User(AbstractUser):
    role = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYEE')
    company_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
