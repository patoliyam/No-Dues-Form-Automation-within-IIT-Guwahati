# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_account_onlinecc_submitthesis'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='account_approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='onlinecc_approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='thesis_manager_approval',
            field=models.BooleanField(default=True),
        ),
    ]