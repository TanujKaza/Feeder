# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_assignment_ass_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='ass_published',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
