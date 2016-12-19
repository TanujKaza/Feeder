# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 20:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_student_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
