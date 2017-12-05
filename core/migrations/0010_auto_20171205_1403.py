# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_system_view_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemversion',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='systemversion',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='system',
            name='view_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='systemfeatures',
            name='description',
            field=models.TextField(help_text='This field supports Markdown Syntax'),
        ),
        migrations.AlterField(
            model_name='systemversion',
            name='description',
            field=models.TextField(blank=True, default='', help_text='This field support Markdown Syntax'),
        ),
        migrations.AlterField(
            model_name='systemversion',
            name='history',
            field=models.TextField(blank=True, default='', help_text='This field support Markdown Syntax'),
        ),
    ]
