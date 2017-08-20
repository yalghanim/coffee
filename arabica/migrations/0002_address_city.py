# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 18:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arabica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('block', models.PositiveIntegerField()),
                ('street', models.CharField(max_length=50)),
                ('building', models.CharField(max_length=50)),
                ('avenue', models.PositiveIntegerField(blank=True, default='', null=True)),
                ('floor', models.PositiveIntegerField(blank=True, default='', null=True)),
                ('apt_number', models.PositiveIntegerField(blank=True, default='', null=True)),
                ('extra_directions', models.TextField(blank=True, default='', null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
