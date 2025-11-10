from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.exceptions import PermissionDenied

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
    
class GetAllCompaniesView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()




class CompanyEmployeesView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        user = self.request.user

        if user.is_superuser or (hasattr(user, 'company') and user.company.id == int(company_id)):
            return User.objects.filter(company_id=company_id)

        raise PermissionDenied("You do not have permission to view employees for this company.")