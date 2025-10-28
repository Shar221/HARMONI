from django.db import models
from django.conf import settings
from django.utils import timezone


class Company(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owned_companies'
    )
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=50, blank=True, null=True)
    theme_color = models.CharField(max_length=7, blank=True, null=True)  
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    subscription_plan = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


