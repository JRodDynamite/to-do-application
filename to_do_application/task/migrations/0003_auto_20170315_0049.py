# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20170315_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='id',
            new_name='item_id',
        ),
    ]