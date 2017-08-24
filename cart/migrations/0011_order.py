# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-24 17:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arabica', '0007_auto_20170824_2049'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0010_auto_20170824_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arabica.Address')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
