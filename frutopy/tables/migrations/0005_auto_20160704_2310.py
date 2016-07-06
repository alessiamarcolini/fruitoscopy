# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 23:10
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_auto_20160704_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='fruit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sample',
            name='ml_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tables.ML_Model'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sp_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tables.SP_Model'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='spectrum',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None),
        ),
        migrations.AlterField(
            model_name='sample',
            name='tmstp',
            field=models.DateTimeField(null=True),
        ),
    ]
