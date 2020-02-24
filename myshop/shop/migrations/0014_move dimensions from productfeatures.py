# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-23 18:22
from __future__ import unicode_literals

from django.db import migrations


def get_delimiter(s):
    for i in s:
        if not i.isdigit():
            return i


def move_dimensions_from_product_features(apps, schema_editor):
    Feature = apps.get_model('shop', 'Feature')
    Dimension = apps.get_model('shop', 'Dimension')
    ProductFeature = apps.get_model('shop', 'ProductFeature')
    productfeatures = ProductFeature.objects.filter(feature__is_digit=True)
    for pf in productfeatures:
        try:
            dimension = Dimension(feature=pf.feature, value=int(pf.value), unit=pf.unit, product=pf.product)
            dimension.save()
        except Exception as error:
            feature = Feature(name='Максимальна {}'.format(pf.feature.name), category=pf.product.category, is_digit=True)
            feature.save()
            values = pf.value.split(get_delimiter(pf.value))
            dimension_1 = Dimension(feature=pf.feature, value=int(values[0]), unit=pf.unit, product=pf.product)
            dimension_1.save()
            dimension_2 = Dimension(feature=feature, value=int(values[1]), unit=pf.unit, product=pf.product)
            dimension_2.save()
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200223_2016'),
    ]

    operations = [
        migrations.RunPython(move_dimensions_from_product_features),
    ]
