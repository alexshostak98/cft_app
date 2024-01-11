from django.db import models

from cft_app.base_models import AbstractCreateDateModel
from credit_application.models import CreditApplication
from producer.models import Producer


class Product(AbstractCreateDateModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    credit_application = models.ForeignKey(
        CreditApplication,
        on_delete=models.CASCADE,
        related_name='products',
    )
    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        related_name='products',
    )

    def __str__(self):
        return self.name
