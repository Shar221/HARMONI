from rest_framework import serializers
from .models import Payroll

class PayrollSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.username', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    net_pay = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Payroll
        fields = [
            'id',
            'employee',
            'employee_name',
            'company',
            'company_name',
            'base_salary',
            'bonuses',
            'deductions',
            'net_pay',
            'pay_date',
            'created_at',
        ]