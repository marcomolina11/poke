# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20160905_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='alias',
            field=models.CharField(default='Marco', max_length=45),
            preserve_default=False,
        ),
    ]
