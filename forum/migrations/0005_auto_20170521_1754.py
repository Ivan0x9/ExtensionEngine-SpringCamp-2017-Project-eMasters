# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20170521_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='message',
            new_name='add_new_comment',
        ),
    ]
