from django.db import models
from django.utils import timezone
from datetime import timedelta
from company.models import Company

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField(default=30)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = timezone.now() + timedelta(days=self.plan.duration_days)

        if self.end_date < timezone.now():
            self.is_active = False

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company.name} - {self.plan.name} ({'Active' if self.is_active else 'Expired'})"