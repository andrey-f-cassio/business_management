import requests
from django.utils import timezone

from .models import Company


def update_company_data():
    # month_ago = timezone.now() - timezone.timedelta(minutes=1)
    month_ago = timezone.now() - timezone.timedelta(days=30)
    companies_to_update = Company.objects.filter(created_at__lte=month_ago)

    for company in companies_to_update:
        response = requests.get(f'https://receitaws.com.br/v1/cnpj/{company.cnpj}')
        if response.status_code == 200:
            data = response.json()
            company.corporate_name = data.get('nome')
            company.trade_name = data.get('fantasia')
            company.status = data.get('status')
            company.save()
