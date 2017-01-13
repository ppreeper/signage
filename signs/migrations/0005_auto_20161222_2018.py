# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-23 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signs', '0004_auto_20161222_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagequeue',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='imagequeue',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='signs.ImageQueue'),
            preserve_default=False,
        ),
    ]