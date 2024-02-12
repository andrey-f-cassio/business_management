from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    owner = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=20)
    corporate_name = models.CharField(max_length=100)
    trade_name = models.CharField(max_length=100)

    def __str__(self):
        return self.trade_name


class CompanyMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'company')

    def __str__(self):
        return f"{self.user.username} - {self.company.trade_name}"
