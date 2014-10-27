# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0003_auto_20141012_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='title',
            field=models.CharField(default=b'', max_length=150),
        ),
    ]
