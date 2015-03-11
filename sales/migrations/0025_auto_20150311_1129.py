# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0024_auto_20150311_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='bonus_paid',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sales',
            name='bonus_unpaid',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sales',
            name='number_of_sales',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 0, 29, 55, 507000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
