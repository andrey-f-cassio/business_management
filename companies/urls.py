from django.urls import path
from .views import CompanyViewSet

urlpatterns = [
    path('create/', CompanyViewSet.as_view({'post': 'create'}), name='company-create'),
]
