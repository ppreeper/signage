# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-23 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signs', '0011_auto_20161222_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]