# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Uyelik', '0003_auto_20171022_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='myuser',
            new_name='user',
        ),
    ]