# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0020_auto_20150311_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='commisionn_1_date',
            new_name='commission_1_date',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='commisionn_2_date',
            new_name='commission_2_date',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 23, 59, 40, 160000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
