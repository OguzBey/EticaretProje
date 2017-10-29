# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 20:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Uyelik', '0007_auto_20171024_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='myuser', to=settings.AUTH_USER_MODEL),
        ),
    ]