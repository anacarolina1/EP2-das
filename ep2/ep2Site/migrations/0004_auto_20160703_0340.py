# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 03:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ep2Site', '0003_auto_20160703_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='commentario',
            new_name='comentario',
        ),
    ]