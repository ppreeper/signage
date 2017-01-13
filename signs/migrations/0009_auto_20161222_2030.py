# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-23 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signs', '0008_auto_20161222_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screen',
            name='images',
        ),
        migrations.AddField(
            model_name='screen',
            name='images',
            field=models.ManyToManyField(to='signs.ImageQueue'),
        ),
        migrations.RemoveField(
            model_name='screen',
            name='newsitems',
        ),
        migrations.AddField(
            model_name='screen',
            name='newsitems',
            field=models.ManyToManyField(to='signs.NewsitemQueue'),
        ),
        migrations.RemoveField(
            model_name='screen',
            name='tickers',
        ),
        migrations.AddField(
            model_name='screen',
            name='tickers',
            field=models.ManyToManyField(to='signs.TickerQueue'),
        ),
    ]
