# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-23 02:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0002_auto_20171216_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='article',
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
