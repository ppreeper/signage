# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-16 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageTitle', models.CharField(max_length=200)),
                ('imageUrl', models.CharField(max_length=200)),
                ('imageYear', models.CharField(max_length=4)),
                ('imageMonth', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Newsitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsTitle', models.CharField(max_length=200)),
                ('newsText', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signs.Image')),
                ('newsitems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signs.Newsitem')),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickerItem', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='screen',
            name='tickers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signs.Ticker'),
        ),
    ]
