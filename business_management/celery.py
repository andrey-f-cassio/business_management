import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business_management.settings')

app = Celery('business_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
