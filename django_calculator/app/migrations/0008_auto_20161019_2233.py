# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20161019_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={},
        ),
        migrations.AlterField(
            model_name='profile',
            name='access_level',
            field=models.CharField(choices=[('o', 'Owner'), ('a', 'Account_User')], default='a', max_length=1),
        ),
    ]
