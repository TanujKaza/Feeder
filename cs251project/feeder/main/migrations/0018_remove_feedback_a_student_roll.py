# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20161101_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback_a',
            name='student_roll',
        ),
    ]
