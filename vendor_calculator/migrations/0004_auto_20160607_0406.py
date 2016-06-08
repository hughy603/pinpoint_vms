# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-07 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_calculator', '0003_auto_20160604_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='vendor',
            name='contact',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='vendor',
            name='customer_service',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='vendor',
            name='mistakes',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='vendor',
            name='product_options',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='vendor',
            name='turnaround_time',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='vendor',
            name='website',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='vendor',
            name='where_to_place_order',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]