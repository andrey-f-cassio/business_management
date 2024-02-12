from django.urls import path
from .views import Company

urlpatterns = [
    path('create/', Company.as_view(), name='company-create'),
]
