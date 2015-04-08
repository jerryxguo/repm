# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20150327_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='client',
            field=models.ForeignKey(to='config.Client'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 3, 45, 2, 690000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
