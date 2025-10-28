from rest_framework import serializers
from .models import Company
from authentication.models import User

class CompanySerializer(serializers.ModelSerializer):
    admin_email = serializers.EmailField(write_only=True)
    admin_password = serializers.CharField(write_only=True)
    admin_name = serializers.CharField(write_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'admin_email', 'admin_password', 'admin_name', 'created_at']

    def create(self, validated_data):
        admin_email = validated_data.pop('admin_email')
        admin_password = validated_data.pop('admin_password')
        admin_name = validated_data.pop('admin_name')

        company = Company.objects.create(**validated_data)

        admin_user = User.objects.create_user(
            username=admin_email,
            email=admin_email,
            password=admin_password,
            first_name=admin_name,
            role='Admin',
            company_name=company.name
        )

        company.admin = admin_user
        company.save()

        return company