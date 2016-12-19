# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20161030_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_f',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_title', models.CharField(max_length=200)),
                ('feed_deadline', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='feedback_o',
            name='course',
        ),
        migrations.RemoveField(
            model_name='feedback_o',
            name='qn_deadline',
        ),
        migrations.RemoveField(
            model_name='feedback_s',
            name='course',
        ),
        migrations.RemoveField(
            model_name='feedback_s',
            name='qn_deadline',
        ),
        migrations.AddField(
            model_name='assignment',
            name='ass_published',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback_o',
            name='feed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Feedback_f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback_s',
            name='feed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Feedback_f'),
            preserve_default=False,
        ),
    ]