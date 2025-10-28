from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Company
from .serializers import CompanySerializer

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
