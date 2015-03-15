# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20150314_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='client_email',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 3, 19, 1, 388000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
