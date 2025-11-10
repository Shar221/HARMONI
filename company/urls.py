from django.urls import path
from .views import CompanyCreateView, GetCompanyView, GetAllCompaniesView , CompanyEmployeesView

urlpatterns = [
    path('create/', CompanyCreateView.as_view(), name='create-company'),
    path('get/', GetCompanyView.as_view(), name='get-company'),
    path('all/', GetAllCompaniesView.as_view(), name='get-all-companies'),
    path('<int:company_id>/employees/', CompanyEmployeesView.as_view(), name='company-employees'),
]