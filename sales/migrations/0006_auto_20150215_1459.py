# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20150215_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='letter1',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='letter2',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='letter3',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='note',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
