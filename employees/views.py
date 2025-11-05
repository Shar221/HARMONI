from rest_framework import generics, permissions
from .models import Employee
from .serializers import EmployeeSerializer
from authentication.models import User

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Admin can only see employees from their own company
        return User.objects.filter(company=user.company, role='employee')

    def perform_create(self, serializer):
        serializer.save()

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
  
