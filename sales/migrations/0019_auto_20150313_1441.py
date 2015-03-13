# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0018_auto_20150313_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 3, 41, 23, 344000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
