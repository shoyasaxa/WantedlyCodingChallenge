# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-23 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20171222_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='endorsed_skill_set',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='skills.SkillSet'),
            preserve_default=False,
        ),
    ]