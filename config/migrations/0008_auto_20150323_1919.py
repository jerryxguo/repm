# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_auto_20150320_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notify_type',
            field=models.CharField(default=b'NS', max_length=2, choices=[(b'NS', b'NOTIFY_CONSULTANT'), (b'NA', b'NOTIFY_ADMIN'), (b'NC', b'NOTIFY_CLIENT')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 8, 19, 9, 210000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
