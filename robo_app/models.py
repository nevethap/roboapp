from __future__ import unicode_literals

from django.db import models


class NewsGroup(models.Model):
    id = models.AutoField(primary_key=True)
    asset_id = models.IntegerField()
    effect = models.FloatField()

    class Meta:
        db_table = "news_group"


class News(models.Model):
    id = models.AutoField(primary_key=True)
    timeStamp = models.DateTimeField()
    group = models.ForeignKey(NewsGroup, null=True)
    headline = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    sentiment = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)

    class Meta:
        db_table = "news"
