# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20180125_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='credit',
            field=models.IntegerField(default=4),
        ),
    ]