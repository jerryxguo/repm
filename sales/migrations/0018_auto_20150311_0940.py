# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0017_auto_20150310_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='leader',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 22, 40, 31, 152000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
