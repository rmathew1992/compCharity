# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 22, 49, 34, 509184), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chipin',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 22, 49, 45, 305436), auto_now=True),
            preserve_default=False,
        ),
    ]
