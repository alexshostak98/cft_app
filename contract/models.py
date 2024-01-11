from django.db import models

from cft_app.base_models import AbstractCreateDateModel
from credit_application.models import CreditApplication


class Contract(AbstractCreateDateModel):
    number = models.BigIntegerField(unique=True, blank=False, null=False)
    credit_application = models.OneToOneField(
        CreditApplication,
        on_delete=models.CASCADE,
        related_name='contract',
    )

    def __str__(self):
        return f'Contract - {self.number}'
