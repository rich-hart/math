# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proof', '0012_statement_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='user',
        ),
    ]
