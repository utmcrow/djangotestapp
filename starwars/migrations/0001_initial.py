# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('height', models.IntegerField()),
                ('mass', models.IntegerField()),
                ('hair_color', models.CharField(max_length=16)),
                ('skin_color', models.CharField(max_length=16)),
                ('eye_color', models.CharField(max_length=16)),
                ('birth_year', models.IntegerField()),
                ('gender', models.CharField(max_length=8)),
            ],
        ),
    ]
