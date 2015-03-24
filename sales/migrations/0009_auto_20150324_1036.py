# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20150323_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='lines',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 23, 36, 11, 757000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
