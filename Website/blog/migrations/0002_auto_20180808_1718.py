# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-08 17:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 17, 18, 50, 608550, tzinfo=utc)),
        ),
    ]
