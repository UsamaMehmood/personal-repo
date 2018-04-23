# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-22 07:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20180421_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fan',
            name='purchase',
        ),
        migrations.RemoveField(
            model_name='item',
            name='purchase',
        ),
        migrations.AddField(
            model_name='fan',
            name='amount_paid',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fan',
            name='balance',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fan',
            name='date_purchased',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2018, 4, 22, 7, 10, 41, 814826, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fan',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fan',
            name='seller',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fan',
            name='total_amount',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='amount_paid',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='balance',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='date_purchased',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2018, 4, 22, 7, 11, 15, 516264, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='total_amount',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fan',
            name='design',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Design',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]