from django.core.management.base import BaseCommand
from predefined_exercises.seed_exercises import seed_data


class Command(BaseCommand):
    help = "Create predifined exercises"

    def handle(self,*args,**options):
        print(options)
        if "seed_db" in options.get('action'):
            seed_data()
            self.stdout.write(self.style.SUCCESS("CREATED"))
        else:
            self.stdout.write(self.style.SUCCESS("NON CREATED"))


    def add_arguments(self, parser):
        parser.add_argument("action", nargs="+", type=str)