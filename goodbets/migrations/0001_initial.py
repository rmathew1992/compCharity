# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=150)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Chipin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('is_challenger', models.BooleanField(default=b'False')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chipin',
            name='user',
            field=models.ForeignKey(to='goodbets.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='challenge',
            name='challengees',
            field=models.ManyToManyField(to='goodbets.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='challenge',
            name='charity',
            field=models.ForeignKey(to='goodbets.Charity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='challenge',
            name='chipins',
            field=models.ManyToManyField(to='goodbets.Chipin'),
            preserve_default=True,
        ),
    ]
