# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uyelik', '0008_auto_20171024_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='profil_foto',
            field=models.ImageField(blank=True, null=True, upload_to='static/image/avatars/', verbose_name='Avatar Seçin'),
        ),
    ]
