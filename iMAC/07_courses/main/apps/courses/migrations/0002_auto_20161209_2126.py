# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='description',
            old_name='course_id',
            new_name='course',
        ),
    ]
