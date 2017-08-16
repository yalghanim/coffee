# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-16 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arabica', '0004_auto_20170816_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Powder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powder_type', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Syrup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syrup_type', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
        ),
        migrations.RemoveField(
            model_name='coffeebean',
            name='bean_price',
        ),
        migrations.RemoveField(
            model_name='coffeebean',
            name='coffee_bean',
        ),
        migrations.AddField(
            model_name='coffeebean',
            name='bean_type',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffeebean',
            name='price',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roast',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=4),
        ),
        migrations.AlterField(
            model_name='roast',
            name='roast_type',
            field=models.CharField(max_length=30),
        ),
    ]
