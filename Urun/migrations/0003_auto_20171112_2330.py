# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 20:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Urun', '0002_auto_20171112_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='satici', to=settings.AUTH_USER_MODEL),
        ),
    ]