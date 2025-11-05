from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import User
from company.models import Company

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(write_only=True, required=False)   
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2', 'role', 'company_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        company_name = validated_data.pop('company_name', None)
        password = validated_data.pop('password', None)
        user = User(**validated_data)

        if company_name:
            company, created = Company.objects.get_or_create(name=company_name)
            user.company = company

        if password:
            user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'company_name']
