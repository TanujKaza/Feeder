# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 12:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20161030_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instruct',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]