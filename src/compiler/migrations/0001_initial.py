# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-16 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('language', models.CharField(max_length=20)),
                ('input', models.TextField()),
                ('owner', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Code List',
                'ordering': ['timestamp'],
                'verbose_name': 'Code List',
            },
        ),
    ]
