# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodbets', '0006_auto_20141029_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
