from __future__ import unicode_literals

from django.db import models


class NewsGroup(models.Model):
    id = models.AutoField(primary_key=True)
    asset_Id = models.IntegerField()
    effect = models.FloatField()

    class Meta:
        db_table = "news_group"


class News(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=2000)
    timeStamp = models.DateTimeField()
    url = models.URLField(max_length=200)
    sentiment = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    group = models.ForeignKey(NewsGroup)

    class Meta:
        db_table = "news"
