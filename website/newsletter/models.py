from django.db import models
from website.core.models import TimeStampedModel


class Lead(TimeStampedModel):
    email = models.EmailField(unique=True)
    validation_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'lead'
