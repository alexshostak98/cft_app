import random

from django.core.management.base import BaseCommand

from cft_app.settings import DEFAULT_ROWS_NUMBER_TO_FILL_TABLE_WITH_TEST_DATA
from credit_application.models import CreditApplication


class Command(BaseCommand):
    help = 'Fill the credit_application table with test data'

    def handle(self, *args, **options):
        applications = [
            CreditApplication(number=random.randint(10**10, 10**11))
            for _ in range(DEFAULT_ROWS_NUMBER_TO_FILL_TABLE_WITH_TEST_DATA)
        ]
        CreditApplication.objects.bulk_create(applications)
        self.stdout.write(
            self.style.SUCCESS(f'{len(applications)} row was successfully added to credit_application table'),
        )
