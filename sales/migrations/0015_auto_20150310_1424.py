# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0014_auto_20150309_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='deposit',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 3, 24, 51, 708000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
