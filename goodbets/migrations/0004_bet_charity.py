# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0003_auto_20141012_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='charity',
            field=models.CharField(default=b'Nitya', max_length=100),
            preserve_default=True,
        ),
    ]
