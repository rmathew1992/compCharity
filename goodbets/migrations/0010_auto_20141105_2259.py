# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0009_auto_20141029_1508'),
    ]

    operations = [
    	migrations.RenameModel(
    		old_name='Bet',
    		new_name='Chipin'
    	),
    	migrations.RenameField(
    		model_name='Challenge',
    		old_name='bets',
    		new_name='chipins'
    	)
    ]
