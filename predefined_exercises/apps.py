from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class PredefinedExercisesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predefined_exercises'

