# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 00:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proof', '0005_auto_20160721_0050'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proof',
            new_name='Theorem',
        ),
    ]