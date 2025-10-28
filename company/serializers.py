from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']