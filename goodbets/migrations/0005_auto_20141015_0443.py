# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0004_bet_charity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(max_length=50),
        ),
    ]
