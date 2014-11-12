# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0002_auto_20141109_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'uncompleted'), (1, b'completed'), (2, b'failed')]),
            preserve_default=True,
        ),
    ]
