# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-14 22:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apiVolontaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporarytoken',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 14, 22, 17, 14, 716927, tzinfo=utc)),
        ),
    ]
