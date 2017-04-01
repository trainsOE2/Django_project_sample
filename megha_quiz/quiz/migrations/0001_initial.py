# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000, verbose_name='Correct answer')),
                ('option_1', models.CharField(max_length=100, verbose_name='Choice 1')),
                ('option_2', models.CharField(max_length=100, verbose_name='Choice 2')),
                ('option_3', models.CharField(max_length=100, verbose_name='Choice 3')),
                ('correct_answer', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], verbose_name='Correct answer')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'questions',
            },
        ),
    ]
