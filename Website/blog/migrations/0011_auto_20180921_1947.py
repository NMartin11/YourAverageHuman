# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-21 19:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180829_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 21, 19, 47, 15, 171414, tzinfo=utc)),
        ),
    ]
