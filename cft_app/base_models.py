from django.db import models


class AbstractCreateDateModel(models.Model):
    """Abstract model with create date"""

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
