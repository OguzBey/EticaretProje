# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 16:50
from __future__ import unicode_literals

import Profil.storage
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('Uyelik', '0011_auto_20171029_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profil_foto',
            field=stdimage.models.StdImageField(blank=True, null=True, storage=Profil.storage.OverwriteStorage(), upload_to=''),
        ),
    ]