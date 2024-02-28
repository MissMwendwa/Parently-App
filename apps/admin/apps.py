from django.apps import AppConfig

class AdminConfig(AppConfig):
    name = "apps.admin"

    def ready(self):
        import apps.admin.signals