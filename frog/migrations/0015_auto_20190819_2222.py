# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-20 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frog', '0014_auto_20190818_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='small',
        ),
        migrations.RemoveField(
            model_name='siteconfig',
            name='image_size_cap',
        ),
        migrations.RemoveField(
            model_name='siteconfig',
            name='query_models',
        ),
        migrations.RemoveField(
            model_name='siteconfig',
            name='thumbnail_size',
        ),
        migrations.AlterField(
            model_name='siteconfig',
            name='default_gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frog.Gallery'),
        ),
        migrations.AlterField(
            model_name='siteconfig',
            name='site_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]