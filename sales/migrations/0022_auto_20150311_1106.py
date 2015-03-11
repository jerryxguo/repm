# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0021_auto_20150311_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='tyler_commission_1_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='tyler_commission_2_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 0, 6, 33, 291000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
