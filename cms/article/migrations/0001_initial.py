# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Article title')),
                ('slug', models.SlugField(max_length=250, verbose_name='Article slug')),
                ('image', models.ImageField(upload_to='article', verbose_name='Article image')),
                ('content', models.TextField(verbose_name='Article content text')),
            ],
        ),
    ]