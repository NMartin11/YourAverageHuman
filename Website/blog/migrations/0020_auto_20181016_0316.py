# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-16 03:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20181016_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 16, 3, 16, 51, 894546, tzinfo=utc)),
        ),
    ]
