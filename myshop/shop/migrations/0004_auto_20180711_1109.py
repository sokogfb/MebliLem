# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 08:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180711_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ('feature_values__unit',), 'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики'},
        ),
    ]
