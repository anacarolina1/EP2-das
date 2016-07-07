# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 01:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ep2Site', '0004_auto_20160703_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='data_pub',
        ),
        migrations.AddField(
            model_name='review',
            name='data_lancamento',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 1, 52, 37, 570093, tzinfo=utc), verbose_name=b'data de lancamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='url',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='musica',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Musica',
        ),
    ]