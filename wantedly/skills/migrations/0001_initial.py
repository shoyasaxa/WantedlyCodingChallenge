# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endorsements', models.PositiveSmallIntegerField()),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.Skill')),
                ('user_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
        ),
    ]