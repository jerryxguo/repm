# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sale',
            new_name='Sales',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='sale',
            new_name='sales',
        ),
        migrations.AlterField(
            model_name='item',
            name='date_of_BOD_paid',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 55, 35, 440000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='date_of_EOI_sent',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 55, 35, 440000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='date_of_contract_exchanged',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 55, 35, 440000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='date_of_contract_received',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 55, 35, 440000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='date_of_contract_signed',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 55, 35, 440000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='date_of_settlement',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 14, 9, 55, 35, 440000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
