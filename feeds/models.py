from __future__ import unicode_literals

from django.db import models


# Create your models here.
class RSSFeed(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=2000)
    published = models.DateTimeField()
    link = models.URLField(max_length=200)
    content_file = models.CharField(max_length=1000, default = "articles/default_content.txt")
    sentiment_score = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
