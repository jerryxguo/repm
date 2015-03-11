# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0022_auto_20150311_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='bonus',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 0, 11, 29, 224000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
