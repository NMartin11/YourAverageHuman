# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-22 22:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180922_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 22, 22, 32, 48, 797815, tzinfo=utc)),
        ),
    ]
