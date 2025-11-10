from django.db import models
from company.models import Company

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField(default=30)  # 30 days, etc.

    def __str__(self):
        return self.name


class Subscription(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company.name} - {self.plan.name}"