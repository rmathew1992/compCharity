# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0010_auto_20141105_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='chipin',
            name='is_challenger',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
