# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Urun', '0014_auto_20171118_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='urun_ktarihi',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
