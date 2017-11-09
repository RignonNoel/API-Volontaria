# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-03 21:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryToken',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.Token')),
                ('expires', models.DateTimeField(default=datetime.datetime(2017, 11, 3, 21, 29, 11, 67255, tzinfo=utc))),
            ],
            bases=('authtoken.token',),
        ),
    ]