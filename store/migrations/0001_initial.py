# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-21 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(db_column='Design', max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Design',
                'verbose_name_plural': 'Designs',
            },
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('design', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.Design')),
            ],
            options={
                'verbose_name': 'Fan',
                'verbose_name_plural': 'Fans',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(db_column='Seller', max_length=150, unique=True)),
                ('paid', models.PositiveIntegerField(db_column='Amount Paid', max_length=20)),
                ('item', models.CharField(max_length=200)),
                ('balance', models.PositiveIntegerField(max_length=20)),
                ('total_amount', models.PositiveIntegerField(db_column='Amount', max_length=20)),
                ('quanitity', models.PositiveIntegerField(db_column='Quantity', max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True, db_column='Date purchased on')),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
            },
        ),
        migrations.AddField(
            model_name='fan',
            name='purchase',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.Purchase'),
        ),
    ]
