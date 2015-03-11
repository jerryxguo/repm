# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0025_auto_20150311_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date_of_EOI_sent',
            field=models.DateField(null=True, verbose_name=b'Date EOI Sent', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 1, 4, 44, 50000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
