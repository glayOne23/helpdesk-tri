from django.apps import AppConfig


class AdminpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.adminpage'

    def ready(self):
        import apps.adminpage.signals
