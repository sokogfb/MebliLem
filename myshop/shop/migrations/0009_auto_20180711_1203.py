# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20180711_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ('-is_digit',), 'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.RenameField(
            model_name='feature',
            old_name='digit_value',
            new_name='is_digit',
        ),
    ]
