# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161026_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('Autumn', 'Autumn'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Winter', 'Winter')], max_length=20),
        ),
    ]
