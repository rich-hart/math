# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proof', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proof',
            name='diagram',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]