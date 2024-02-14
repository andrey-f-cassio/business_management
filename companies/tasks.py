import requests
from django.utils import timezone
from ratelimit import limits, sleep_and_retry

from django.utils.timezone import now
from datetime import timedelta
from django_q.tasks import schedule
from django_q.models import Schedule

from .models import Company

ONE_MINUTE = 60


@sleep_and_retry
@limits(calls=10, period=ONE_MINUTE)
def call_receita_api(cnpj):
    response = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj}')
    return response


def update_company_data():
    current_time = timezone.now()
    companies_to_update = Company.objects.all()

    for company in companies_to_update:
        if not company.last_updated or (current_time - company.last_updated).days > 30:
            response = call_receita_api(company.cnpj)
            if response.status_code == 200:
                data = response.json()
                company.corporate_name = data.get('nome', company.corporate_name)
                company.trade_name = data.get('fantasia', company.trade_name)
                company.status = data.get('status', company.status)
                company.last_updated = current_time
                company.save()


def create_task_update_company_data_if_not_exists():
    if not Schedule.objects.filter(func='companies.tasks.update_company_data').exists():
        schedule('companies.tasks.update_company_data',
                 schedule_type=Schedule.ONCE,
                 next_run=now() + timedelta(seconds=10))
        print('Task "update_company_data" successfully scheduled to run in 10 seconds.')
    else:
        print('The "update_company_data" task is already scheduled.')
