# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20161019_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='answer',
            field=models.CharField(max_length=255),
        ),
    ]
