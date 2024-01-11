import random

from django.core.management.base import BaseCommand

from cft_app.settings import DEFAULT_ROWS_NUMBER_TO_FILL_TABLE_WITH_TEST_DATA
from credit_application.models import CreditApplication
from producer.models import Producer
from product.models import Product


class Command(BaseCommand):
    help = 'Fill the product table with test data'

    def handle(self, *args, **options):
        applications = list(CreditApplication.objects.all())
        producers = list(Producer.objects.all())
        products = [
            Product(
                name=f'Product-{numb+1}',
                credit_application=random.choice(applications),
                producer=random.choice(producers),
            )
            for numb in range(DEFAULT_ROWS_NUMBER_TO_FILL_TABLE_WITH_TEST_DATA)
        ]
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'{len(products)} row was successfully added to product table'))
