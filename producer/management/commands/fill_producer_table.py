from django.core.management.base import BaseCommand

from cft_app.settings import DEFAULT_ROWS_NUMBER_TO_FILL_TABLE_WITH_TEST_DATA
from producer.models import Producer


class Command(BaseCommand):
    help = 'Fill the producer table with test data'

    def handle(self, *args, **options):
        producers = [
            Producer(name=f'Producer-{numb+1}')
            for numb in range(DEFAULT_ROWS_NUMBER_TO_FILL_TABLE_WITH_TEST_DATA)
        ]
        Producer.objects.bulk_create(producers)
        self.stdout.write(self.style.SUCCESS(f'{len(producers)} row was successfully added to producer table'))
