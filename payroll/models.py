from django.db import models
from django.conf import settings
from company.models import Company

class Payroll(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='payrolls'
    )
    company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE, 
        related_name='company_payrolls'
    )
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pay_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def net_pay(self):
        return self.base_salary + self.bonuses - self.deductions

    def __str__(self):
        return f"{self.employee.username} - {self.company.name} ({self.pay_date})"