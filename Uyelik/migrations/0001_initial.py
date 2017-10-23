# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 01:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Uyelik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullanici_tipi', models.CharField(choices=[('MS', 'Müşteri'), ('ST', 'Satıcı')], max_length=2)),
                ('adres', models.CharField(max_length=100)),
                ('dogum_tarihi', models.DateField()),
                ('kullanici', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
