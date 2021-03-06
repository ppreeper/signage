# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-23 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signs', '0003_auto_20160916_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='imageTitle',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='imageMonth',
        ),
        migrations.RemoveField(
            model_name='image',
            name='imageUrl',
        ),
        migrations.RemoveField(
            model_name='image',
            name='imageYear',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='', upload_to='images/beerthumbs/'),
            preserve_default=False,
        ),
    ]
