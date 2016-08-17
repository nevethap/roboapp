from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quote(models.Model):
    symbol = models.CharField(max_length=20)
    quote = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField()


