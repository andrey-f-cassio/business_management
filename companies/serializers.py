from rest_framework import serializers
from .models import Company, CompanyMember, User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyMemberSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=User.objects.all(),
        source='user'
    )
    company_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Company.objects.all(),
        source='company'
    )

    class Meta:
        model = CompanyMember
        fields = ['id', 'user_id', 'company_id', 'date_joined']

