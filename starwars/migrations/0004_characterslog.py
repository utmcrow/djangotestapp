# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0003_requestlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharactersLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=6)),
                ('character_id', models.IntegerField()),
            ],
        ),
    ]
