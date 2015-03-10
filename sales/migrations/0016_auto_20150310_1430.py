# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0015_auto_20150310_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='id',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 3, 30, 29, 285000, tzinfo=utc), serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
