from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = "apps.coreapp"

    def ready(self):
        import apps.coreapp.signals