# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20150424_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='reminder_within_days',
            field=models.IntegerField(default=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 25, 2, 32, 13, 652000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
