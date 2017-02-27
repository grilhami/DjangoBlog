# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-08 20:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_publish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created', 'updated']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 8, 20, 58, 52, 987516, tzinfo=utc)),
            preserve_default=False,
        ),
    ]