# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0028_auto_20150311_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='commission_1',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='commission_2',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 3, 21, 19, 795000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
