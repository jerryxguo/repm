# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0023_auto_20150311_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='accumulation_bonus',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sales',
            name='date_of_paid',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 0, 14, 56, 921000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
