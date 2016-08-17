from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RSSFeed(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    published = models.DateTimeField()
    link = models.URLField(max_length=200)
