# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 13:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170504_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='firstName',
            new_name='fullName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='lastName',
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 13, 41, 15, 96759, tzinfo=utc)),
        ),
    ]