from rest_framework import generics, permissions
from .models import Payroll
from .serializers import PayrollSerializer

class PayrollListCreateView(generics.ListCreateAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class PayrollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [permissions.IsAuthenticated]