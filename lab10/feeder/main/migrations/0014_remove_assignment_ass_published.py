# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 08:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20161031_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='ass_published',
        ),
    ]