# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 21:28
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        ('matching', '0003_auto_20160128_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helprequest',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.',
                                                  through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]