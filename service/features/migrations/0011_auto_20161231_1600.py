# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-31 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0010_auto_20161017_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='private_key',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='public_key',
            field=models.TextField(blank=True),
        ),
    ]