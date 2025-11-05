from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('ADMIN', 'Admin'),
    ('EMPLOYEE', 'Employee'),
    ('SUPERADMIN', 'Superadmin'),
)
class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    company = models.ForeignKey('company.Company', on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    def __str__(self):
        return self.username

    def __str__(self):
        return f"{self.username} ({self.role})"
