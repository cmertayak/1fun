from django.db import models
from website.core.models import TimeStampedModel


class Lead(TimeStampedModel):
    email = models.EmailField()