# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-18 20:07
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('email_validation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='email',
            managers=[
                ('emailManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
