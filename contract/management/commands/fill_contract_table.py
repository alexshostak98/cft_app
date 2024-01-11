import random

from django.core.management.base import BaseCommand

from contract.models import Contract
from credit_application.models import CreditApplication


class Command(BaseCommand):
    help = 'Fill the contract table with test data'

    def handle(self, *args, **options):
        applications = CreditApplication.objects.all()
        contracts = [
            Contract(
                number=random.randint(10**10, 10**11),
                credit_application=application,
            )
            for application in applications
        ]
        Contract.objects.bulk_create(contracts)
        self.stdout.write(self.style.SUCCESS(f'{len(contracts)} row was successfully added to contract table'))
