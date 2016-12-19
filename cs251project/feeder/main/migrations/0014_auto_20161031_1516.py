# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20161031_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback_o',
            name='feed',
        ),
        migrations.AddField(
            model_name='feedback_o',
            name='feed',
            field=models.ManyToManyField(to='main.Feedback_f'),
        ),
        migrations.RemoveField(
            model_name='feedback_s',
            name='feed',
        ),
        migrations.AddField(
            model_name='feedback_s',
            name='feed',
            field=models.ManyToManyField(to='main.Feedback_f'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='main.Course'),
        ),
    ]