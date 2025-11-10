from django.urls import path
from .views import CompanyCreateView, GetCompanyView

urlpatterns = [
    path('create/', CompanyCreateView.as_view(), name='create-company'),
    path('get/', GetCompanyView.as_view(), name='get-company'),
]