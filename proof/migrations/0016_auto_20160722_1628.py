# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proof', '0015_auto_20160722_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='label',
            field=models.CharField(choices=[('DE', 'Definition'), ('AX', 'Axiom'), ('LE', 'Lemma'), ('TH', 'Theorem'), ('CO', 'Corollary')], default=None, max_length=2, null=True),
        ),
    ]
