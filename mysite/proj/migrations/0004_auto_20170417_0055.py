# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0003_auto_20170416_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='blurb',
            name='reading',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='goodreads_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_filepath',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
