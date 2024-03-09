from django.apps import AppConfig

#configurations go here
class StudentConfig(AppConfig):
    name = "apps.students"

    def ready(self):
        import apps.students.signals