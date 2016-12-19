# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161026_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(choices=[('Aerospace Engineering', 'Aerospace Engineering'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science & Engineering', 'Computer Science & Engineering'), ('Earth Sciences', 'Earth Sciences'), ('Electrical Engineering', 'Electrical Engineering'), ('Energy Science and Engineering', 'Energy Science and Engineering'), ('Humanities & Social Science', 'Humanities & Social Science'), ('Industrial Design Centre', 'Industrial Design Centre'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Metallurgical Engineering & Materials Science', 'Metallurgical Engineering & Materials Science'), ('Physics', 'Physics')], max_length=40),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(choices=[('Full', 'Full'), ('Half', 'Half'), ('Summer', 'Summer'), ('Winter', 'Winter')], max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('Autumn', 'Autumn'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Winter', 'Winter')], max_length=20),
        ),
    ]
