# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20150320_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='lines',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 8, 19, 9, 215000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
