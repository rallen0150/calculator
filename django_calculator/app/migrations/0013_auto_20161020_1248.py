# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20161019_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_level',
            field=models.CharField(choices=[('o', 'Owner'), ('a', 'Account_User')], default='a', max_length=1, null=True),
        ),
    ]
