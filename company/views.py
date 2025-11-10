from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer

class CompanyCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    

class GetCompanyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        company = getattr(user, 'company', None)
        if company:
            serializer = self.get_serializer(company)
            return Response(serializer.data)
        return Response({"detail": "No company associated with this user."}, status=404)