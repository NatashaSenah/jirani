# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood_name', models.TextField()),
                ('neighbourhood_location', models.TextField()),
                ('neighbourhood_occupant', models.TextField()),
            ],
        ),
    ]
