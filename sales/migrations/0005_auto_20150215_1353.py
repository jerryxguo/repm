# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20150214_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date_of_BOD_paid',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date_of_EOI_sent',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date_of_contract_exchanged',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date_of_contract_received',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date_of_contract_signed',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date_of_settlement',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
    ]
