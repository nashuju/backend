# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jc', '0005_auto_20170714_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitrecord',
            name='is_crawler',
            field=models.CharField(default='0', max_length=32),
        ),
    ]
