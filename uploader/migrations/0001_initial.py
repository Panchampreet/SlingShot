# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images/', verbose_name='Image')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
