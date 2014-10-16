# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='title',
            field=models.CharField(default=b'', max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]