# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0008_bet_charity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='charity',
        ),
        migrations.AddField(
            model_name='challenge',
            name='charity',
            field=models.ForeignKey(default=1, to='goodbets.Charity'),
            preserve_default=False,
        ),
    ]
