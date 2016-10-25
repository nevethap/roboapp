# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 09:52
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robo_app', '0002_auto_20161018_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('subSector', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'asset',
            },
        ),
        migrations.CreateModel(
            name='AssetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('price', models.FloatField()),
                ('prediction', models.FloatField()),
                ('errorMargin', models.FloatField()),
                ('neteffect', models.FloatField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robo_app.Asset')),
            ],
            options={
                'db_table': 'assetdata',
            },
        ),
        migrations.CreateModel(
            name='MinimumSpanningTreeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetIdTwo', models.IntegerField()),
                ('slope', models.FloatField()),
                ('intercept', models.FloatField()),
                ('assetIdOne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robo_app.Asset')),
            ],
            options={
                'db_table': 'minimum_spanning_tree_model',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.IntegerField()),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
        migrations.CreateModel(
            name='PortfolioAssetMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('currentCount', models.IntegerField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robo_app.Asset')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robo_app.Portfolio')),
            ],
            options={
                'db_table': 'portfolio_asset_mapping',
            },
        ),
        migrations.CreateModel(
            name='RippleEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robo_app.Asset')),
            ],
            options={
                'db_table': 'ripple_effect',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastUpdateDate', models.DateTimeField()),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='TimeSeriesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coefficients', django.contrib.postgres.fields.jsonb.JSONField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robo_app.Asset')),
            ],
            options={
                'db_table': 'time_series_model',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('trade', models.CharField(max_length=50)),
                ('initialCount', models.IntegerField()),
                ('finalCount', models.IntegerField()),
                ('tradeCount', models.IntegerField()),
                ('price', models.FloatField()),
                ('mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robo_app.PortfolioAssetMapping')),
            ],
            options={
                'db_table': 'transaction',
            },
        ),
        migrations.RenameField(
            model_name='news',
            old_name='timeStamp',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='news',
            name='group',
        ),
        migrations.RemoveField(
            model_name='newsgroup',
            name='asset_id',
        ),
        migrations.AddField(
            model_name='news',
            name='asset',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='robo_app.Asset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsgroup',
            name='asset',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='robo_app.Asset'),
            preserve_default=False,
        ),
    ]
