# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20150315_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 9, 7, 16, 192000, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='purchase',
            unique_together=set([('project', 'project_lot')]),
        ),
    ]
