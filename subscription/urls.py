from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionPlanViewSet, SubscriptionViewSet, ActiveSubscriptionsView, ExpiredSubscriptionsView, RenewSubscriptionView

router = DefaultRouter()
router.register(r'plans', SubscriptionPlanViewSet, basename='subscription-plan')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('active/', ActiveSubscriptionsView.as_view(), name='active-subscriptions'),
    path('expired/', ExpiredSubscriptionsView.as_view(), name='expired-subscriptions'),
    path('renew/', RenewSubscriptionView.as_view(), name='renew-subscription'),
]