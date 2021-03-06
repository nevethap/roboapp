# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('headline', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('timeStamp', models.DateTimeField()),
                ('url', models.URLField()),
                ('sentiment', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='NewsGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_Id', models.IntegerField()),
                ('effect', models.FloatField()),
            ],
            options={
                'db_table': 'news_group',
            },
        ),
    ]
