# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20150326_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='reciever',
            new_name='receiver',
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 26, 4, 25, 52, 476000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
