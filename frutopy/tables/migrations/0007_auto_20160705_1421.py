# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_auto_20160705_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='image_path',
            field=models.FilePathField(null=True, verbose_name='/home/l-brognoli/pics/'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='label',
            field=models.SmallIntegerField(choices=[(0, 'not ripe'), (1, 'ripe'), (2, 'too ripe')]),
        ),
        migrations.AlterField(
            model_name='sample',
            name='label_is_right',
            field=models.NullBooleanField(default=False),
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
    ]
