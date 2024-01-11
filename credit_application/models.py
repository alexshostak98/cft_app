from django.db import models

from cft_app.base_models import AbstractCreateDateModel


class CreditApplication(AbstractCreateDateModel):
    number = models.BigIntegerField(unique=True, null=False, blank=False)

    def __str__(self):
        return f'Credit application - {self.number}'
