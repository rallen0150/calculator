# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='operator',
            field=models.CharField(choices=[('+', 'Add'), ('-', 'Subtract'), ('*', 'Multiply'), ('/', 'Divide')], max_length=1),
        ),
    ]
