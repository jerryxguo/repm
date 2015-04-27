# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20150425_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 25, 9, 46, 21, 944000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
