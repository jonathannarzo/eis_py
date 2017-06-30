# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161126_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='basic_salary',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='monthly_allowance',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
    ]