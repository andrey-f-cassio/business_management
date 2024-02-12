from rest_framework import serializers
from .models import Company, CompanyMember


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyMember
        fields = ['id', 'user', 'company', 'date_joined']
