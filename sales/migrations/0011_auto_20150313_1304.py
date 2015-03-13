# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_auto_20150312_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 2, 4, 42, 952000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='project_lot',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
