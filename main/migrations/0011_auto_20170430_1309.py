# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 13:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170430_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactReason', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 30, 13, 9, 43, 209865, tzinfo=utc)),
        ),
    ]
