# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-29 22:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180829_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 29, 22, 38, 39, 323672, tzinfo=utc)),
        ),
    ]
