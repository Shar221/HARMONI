from rest_framework import viewsets , generics, permissions
from rest_framework.permissions import IsAdminUser
from .models import SubscriptionPlan, Subscription
from .serializers import SubscriptionPlanSerializer, SubscriptionSerializer
from django.utils import timezone
from rest_framework import views, status
from rest_framework.response import Response
from company.models import Company
from datetime import timedelta

class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminUser]  


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAdminUser] 


class ActiveSubscriptionsView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(is_active=True, end_date__gte=timezone.now())


class ExpiredSubscriptionsView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(is_active=False, end_date__lt=timezone.now())
    
class RenewSubscriptionView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        company_id = request.data.get("company_id")
        plan_name = request.data.get("plan_name")

        if not company_id or not plan_name:
            return Response(
                {"error": "company_id and plan_name are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

        subscription = Subscription.objects.filter(company=company).first()
        
        new_end_date = timezone.now() + timedelta(days=30)

        if subscription:
            subscription.plan_name = plan_name
            subscription.start_date = timezone.now()
            subscription.end_date = new_end_date
            subscription.is_active = True
            subscription.save()
        else:
            subscription = Subscription.objects.create(
                company=company,
                plan_name=plan_name,
                start_date=timezone.now(),
                end_date=new_end_date,
                is_active=True
            )

        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)    