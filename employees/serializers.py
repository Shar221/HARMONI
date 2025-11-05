from rest_framework import serializers
from authentication.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'company']
        read_only_fields = ['id', 'company']

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        company = user.company  # Link new employee to admin’s company
        employee = User.objects.create(
            company=company,
            role='employee',
            **validated_data
        )
        employee.set_password(validated_data['password'])
        employee.save()
        return employee