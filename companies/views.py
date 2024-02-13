from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Company, CompanyMember
from .serializers import CompanySerializer, CompanyMemberSerializer
from django.shortcuts import get_object_or_404


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)


class CompanyMemberViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyMemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        company = get_object_or_404(Company, pk=company_id)
        return CompanyMember.objects.filter(company=company)
