# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_auto_20150327_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.AlterField(
            model_name='client',
            name='full_name',
            field=models.CharField(max_length=30, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sales',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 27, 4, 16, 38, 376000, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
