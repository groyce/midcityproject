# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 17:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer_activity', '0007_auto_20171101_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userevent',
            name='user_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]