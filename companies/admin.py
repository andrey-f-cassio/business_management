from django.contrib import admin

from companies.models import Company, CompanyMember

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyMember)