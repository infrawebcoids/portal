from django.db import models

from apps.infra.models import Storage


class Aggregates(models.Model):
    name = models.CharField(max_length=255)
    full_size = models.CharField(max_length=255)
    used_size = models.CharField(max_length=255)
    available_size = models.CharField(max_length=255)
    name_storage = models.ForeignKey(Storage, on_delete=models.CASCADE)

