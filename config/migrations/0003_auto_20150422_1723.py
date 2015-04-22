# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20150422_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='lot',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 22, 7, 23, 21, 437000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
