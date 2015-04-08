# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20150326_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(default=b'----', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 26, 22, 21, 31, 477000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
