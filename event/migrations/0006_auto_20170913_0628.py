# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20170911_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(),
        ),
    ]
