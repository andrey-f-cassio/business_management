import requests
from django.utils import timezone

from .models import Company


def update_company_data():
    current_time = timezone.now()
    companies_to_update = Company.objects.all()

    for company in companies_to_update:
        if not company.last_updated or (current_time - company.last_updated).days > 30:
            response = requests.get(f'https://receitaws.com.br/v1/cnpj/{company.cnpj}')
            if response.status_code == 200:
                data = response.json()
                company.corporate_name = data.get('nome', company.corporate_name)
                company.trade_name = data.get('fantasia', company.trade_name)
                company.status = data.get('status', company.status)
                company.last_updated = current_time
                company.save()