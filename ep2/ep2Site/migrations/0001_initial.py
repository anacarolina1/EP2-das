# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pub', models.DateTimeField(verbose_name=b'data de publicacao')),
                ('nome_de_usuario', models.CharField(max_length=100)),
                ('commentario', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('musica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep2Site.Musica')),
            ],
        ),
    ]
