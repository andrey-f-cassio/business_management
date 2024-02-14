from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'companies'

    def ready(self):
        """
        Called when the app 'companies' is ready to used.
        """

        from companies.tasks import create_task_update_company_data_if_not_exists
        import sys
        if 'runserver' in sys.argv:
            create_task_update_company_data_if_not_exists()
