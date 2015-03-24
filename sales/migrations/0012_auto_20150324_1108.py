# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0011_auto_20150324_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='letter1',
            field=models.CharField(default=0, max_length=40, blank=True),
            preserve_default=False,
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
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 0, 8, 47, 448000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
