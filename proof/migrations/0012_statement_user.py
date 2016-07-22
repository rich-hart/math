# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 16:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proof', '0011_auto_20160722_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
