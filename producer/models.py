from django.db import models

from cft_app.base_models import AbstractCreateDateModel


class Producer(AbstractCreateDateModel):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name
