# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20161102_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback_a',
            name='feed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Feedback_o'),
        ),
    ]