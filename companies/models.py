from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    owner = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=20)
    corporate_name = models.CharField(max_length=100)
    trade_name = models.CharField(max_length=100)

    def __str__(self):
        return self.trade_name
