# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-17 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20)),
                ('quote', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
