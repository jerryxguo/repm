# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0013_auto_20150309_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='deposit',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 2, 38, 32, 6000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
