# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=999, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
