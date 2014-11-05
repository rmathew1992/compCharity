# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0011_chipin_is_challenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chipin',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chipin',
            name='is_challenger',
            field=models.BooleanField(default=b'False'),
        ),
    ]
