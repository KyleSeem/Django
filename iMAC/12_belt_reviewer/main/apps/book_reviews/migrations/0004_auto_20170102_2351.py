# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 23:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0003_auto_20170102_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book_reviews.Book'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book_reviews.Review'),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login_reg.User'),
        ),
    ]
