# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20150311_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-modified_date'], 'verbose_name': 'Sale', 'verbose_name_plural': 'Sale Records'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 22, 35, 20, 717000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
