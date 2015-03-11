# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0026_auto_20150311_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='date_of_contract_exchanged',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 1, 8, 45, 858000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
