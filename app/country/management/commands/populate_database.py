import time
from django.core.management.base import BaseCommand, CommandError
from utilities.functions import get_data

class Command(BaseCommand):
    '''Django command to populate database with restcountries data.'''

    def handle(self, *args, **options):
        self.stdout.write('Database is being populated. Please wait...')
        try:
            get_data()
        except Exception as e:
            raise CommandError(str(e))

        self.stdout.write(self.style.SUCCESS('Database successfully populated by restcountries data!'))
