# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 04:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170430_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='Yerevan', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 1, 4, 40, 52, 757818, tzinfo=utc)),
        ),
    ]
